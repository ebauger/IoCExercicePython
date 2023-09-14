from SQLiteFileListService import SQLiteFileListService
from LocalDestinationService import LocalDestinationService
from ZipFormatArchive import ZipFormatArchive
from BackupService import BackupService


def main():
    # Step 1: Set up the services
    file_service = SQLiteFileListService()
    destination_service = LocalDestinationService()
    format_service = ZipFormatArchive()

    # Step 2: Instantiate the BackupService
    backup_service = BackupService(
        file_service, destination_service, format_service)

    # Step 3: Execute the backup
    # For this example, we're saving the backup to a directory named "backups"
    # Ensure this directory exists or adjust the path as needed
    backup_service.execute_backup("backups")


if __name__ == "__main__":
    main()
