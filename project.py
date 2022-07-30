from distutils import extension
import os
import shutil

dict_extension = {
    'audion_extension': ('.mp3', '.m4a', '.wav', '.flac'),
    'video_extension': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'documents_extension': ('.doc', '.pdf', '.txt')
}

folderpath = input("Enter your folder path: ")


def file_finder(folder_path, file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]


# filesExtension = file_finder(folderpath, video_extension)
# print(filesExtension)
for extension_type, extension_touple in dict_extension.items():
    # print("calling file finder function")
    # print(file_finder(folderpath, extension_touple))
    folder_name = extension_type.split('_')[0]+'Files'
    folder_path = os.path.join(folderpath, folder_name)
    # print("new path to store the file : "+folder_path)
    isdir = os.path.isdir(folder_path)
    if not isdir:
        os.mkdir(folder_path)
        for item in (file_finder(folderpath, extension_touple)):
            item_path = os.path.join(folderpath, item)
            # print("item_path : "+item_path)
            item_new_path = os.path.join(folder_path, item)
            # print("item_new_path : "+item_new_path)
            shutil.move(item_path, item_new_path)
    else:
        print("Folder already exists")
