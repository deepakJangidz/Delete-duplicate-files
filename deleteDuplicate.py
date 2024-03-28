# from tkinter import Tk
# from tkinter.filedialog import askdirectory

# import os , hashlib
# from pathlib import Path

# Tk.withdraw()
# path = askdirectory(title= "select a folder")

# file_list = os.listdir(path)
# # print(path)
# unique = dict()

# for file in file_list:
#     file_name = Path(os.path.join(path  , file))

#     if file_name.isfile():
#         fileHash = hashlib.md5(open(file_name , 'rb').read()).hexdigest()

#         if fileHash not in unique:
#             unique[fileHash] = file_name

#         else:
#             os.remove(file_name)
#             # print(f"Successfully deleted {file_name}")
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib
from pathlib import Path

root = Tk()  # Create an instance of the Tk class
root.withdraw()  # Call the withdraw() method on the instance

path = askdirectory(title="Select a folder")

file_list = os.listdir(path)

# print(path)

unique = dict()

for file in file_list:
    file_name = Path(os.path.join(path, file))

    if file_name.is_file():
        file_hash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()

        if file_hash not in unique:
            unique[file_hash] = file_name
        else:
            os.remove(file_name)
            print(f"Successfully deleted {file_name}")

root.mainloop()  # Start the Tkinter event loop