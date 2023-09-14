from Interfaces import List, File, DestinationService
import os


class LocalDestinationService(DestinationService):
    def save(self, files: List[File], destination: str) -> None:
        for file in files:
            with open(os.path.join(destination, file["name"]), "wb") as f:
                f.write(file["content"])
