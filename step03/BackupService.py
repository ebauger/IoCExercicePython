# Interfaces

from Interfaces import List, File, DestinationService, FormatArchive, FileListService


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
