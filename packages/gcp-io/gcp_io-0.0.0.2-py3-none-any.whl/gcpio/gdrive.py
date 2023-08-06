import io
from PIL import Image
from .utils import auth_token, get_logger, token
from torch.utils.data import Dataset
from torchvision import transforms
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError

# import asyncio
# import time

logger = get_logger(__name__)


class Gdrive:
    """Google Drive class that has functions to return the metadata of files in a Google Drive folder and generate torch datasets from files in google drive
    Available functions: get_files_metadata, create_dataset, download_files_from_drive
    """

    def __init__(self) -> None:
        self.token = token()

    @auth_token
    def get_files_metadata(
        self,
        folder_id,
        page_size=500,
        file_type=None,
        replace_query=None,
    ) -> dict:
        """Retrieves the metadata of files present in the Drive folder ID passed as an argument to the function.

        Args:
            folder_id (str): The folder id in google drive (can be found at the end of url in web browser).
            page_size (int, optional): number of files to get back in response. Defaults to 500.
            file_type (MimeType, optional): Can be used to get the files of a certain MimeType for example image/png. Defaults to None.(gets all files in the given folder)
            replace_query (str, optional): Can be used to make more complex queries. This uses q parameter from Gdrive API documentation. Defaults to None.

        Returns:
            dict: returns a file dictionary that has the files and len as keys. files has a list of file objects as response
        """
        try:
            logger.debug(
                f"Args received by get_files_metadata func - {folder_id,page_size,file_type,replace_query}"
            )
            files = {}
            query = f"parents in '{folder_id}' and mimeType != 'application/vnd.google-apps.folder'"

            if file_type:
                query = query + f"and mimeType='{file_type}'"
            if replace_query:
                query = replace_query

            service = build("drive", "v3", credentials=self.token)
            page_size = page_size
            next_page_token = None
            results = (
                service.files()
                .list(
                    pageSize=page_size,
                    fields="nextPageToken, files(id, name, mimeType, webContentLink)",
                    q=query,
                )
                .execute()
            )
            items = results.get("files", [])
            if not items:
                logger.info("No files found with the given parameters")
                return

            next_page_token = results.get("nextPageToken")
            while next_page_token:
                results = (
                    service.files()
                    .list(
                        pageToken=next_page_token,
                        pageSize=page_size,
                        fields="nextPageToken, files(id, name, mimeType, webContentLink)",
                        q=query,
                    )
                    .execute()
                )
                items = items + results.get("files", [])
                next_page_token = results.get("nextPageToken")

            files["files"] = items
            files["len"] = len(items)

            return files
        except Exception as e:
            logger.error(f"{e}")

    def reformat_response(self, data):
        data_dict = {}
        for obj in data:
            data_dict[obj.get("name").split(".")[0]] = {
                "mimeType": obj.get("mimeType"),
                "id": obj.get("id"),
            }
        return data_dict

    @auth_token
    def create_dataset(
        self,
        data_folder_id,
        labels_folder_id=None,
        page_size=500,
        data_file_type=None,
        labels_file_type=None,
        replace_query=None,
        skip_labels=False,
    ):
        try:
            logger.debug(
                f"Args received by create_dataset func - {data_folder_id,labels_folder_id, page_size,data_file_type,labels_file_type,replace_query,skip_labels}"
            )
            logger.info("Fetching data from G Drive")

            if skip_labels:
                logger.debug(f"skip labels set to - {skip_labels}")

                data_files_metadata_dict = self.get_files_metadata(
                    data_folder_id,
                    page_size=page_size,
                    file_type=data_file_type,
                    replace_query=replace_query,
                )
                if data_files_metadata_dict:
                    data_files = self.reformat_response(
                        data_files_metadata_dict.get("files")
                    )
                    logger.info("Generating dataset.")
                    dataset = GdriveDataset(
                        data_files, None, self.download_files_from_drive
                    )
                    logger.info("Dataset generated.")
                    return dataset

            else:
                data_files_metadata_dict = self.get_files_metadata(
                    data_folder_id,
                    page_size=page_size,
                    file_type=data_file_type,
                    replace_query=replace_query,
                )
                if data_files_metadata_dict:
                    data_files = self.reformat_response(
                        data_files_metadata_dict.get("files")
                    )

                labels_files_metadata_dict = self.get_files_metadata(
                    labels_folder_id,
                    page_size=page_size,
                    file_type=labels_file_type,
                    replace_query=replace_query,
                )
                if labels_files_metadata_dict:
                    label_files = self.reformat_response(
                        labels_files_metadata_dict.get("files")
                    )
                if data_files_metadata_dict and labels_files_metadata_dict:

                    if data_files_metadata_dict.get(
                        "len"
                    ) == labels_files_metadata_dict.get("len"):
                        logger.info("Generating dataset.")
                        dataset = GdriveDataset(
                            data_files, label_files, self.download_files_from_drive
                        )
                        logger.info("Dataset generated.")
                        return dataset

                    elif labels_files_metadata_dict.get("len") == 1:
                        "TODO write a func to download the labels file and a validation function to check if number of data samples match with number of rows using pandas"
                        "Convert the label file into similar format as the others and pass it to the Dataset class"
                        raise NotImplementedError("Single label file")
                    else:
                        raise Exception(
                            "Number of data samples different from number of label files found."
                        )

                return None
        except NotImplementedError as e:
            logger.error(f"{e} is not implemented yet.")
        except Exception as e:
            logger.error(f"Exception at create_dataset func: {e}")

    def download_files_from_drive(self, file_id) -> bytes:
        """Downloads a file from GDrive with the given fileid and returns the file binary

        Args:
            file_id (str): file id

        Returns:
            bytes: file binary data
        """
        try:
            service = build("drive", "v3", credentials=self.token)
            request = service.files().get_media(fileId=file_id)
            file = io.BytesIO()
            downloader = MediaIoBaseDownload(file, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()

        except HttpError as error:
            logger.error(f"An error occurred while downloading file:{file_id} {error}")
            file = None

        if file:
            return file.getvalue()


class GdriveDataset(Dataset):  # pragma: no cover
    """Make API calls and create a dataset with file binaries"""

    def __init__(
        self, data_file_names_list, labels_file_names_list, download_func
    ) -> None:
        self.data = data_file_names_list
        self.labels = labels_file_names_list
        self.keys = list(data_file_names_list)
        self.download_func = download_func
        self.transorm = transforms.Compose([transforms.ToTensor()])

    def __len__(self) -> int:
        return len(self.keys)

    # async def get_files_from_drive(self, indices) -> dict:
    #     print(time.time())
    #     await (time.sleep(10))
    #     print(indices)

    #     return indices

    # async def test_func(self, index):
    #     await asyncio.gather(*[self.get_files_from_drive(index) for index in index])
    #     return 1

    def __getitem__(self, index) -> None:  # pragma: no cover
        """# This function cuurently makes API calls synchronously.
        Making these API calls async would improve the performance significantly
        but that would require updating the Datafetcher functions from the torch dataloader.
        More details about this in the documentation.

        Args:
            index (_type_): For this use case it's better to use a batch index hence a list of numbers
            in range(0, len(data)) with length as batch size from dataloader is expected

        Returns:
            [(Images,labels)]
        """

        if isinstance(index, int):
            index = [index]

        batched_data = []
        for i in index:
            file_name = self.keys[i]
            data_file_id = self.data.get(file_name).get("id")
            data_file_b_content = self.download_func(data_file_id)
            label_file_b_content = []
            if self.labels:
                label_file_id = self.labels.get(file_name).get("id")
                label_file_b_content = self.download_func(label_file_id)

            image = Image.open(io.BytesIO(data_file_b_content))
            image = self.transorm(image)
            batched_data.append((image, label_file_b_content))

        return batched_data
