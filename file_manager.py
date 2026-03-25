# IMPORTS
from pathlib import Path
# Create my own filemanager and inherit parent class Path from pathlib library
class FileManager(Path):
    def __init__(self):
        super().__init__()
        self.absolute_path = str(Path(__file__).parent.absolute())
    # Read file
    def read_file(self, relative_path):
        full_path = self.absolute_path + "/" + relative_path
        with open(full_path, 'r') as file:
            content = file.read()
        return content
    # Read first line
    def read_first_line(self, relative_path):
        full_path = self.absolute_path + "/" + relative_path
        with open(full_path, 'r') as file:
            content = file.readlines()[0]
        return content
    # Write file
    def write_to_file(self, relative_path, new_file_name, content):
        full_path = self.absolute_path + "/" + relative_path + "/" + new_file_name
        with open(full_path, 'w') as file:
            file.write(content)
    # Append to file
    def append_to_file(self, relative_path, content):
        full_path = self.absolute_path + "/" + relative_path
        with open(full_path, 'a') as file:
            file.write(content)