# Secure File Deletion using shutil
import shutil
import os

# Class For securely removing file 

class FileDeletion:

    # Constructor 
    def __init__(self, file_path):
        self.file_path = file_path

    # Check File Existence 
    def check_file(self):
        if os.path.exists(file_path):
            return True
        else:
            print(f"File {file_path} not exist")
            return False
    
    def secure_file(self):
        if self.check_file() is True:
            # Open file in write mode
            with open(file_path,"wb") as file:

                # Overwriting the content of the file
                file.write(os.urandom(os.path.getsize(file_path)))
                print("Overwrite the content of file sucessfully....")

            # Delete file
            shutil.rmtree(file_path)
            print("File Deleted Successfully....")
        
        else:
            print("Try again")

# Input Path 
file_path = input("Enter the file path : ")
secure_del = FileDeletion(file_path)
secure_del.check_file()
secure_del.secure_file()