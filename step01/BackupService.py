# Keep in mind that TypedDict is available in Python 3.8 and newer.
# If you're using an older version of Python, you'll need to install
# the typing-extensions package to use TypedDict.

from typing import List, TypedDict, Protocol
from abc import abstractmethod

# Interfaces


class File(TypedDict):
    name: str
    content: bytes

# Using Protocol to define interfaces


class FileListService(Protocol):
    @abstractmethod
    def fetch_files(self) -> List[File]:
        pass


class DestinationService(Protocol):
    @abstractmethod
    def save(self, files: List[File], destination: str) -> None:
        pass


class FormatArchive(Protocol):
    @abstractmethod
    def archive(self, files: List[File]) -> File:
        pass

# Implementations


class SQLiteFileListService(FileListService):
    def fetch_files(self) -> List[File]:
        pass


class LocalDestinationService(DestinationService):
    def save(self, files: List[File], destination: str) -> None:
        pass


class ZipFormatArchive(FormatArchive):
    def archive(self, files: List[File]) -> File:
        pass

# Future Strategy Implementations


class FuturStrategyFileListService(FileListService):
    def fetch_files(self) -> List[File]:
        pass


class FuturStrategyDestinationService(DestinationService):
    def save(self, files: List[File], destination: str) -> None:
        pass


class FuturStrategyFormatArchive(FormatArchive):
    def archive(self, files: List[File]) -> File:
        pass

# Main Service


class BackupService:
    def __init__(self, file_service: FileListService, destination_service: DestinationService, format_service: FormatArchive):
        self.file_service = file_service
        self.destination_service = destination_service
        self.format_service = format_service

    def execute_backup(self, destination: str) -> None:
        files = self.file_service.fetch_files()
        archived_files = self.format_service.archive(files)
        self.destination_service.save([archived_files], destination)
