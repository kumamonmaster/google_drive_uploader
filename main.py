import glob
import os

import send2trash

from google_drive_client import GoogleDriveClient
from upload_file_info import UploadFileInfo, MetaData, Parents


LOCAL_FOLDER_PATH = r"C:\Users\kuma\Downloads\test"
GOOGLE_DRIVE_FOLDER_ID = "1gakGiYh_x6G34k_D9CgvBtKTl01B2Nt2"


def get_upload_files() -> list[UploadFileInfo]:
    """アップロード対象のファイル情報を取得する"""
    upload_files = []

    if not os.path.isdir(LOCAL_FOLDER_PATH):
        raise FileNotFoundError(f"アップロード対象のローカルディレクトリが存在しません。LOCAL_FOLDER_PATH: {LOCAL_FOLDER_PATH}")

    files = glob.glob(os.path.join(LOCAL_FOLDER_PATH, "*.csv"))
    if not files:
        raise FileNotFoundError(f"アップロード対象ディレクトリ内のファイルが0件でした。LOCAL_FOLDER_PATH: {LOCAL_FOLDER_PATH}")

    for file in files:
        upload_files.append(UploadFileInfo(file, MetaData(os.path.basename(file), [Parents(GOOGLE_DRIVE_FOLDER_ID)])))

    return upload_files


google_drive = GoogleDriveClient()

try:
    print("指定のGoogleDriveフォルダ内のファイルを削除します")
    google_drive.delete_file(GOOGLE_DRIVE_FOLDER_ID)
    print("削除完了")

    # GoogleDriveにアップロードするロカールファイルの一覧を取得する
    upload_files = get_upload_files()

    print("指定のローカルフォルダ内のファイルをGoogleDriveにアップロードします")
    for upload_file in upload_files:
        google_drive.upload_file(upload_file)
        send2trash.send2trash(upload_file.path)
    print("アップロード完了")

except FileNotFoundError as e:
    print(e)
