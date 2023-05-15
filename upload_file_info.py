from dataclasses import dataclass


@dataclass(frozen=True)
class Parents:
    id: str


@dataclass(frozen=True)
class MetaData:
    title: str
    parents: list[Parents]


@dataclass(frozen=True)
class UploadFileInfo:
    path: str
    metadata: MetaData
