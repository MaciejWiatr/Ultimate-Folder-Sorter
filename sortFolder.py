import os
import glob
import pathlib
import shutil
from pprint import pprint
from termcolor import colored, cprint
from colorama import init


class Sorter:

    def __init__(self):
        init()
        self.path = ''
        self.header = """    ______      __    __         
   / ____/___  / /___/ /__  _____
  / /_  / __ \/ / __  / _ \/ ___/
 / __/ / /_/ / / /_/ /  __/ /    
/_/____\____/_/\__,_\\___/_/     
  / ___/____  _____/ /____  _____
  \__ \/ __ \/ ___/ __/ _ \/ ___/
 ___/ / /_/ / /  / /_/  __/ /    
/____/\____/_/   \__/\___/_/     
                                  \n-- By Maciej Wiatr --\n"""
        self.directories = {
            'Images': ['png', 'jpg', 'jpeg', 'svg', 'gif', 'bmp', 'ico', 'gvdesign'],
            'Executable': ['exe', 'msi', 'bat', 'jar', "url", 'lnk'],
            'Documents': ['mobi', 'epub', 'txt', 'pdf', 'doc', 'xlsx', 'docx', 'md', 'pptx', 'csv', 'srt', 'cbr',
                          'azw3', 'opf'],
            'Videos': ['mp4', 'avi', 'mkv'],
            'Audio': ['mp3'],
            'Coding': ['sqlite', 'py', 'js', 'war', 'npz', 'html', 'css', 'xml', 'log'],
            'Compressed': ['zip', '7z', 'rar', 'deb']
        }
        self.moved_files = {}

    def check_directory(self):
        try:
            if not os.path.exists(self.path):
                raise IOError('Path does not exist!')
        except Exception as e:
            print('Error: ', e)
            exit()

    def get_directory_name(self, name):
        return os.path.join(self.path, name)

    def create_directories(self):
        for key, _ in self.directories.items():
            dest_path = self.get_directory_name(key)
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)

    def sort_files(self):
        file_list = glob.glob(os.path.join(self.path, "*"))
        for file in file_list:
            file_extension = pathlib.Path(file).suffix.replace('.', '')
            for dest_path_name, extensions in self.directories.items():
                if file_extension in extensions:
                    if os.path.exists(os.path.join(self.get_directory_name(dest_path_name), file)):
                        shutil.move(
                            file, self.get_directory_name(dest_path_name))
                        if dest_path_name not in self.moved_files:
                            self.moved_files[dest_path_name] = [file]
                        else:
                            self.moved_files[dest_path_name].append(file)
                    else:
                        pass

    def create_summary(self):
        print("Moved files: \n")
        pprint(self.moved_files)

    def run(self):
        cprint(self.header, 'red')
        self.path = input('Enter directory path: ')
        self.check_directory()
        self.create_directories()
        self.sort_files()
        self.create_summary()


if __name__ == "__main__":
    Sort = Sorter()
    Sort.run()

# C:\Users\macie\Desktop\test_folder
