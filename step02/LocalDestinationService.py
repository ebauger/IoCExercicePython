from Interfaces import List, File, DestinationService
import os


class LocalDestinationService(DestinationService):
    def save(self, files: List[File], destination: str) -> None:
        pass
