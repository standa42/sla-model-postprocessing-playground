from email.errors import NonPrintableDefect
from os import listdir
from os.path import isfile, join


class FileManager:
    def __init__(self):
        self.path = "./sl1_files/"
        self.currently_located_files = []
        self.currently_selected_file = None 

    def refresh(self):
        # get all .sl1 files
        self.currently_located_files = [f for f in listdir(self.path) if isfile(join(self.path, f))] 
        self.currently_located_files = list(filter(lambda file_path: ".sl1" in file_path, self.currently_located_files))
        self.currently_located_files = list(map(lambda f: join(self.path, f), self.currently_located_files))

    def get_files(self):
        return self.currently_located_files

    def get_file_count(self):
        return len(self.currently_located_files)