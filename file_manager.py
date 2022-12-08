
from tkinter import *
import os
import shutil
from tkinter import messagebox
from tkinter import filedialog
from app_file_manager import *

def open_file():
    files= filedialog.askopenfilename(
        title= "Please, select file to open:", filetypes=[("all", "*.*")]

    )
    os.startfile(os.path.abspath(files))
#after call of function open_file there is method askopenfilename, after that with using of os modules we are open selected file

def copy_file():
    copy= filedialog.askopenfilename(
        title= "Please, copy the file: ", filetypes= [("All files", "*.*")]
    )
    copy_to_paste= filedialog.askdirectory(title=("Where are you going to paste file?"))
    try:
        shutil.copy(copy, copy_to_paste)
        messagebox.showinfo(title="It is done", message="Files have been copied")
    except:
        messagebox.showwarning(title="Not good!", message="Try again!!")
#for the first we are using function askopenfilename to choose for the file, askdirectory method is pasting our files to wherever we wan

def delete_file():
    file= filedialog.askopenfilename(
        title= "Please choose a file: ", filetypes= [("All files", "*.*")]
    )   
    os.remove(os.path.abspath(file))
    messagebox.showinfo(title= "File deleted!")


def showpath():
    files= filedialog.askopenfilename(title= "Select the file: ", filetypes= [("All files", "*.*")])
    return files



if __name__=="__main__":
    root= Tk()
    root.title("File manager, simple..")
    root.configure(bg= "skyblue")

    header= Frame(root, bg="red")
    button= Frame(root, bg="yellow")

    header.pack(fill="both")
    button.pack(expand=True, fill="both")
    
    header_label= Label(header, text="File manager")
    header_label.pack(expand= True, fill= "both")

    #open button
    open_button= Button(
        button, text= "Open a file: ", bg= "red", command= open_file
    )
    copy_button= Button(
        button, text= "Copy a file: ", bg= "red", command= copy_file
    )
    delete_button= Button(
        button, text= "Delete a file", bg= "red", command= delete_file
    )
    #rename_button= Button(
    #    button, text= "Rename the file", bg= "red", command= renamefile
    #)
    show_button= Button(
        button, text= "Show the way: ", command= showpath
    )
    files= StringVar()

    open_button.pack(pady= 9)
    copy_button.pack(pady= 9)
    delete_button.pack(pady= 9)
    #rename_button.pack(pady= 9)
    show_button.pack(pady= 9)
    root.mainloop()



