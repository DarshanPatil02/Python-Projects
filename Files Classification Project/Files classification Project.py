import os, shutil

# NOTE: You can write every single extensions inside tuples 
dict_extensions = {
    "audio":(".M4A",".m4a",".FLAC",".flac",".MP3",".mp3",".WAV",".wav",".WMA",".wma",".AAC",".aac"),
    "video":(".MP4",".mp4",".MOV",".mov",".WMV",".wmv",".AVI",".avi",".AVCHD",".avchd",".FLV",".flv",".F4V",".f4v",".SWF",".swf"),
    "images":(".APNG",".apng",".AVIF",".avif",".GIF",".gif",".JPEG",".jpeg",".PNG",".png",".svg",".SVG",".WebP",".JPG",".jpg"),
    "document":(".DOC",".doc",".DOCX",".docx",".HTML",".html",".HTM",".htm",".odt",".ODT",".PDF",".pdf",".xls",".XLS",".xlsx",".XLSX",".ODS",".ods",".ppt",".PPT",".pptx",".PPTX",".txt",".TXT",".py",".PY",".JAVA",".java"),
    "software":(".exe",".EXE",".MSI",".msi"),
}


folderpath = input('enter folder path : ')

def file_finder(folder_path, file_extensions):
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]

for extension_type, extension_tuple in dict_extensions.items():
    files_with_extension = file_finder(folderpath, extension_tuple)
    if files_with_extension:
        folder_name = extension_type.split('_')[0] + 'Files'
        folder_path = os.path.join(folderpath, folder_name)
        os.mkdir(folder_path)
        for item in files_with_extension:
            item_path = os.path.join(folderpath, item)
            item_new_path = os.path.join(folder_path, item)
            shutil.move(item_path, item_new_path)
