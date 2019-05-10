from os import makedirs, startfile
from PyPDF2 import PdfFileMerger
from getpass import getuser
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

Tk().withdraw()
userinput = "yes"
mergedfilepaths = []

while userinput == "yes" or userinput == "y": 
    merger = PdfFileMerger()
    
    print("Click on the PDF files you want to merge!\n"
          "Prest CTRL or SHIFT while clicking to choose multiple files.\n"
          "Files will be merged according to their directory order.\n"
          "The merged files will be stored in a folder 'PDFMerger Files' in Desktop.\n")
    
    filepaths = askopenfilenames(title = "Select Files", filetypes = [("PDF Files", "*.pdf")])
    filepaths = [filepath.replace("/", "\\") for filepath in filepaths]
    for filepath in filepaths:
        merger.append(open(filepath, "rb"))
        
    destfolder = f"C:\\Users\\{getuser()}\\Desktop\\PDFMerger Files"
    makedirs(destfolder, exist_ok = True)
    
    dateandtime = datetime.now().isoformat(" ", "seconds")
    filename = str(dateandtime).replace(":", ".")
    
    mergedfilepath = destfolder + f"\\{filename}.pdf"
    with open(mergedfilepath, "wb") as result:
        merger.write(result)
        
    print("Files successfully merged!\n"
          f"{mergedfilepath}\n")
    
    mergedfilepaths.append(mergedfilepath)
    
    userinput = input("Do you want to merge more files?\n"
                      "If so, type y or yes. If not, type n or no: ").lower()
    print("\n")

userinput = input("Do you want to open all the PDF files you just merged?\n"
                  "If so, type y or yes. If not, type n or no: ").lower()
if userinput == "yes" or userinput == "y":
    for filepath in mergedfilepaths:
        startfile(filepath)
    
