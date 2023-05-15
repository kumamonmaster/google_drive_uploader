# Google Drive アップローダー
任意のローカルフォルダ内のファイルを、任意のGoogle Driveのフォルダにアップロードするプログラム。

## 設定方法

1. 環境変数に `SERVICE_ACCOUNT_FILE_PATH` を追加して、サービスアカウントのキー情報ファイルのパスを指定する。
2. `LOCAL_FOLDER_PATH` にアップロードしたいファイルが格納されているフォルダのパスを指定する。
3. `GOOGLE_DRIVE_FOLDER_ID` にアップロード先のGoogle DriveのフォルダIDを指定する。

main.py
```py
LOCAL_FOLDER_PATH = "YOUR_LOCAL_FOLDER_PATH"
GOOGLE_DRIVE_FOLDER_ID = "YOUR_GOOGLE_DRIVE_FOLDER_ID"
```

## 開発環境
| ツール等    | バージョン |
| ----------- | ---------- |
| OS          | Windows 11 |
| Python      | 3.10.5     |
| PyDrive2    | 1.15.3     |
| google-auth | 2.18.0     |
