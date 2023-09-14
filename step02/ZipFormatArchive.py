from Interfaces import List, File, FormatArchive
import zipfile
from zipfile import ZipFile
from io import BytesIO


class ZipFormatArchive(FormatArchive):
    def archive(self, files: List[File]) -> File:
        pass
