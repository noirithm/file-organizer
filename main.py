import os
import shutil

def organize(folder_path):
    file_types = {
        "IMGS": [".jpg",".jpeg",".png",".svg",".gif"],
        "VIDS": [".mp4",".mov",".mkv",".avi"],
        "DOCS": [".pdf",".docx",".txt","xlsx",".pptx"],
        "AUDS": [".mp3",".wav",".flac"],
        "CODE": [".py",".c",".cpp",".java",".js",".css",".html"],
        "ARCS": [".zip",".tar",".gz",".rar"],
        "EXEC": [".exe",".bin",".sh",".appimage"]
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path,file)
        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                dest = os.path.join(folder_path,folder_name)
                os.makedirs(dest, exist_ok=True)
                shutil.move(file_path, os.path,join(dest,file))
                moved = True
                break

        if not moved:
            other = os.path.join(folder_name, "Other")
            os.makedirs(other,exist_ok=True)
            shutil.move(file_path,os.path.join(other,file))

folder = input("Folder path to organize: ")
organize(folder)
print("Finished")
