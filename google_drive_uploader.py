import glob
import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials


SERVICE_ACCOUNT_PATH = "YOUR_SERCICE_ACCOUNT_JSON_FILE_PATH"
LOCAL_FOLDER_PATH = "YOUR_LOCAL_FOLDER_PATH"
GOOGLE_DRIVE_FOLDER_ID = "YOUR_GOOGLE_DRIVE_FOLDER_ID"


def create_google_drive() -> GoogleDrive:
    """Google Driveインスタンスの生成"""
    # Google Drive APIに認証する
    gauth = GoogleAuth()
    scope = ["https://www.googleapis.com/auth/drive"]
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_PATH, scope)

    return GoogleDrive(gauth)


def upload_to_google_drive(file_path: str) -> None:
    """指定ファイルをGoogle Driveにアップロードする"""
    upload_file = drive.CreateFile({"title": os.path.basename(file_path), 'parents': [{'id': GOOGLE_DRIVE_FOLDER_ID}]})
    upload_file.SetContentFile(file_path)
    upload_file.Upload()

    print(f'{file_path}のアップロードが完了しました。')


drive = create_google_drive()
files = glob.glob(f"{LOCAL_FOLDER_PATH}\*.csv")
for file in files:
    upload_to_google_drive(file)
