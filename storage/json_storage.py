import json

from storage.base_storage import BaseStorage


class JsonStorage(BaseStorage):
    def __init__(self, path_to_file):
        # TODO: Create file handler
        try:
            self.file = open(path_to_file)
        except FileNotFoundError:
            ...

    def read(self):
        data = json.load(self.file)
        return data

    def add_to_storage(self, instances): ...

    def save(self):
        self.file.close()
