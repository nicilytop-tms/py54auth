import json

from storage.base_storage import BaseStorage


class JsonStorage(BaseStorage):
    def __init__(self, path_to_file):
        try:
            self.__path_to_file = path_to_file
            self.file = open(self.__path_to_file)
        except FileNotFoundError:
            self.file = open(self.__path_to_file, "w")
            self.file.write("[]")
            self.file.close()
            self.file = open(self.__path_to_file)

    def read(self):
        data = json.load(self.file)
        return data

    def add_to_storage(self, instances):
        data = self.read()
        data.extend(instances)
        self.file.close()
        self.file = open(self.__path_to_file, "w")
        json.dump(data, self.file)
        self.save()
        self.file = open(self.__path_to_file)

    def save(self):
        self.file.close()
