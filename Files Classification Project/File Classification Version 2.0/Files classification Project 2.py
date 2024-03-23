import tkinter as tk
from tkinter import ttk
import os
import shutil

extension = {
    "audio":(".M4A",".m4a",".FLAC",".flac",".MP3",".mp3",".WAV",".wav",".WMA",".wma",".AAC",".aac"),
    "video":(".MP4",".mp4",".MOV",".mov",".WMV",".wmv",".AVI",".avi",".AVCHD",".avchd",".FLV",".flv",".F4V",".f4v",".SWF",".swf"),
    "images":(".APNG",".apng",".AVIF",".avif",".GIF",".gif",".JPEG",".jpeg",".PNG",".png",".svg",".SVG",".WebP",".JPG",".jpg"),
    "document":(".DOC",".doc",".DOCX",".docx",".HTML",".html",".HTM",".htm",".odt",".ODT",".PDF",".pdf",".xls",".XLS",".xlsx",".XLSX",".ODS",".ods",".ppt",".PPT",".pptx",".PPTX",".txt",".TXT",".py",".PY",".JAVA",".java"),
    "software":(".exe",".EXE",".MSI",".msi")
}

def file_modifier(extension):
    for item in os.listdir():
        for k,v in extension.items():
            for i in v:
                if item.endswith(i):
                    check = os.path.exists(f"{k}_files")
                    if check == True:
                        shutil.move(item,f"{k}_files")
                    elif check == False:
                        os.mkdir(f"{k}_files")
                        shutil.move(item,f"{k}_files")
    
extension = {
    "Word":(".DOC",".doc",".DOCX",".docx",),
    'html': (".HTML",".html",".HTM",".htm"),
    'PDF' : (".PDF",".pdf"),
    'Excel':(".xls",".XLS",".xlsx",".XLSX"),
    'Other':(".ODS",".ods",".py",".PY",".JAVA",".java",".odt",".ODT"),
    'PPT':(".ppt",".PPT",".pptx",".PPTX"),
    'text':(".txt",".TXT"),
    
}

def file_modifier(extension):
    for item in os.listdir():
        for k,v in extension.items():
            for i in v:
                if item.endswith(i):
                    check = os.path.exists(f"{k}_files")
                    if check == True:
                        shutil.move(item,f"{k}_files")
                    elif check == False:
                        os.mkdir(f"{k}_files")
                        shutil.move(item,f"{k}_files")






# creating window
win = tk.Tk()
# adding title
win.title("File modifier")
# creating label
main_label = ttk.Label(win, text="Enter your path where you want to sort files: ")
main_label.grid(row=0, column=0, sticky=tk.W)
# creating entrybox
path_var = tk.StringVar()
path = ttk.Entry(win, width=14, textvariable=path_var)
path.grid(row=0, column=1)
# creating button
def action():
    try:
        os.chdir(path_var.get())
    except:
        pass
    else:
        file_modifier(extension)
        
submit = ttk.Button(win, text="Submit", command=action)
submit.grid(row=1, column=0)
win.mainloop()
