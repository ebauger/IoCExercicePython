# Keep in mind that TypedDict is available in Python 3.8 and newer.
# If you're using an older version of Python, you'll need to install
# the typing-extensions package to use TypedDict.

from typing import List, TypedDict, Protocol
from abc import abstractmethod


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
