#Aditional task (AW12.2). Cleaning directory from some files.

# The script must be situated in catalog, where need remove some files!!!

import os

path = os.getcwd()
dir_list = os.listdir(path)
print("Files in '", path, "' :")
print(dir_list)
choice_1 = input("Do you want to clear the current directory from some file? Input 'yes - 1' or 'no - 0': ")
if choice_1 == "1":
    choice_2 = int(input("Select the deletion option: 1 - at the beginning of the file name; 2 - at the ends of the file name: "))
    if choice_2 == 1:
        name_start = input("Enter the beginning of the file name: ")
        print("Removal... : ")
        for i in dir_list:
            if i.startswith(name_start):
                os.remove(i)
    else:
        name_ends = input("Enter the ends of the file: ")
        print("Removal... : ")
        for i in dir_list:
            if i.endswith(name_ends):
                os.remove(i)
print("Verification output of left files in the directory: ")
dir_list = os.listdir(path)
print(dir_list)



# ########################################################################################
# # 1. Getting the path to the script file
# #v1:
# # import sys
# # script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
# # print(script_directory)
# #v2:
# # print("File location using os.getcwd():", os.getcwd())
# address = (os.getcwd())                               #Formation of a variable with an address
# # address = address.replace(chr(92), chr(47))
# # print(address)
#
# #########################################################################################
# # 2. Getting a list of files in a directory and deleting them:
# # Get the list of all files and directories
# path = address
# dir_list = os.listdir(path)
# print("Files and directories in '", path, "' :")
# # prints all files
# print(dir_list)
# #for i in dir_list:       #Enable when there is a copy of the file and directory!!! Attension!
#     # os.remove(i)
# ##########################################################################################################
# ##########################################################################################################
