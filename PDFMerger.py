from os import makedirs, startfile
from PyPDF2 import PdfFileMerger
from getpass import getuser
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

Tk().withdraw()
user_input = "yes"
merged_filepath_list = []

while user_input == "yes" or user_input == "y": 
    merger = PdfFileMerger()

    # instructions
    print("\nClick on the PDF files you want to merge!\n"
          "Press CTRL or SHIFT while clicking to choose multiple files.\n"
          "Files will be merged according to their original directory order.\n"
          "The merged files will be stored in a folder 'PDFMerger Files' in Desktop.\n")
    
    # select files to merge
    filepath_list = askopenfilenames(title="Select Files", filetypes=[("PDF Files", "*.pdf")])

    # exit program if no files were selected
    if not filepath_list:
        break

    # adjust for Windows filepath syntax
    filepath_list = [filepath.replace("/", "\\") for filepath in filepath_list]

    # append to PdfFileMerger
    for filepath in filepath_list:
        merger.append(open(filepath, "rb"))
    
    # create a folder for the merged files
    destfolder = f"C:\\Users\\{getuser()}\\Desktop\\PDFMerger Files"
    makedirs(destfolder, exist_ok=True)
    
    # name merged file by current date and time
    date_time = datetime.now().isoformat(" ", "seconds")
    filename = str(date_time).replace(":", "-")
    merged_filepath = destfolder + f"\\{filename}.pdf"
    
    # merge!
    with open(merged_filepath, "wb") as result:
        merger.write(result)
    
    print("Files successfully merged!\n"
          f"{merged_filepath}\n")
    
    merged_filepath_list.append(merged_filepath)
    
    user_input = input("Do you want to merge more files?\n"
                       "If so, type y or yes. If not, type n or no: ").lower()

user_input = input("\nDo you want to open all the PDF files you just merged?\n"
                   "If so, type y or yes. If not, type n or no: ").lower()

if user_input == "yes" or user_input == "y":
    for filepath in merged_filepath_list:
        startfile(filepath)