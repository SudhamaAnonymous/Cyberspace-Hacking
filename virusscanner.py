from tkinter import Tk
from tkinter.filedialog import askopenfilename

def file_open():
    Tk().withdraw()
    file_path=askopenfilename()
    scan_file(file_path)
def scan_file(file_path):
    with open(file_path,"rb") as f:
        file_content=f.read()
        virus_signature=rb"jashahshlaagsgas@jkdhsdhsdhsdsjdsadasdjasdjasdj12242885"
        if virus_signature in file_content:
            print("virus found in file",file_path)
        else:
            print("virus not found")
file_open()
