import os
import errno
from pathlib import Path
from shutil import move


class Organizer:
    def __init__(self):
        self.list_of_directories = {
            "Picture_Folder": [".jpeg", ".jpg", ".ico", ".gif", ".png", ".svg", ".heic"],
            "Video_Folder": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv", ".m3u8", ".webm", ".ts"],
            "Zip_Folder": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
            "Music_Folder": [".mp3", ".msv", ".wav", ".wma"],
            "PDF_Folder": [".pdf"],
            "SQL_Folder": [".sql"],
            "Programs_Folder": [".exe", ".msi"],
            "Spreadsheet_Folder": [".xlsx", ".csv"],
            "Word_Folder": [".docx", ".doc", ".txt"],
            "Python_Folder": [".ipynb", ".py"],
            "PPT_Folder": [".pptx", ".ppt"],
            "Json_Folder": [".json"],
            "Web_Folder": [".html", ".xml", ".xhtml", ".css", ".js"],
            "3D_Printer_folder": [".stl", ".gcode"]
        }

        self.file_format_dictionary = {
            final_file_format: directory
            for directory, file_format_stored in self.list_of_directories.items()
            for final_file_format in file_format_stored
        }

    def organizer(self, src):
        try:
            with os.scandir(src) as Downloads:
                os.chdir(src)
                for entry in Downloads:
                    os.scandir().close()
                    if not entry.name.startswith('.') and entry.is_file():
                        file_path = Path(entry)
                        final_file_format = file_path.suffix.lower()
                        if final_file_format in self.file_format_dictionary:
                            destination_path = os.path.join(os.getcwd(), self.file_format_dictionary[final_file_format])
                            if os.path.exists(self.file_format_dictionary[final_file_format]):
                                move(src=str(file_path), dst=destination_path)
                            else:
                                os.makedirs(destination_path)
                                move(src=str(file_path), dst=destination_path)
        except IOError as err:
            if err.errno == errno.ENOENT:
                print(err)
            elif err.errno == errno.EBADF:
                print(err)

