from dataclasses import asdict, dataclass, field


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
