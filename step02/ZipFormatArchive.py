from Interfaces import List, File, FormatArchive
import zipfile
from zipfile import ZipFile
from io import BytesIO


class ZipFormatArchive(FormatArchive):
    def archive(self, files: List[File]) -> File:
        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, "a", compression=zipfile.ZIP_DEFLATED) as zf:
            for file in files:
                zf.writestr(file["name"], file["content"])

        zip_filename = "archive.zip"
        zip_content = zip_buffer.getvalue()
        return {"name": zip_filename, "content": zip_content}
