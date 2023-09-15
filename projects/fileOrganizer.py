import os
import subprocess
usr = os.getenv("USER")
rootfile = f"/home/{usr}/"

rootFolderDirectory = {
    "Documents",
    "Music",
    "Downloads",
    "Pictures",
    "Videos"
}


File_format = {
    "Documents": ["zip", "tar", "xy", "iso", "txt", "deb", "AppImage", "woff2"],
    "Pictures": ["jpeg", "png", "svg", "wemp", "jpg"],
    "Videos": ["mp4", "mkv", "mov", "gif"],
    "Music": ["mp3"]
}
filtered_folders = ["Music", "Videos", "Pictures"]
folder_name = {
    "zip": ["zip", "tar", "xy", "iso", "deb", "AppImage"],
    "font": ["woff2"],
    "txt": ["docx", "odt", "rtf", "txt", "log"],
    "gfc_img": ["png", "svg", "wemp"],
    "books": ["pdf"]
}


def file_organiser():
    for rootDir in rootFolderDirectory:
        main_directory = f'{rootfile}{rootDir}/'
        for files in os.listdir(main_directory):
            [file_name, *fileFormat] = files.split(".")
            for directory in File_format:
                for items in File_format[directory]:
                    if items in fileFormat and os.path.isdir(main_directory + files) is False:
                        command = ["mv", main_directory +
                                   files, rootfile+directory]
                        subprocess.Popen(
                            command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
                    elif rootDir in filtered_folders and os.path.isdir(main_directory + files):
                        pass
                    elif rootDir not in filtered_folders and os.path.isdir(main_directory + files):

                        command = ["mv", main_directory +
                                   files, rootfile+"Documents"]
                        subprocess.Popen(
                            command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)


def file_sorter():
    for rootDir in rootFolderDirectory:
        main_directory = f'{rootfile}{rootDir}/'
        for files in os.listdir(main_directory):
            [file_name, *fileFormat] = files.split(".")
            for folder in folder_name:
                for items in folder_name[folder]:
                    if items in fileFormat:
                        try:
                            os.mkdir(main_directory+folder)
                            command = ["mv", main_directory +
                                       files, main_directory+folder]
                            subprocess.Popen(
                                command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
                        except FileExistsError:
                            command = ["mv", main_directory +
                                       files, main_directory+folder]
                            subprocess.Popen(
                                command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)


def Organise():
    file_organiser()
    file_sorter()
    file_organiser()


Organise()
