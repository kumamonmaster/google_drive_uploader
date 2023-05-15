from dataclasses import asdict, dataclass, field
import glob
import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials


SERVICE_ACCOUNT_PATH = "service_account.json"
LOCAL_FOLDER_PATH = r"C:\Users\kuma\Downloads\test"
GOOGLE_DRIVE_FOLDER_ID = "1gakGiYh_x6G34k_D9CgvBtKTl01B2Nt2"


@dataclass
class Parents:
    id: str = field(init=False)

    def __post_init__(self):
        self.id = GOOGLE_DRIVE_FOLDER_ID


@dataclass(frozen=True)
class MetaData:
    title: str
    parents: list[Parents]


@dataclass
class UploadFileInfo:
    path: str
    metadata: MetaData


def create_google_drive() -> GoogleDrive:
    """Google Driveインスタンスの生成"""
    gauth = GoogleAuth()
    scope = ["https://www.googleapis.com/auth/drive"]
    gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_PATH, scope)

    return GoogleDrive(gauth)


def get_upload_files() -> list[UploadFileInfo]:
    """アップロード対象のファイル情報を取得する"""
    upload_files = []

    if not os.path.isdir(LOCAL_FOLDER_PATH):
        raise FileNotFoundError(f"アップロード対象のローカルディレクトリが存在しません。LOCAL_FOLDER_PATH: {LOCAL_FOLDER_PATH}")

    files = glob.glob(f"{LOCAL_FOLDER_PATH}\*.csv")
    if not files:
        raise FileNotFoundError(f"アップロード対象ディレクトリ内のファイルが0件でした。LOCAL_FOLDER_PATH: {LOCAL_FOLDER_PATH}")

    for file in files:
        upload_files.append(UploadFileInfo(file, MetaData(os.path.basename(file), [Parents()])))

    return upload_files


def upload_to_google_drive(file_info: UploadFileInfo) -> None:
    """指定ファイルをGoogle Driveにアップロードする"""
    upload_file = drive.CreateFile(asdict(file_info.metadata))
    upload_file.SetContentFile(file_info.path)
    upload_file.Upload()

    print(f'{file_info.metadata.title} をアップロードしました。')


if __name__ == '__main__':
    try:
        drive = create_google_drive()
        upload_files = get_upload_files()
        for upload_file in upload_files:
            upload_to_google_drive(upload_file)

    except Exception as e:
        print(e)
