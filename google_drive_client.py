from dataclasses import asdict
import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

from upload_file_info import UploadFileInfo


class GoogleDriveClient:
    """GoogleDrive操作用クライアント"""
    def __init__(self) -> None:
        self.drive = self.__create_instance()

    def __create_instance(self) -> GoogleDrive:
        """GoogleDriveインスタンスの生成"""
        gauth = GoogleAuth()
        scope = ["https://www.googleapis.com/auth/drive"]
        gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(os.environ["SERVICE_ACCOUNT_FILE_PATH"], scope)

        return GoogleDrive(gauth)

    def upload_file(self, file_info: UploadFileInfo) -> None:
        """指定ファイルをアップロードする"""
        upload_file = self.drive.CreateFile(asdict(file_info.metadata))
        upload_file.SetContentFile(file_info.path)
        upload_file.Upload()

        print(f'{file_info.metadata.title} をアップロードしました。')
