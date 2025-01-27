#Aditional task (AW12.2). Cleaning directory from all files.

# The script must be situated in catalog,
# where need remove all files!!!
# After activation the file will be deleted together with others
# files of this directory. Be careful! Make a copy of the catalog!..
import os

path = os.getcwd()
dir_list = os.listdir(path)
print("Files in '", path, "' :")
print(dir_list)
choice = input("Do you want to clear the current directory together with this file? Input 'yes' or 'no': ")
if choice == "yes":
    for i in dir_list:
        os.remove(i)
    print("The directory is cleared!")




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
