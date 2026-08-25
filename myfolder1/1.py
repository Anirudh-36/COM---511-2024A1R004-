print("Hello world")
vol = 212
print(f"volume of cyclinder is {vol}")

# This is a single comment
"""
This is a multiline
string.
It can be used as a comment
when it is not assigned to anything.

"""
# Q1. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
# import os
# contents = os.listdir(".")

# for item in contents:
#     print(item)

# Gives files in directory
import os
files = os.listdir()
print(files)

# current working directory
import os
print(os.getcwd())


# creates new folder
# import os
# os.mkdir("myfolder")


# It checks whether another folder exists
import os
print(os.path.exists("myfolder2"))


# Rename the folder
# import os
# print(os.rename("myfolder","myfolder2"))


# os.path.isfile() is used to check whether something is a file.
import os
print(os.path.isfile("2.py"))

# os.path.isdir() is used to check whether something is a directory.
import os
print(os.path.isdir("myfolder2"))

# write a program to remove the file
# import os
# print(os.remove("2.py"))


# write a program to remove the directory
# import os
# os.rmdir("myfolder3")