
import re # to run run regular expresion RegEx operation

import os # for Operating system manegement
import glob

coolFact = "how are you Mr Python!"

found = re. search("how*", coolFact )

if found:
    print("Oh!, this match")
else:
    print("No lick finding it. :(")


# A few RegEx function, metachareters and speial sequences

##findall function
rhyme = "The rain in Spain fall mainly in the plain"
matches= re.findall(r'ain', rhyme)
print(matches)

##sub() function

text = "soda cans can  be found in Canada"
result =  re.sub(r"can", "123",text) 
# search for 'can' and replace with 123 in the varable text
#output is -->> soda 123s 123  be found in Canad
print(result)

#split function
fruits = "apple: banana! cherry; date"

ress = re.split("[!;:]",fruits)
# split() will search for the characters "!",";",":"  removes them from ress
# The will be ['apple', ' banana', ' cherry', ' date']
print(ress)
ress2 = re.split("[!;:\s]",fruits); print(ress2)


grettings = "Hello, Brothers! How are you"
lookup = re.search("\s\w+", grettings)
 #search for white space(\s) immediately follow by a letter(\w)
if lookup:
    print("Whitesapce found in :", lookup.group())
else:
    print("found no match, sorry ")  #????????ASK QUESTIONS ABOUT THIS


"""OS (Operating System) Module"""

#File and directories management

#import os
print(os.getcwd())  # cwd reffers to current working directory 
print(os.listdir())  # listdir will listt all the file/folder in the working directory
#print(os.mkdir("FolderMoise"))  # create a folder
#os.mkdir("yetAnotherfolder")
#os.rename("yetAnotherfolder", "yetAnotherfolder2")   #remane folder
#os.rmdir("yetAnotherFolder2") #remove the file
print(os.path.isdir("FolderMoise"))
print(os.path.isfile("courses.py"))


## System Commands and Process managememt
print(os.name) # returns the operating system name. NT is New Technology which reffer to Windowns

##Glob Module
#import glob   as gl

py_files = glob.glob("*.py")
print("Here is are the python file(s) in this location", py_files)

#iglob (works like glob but with better memory efficiency especially for iteration
for file in glob.glob("*.txt"):
    print("hey, I located the 'txt' file name", file)

#combination of functionality

all_doc_files = glob.glob("*.docx")
for  File in all_doc_files:
    os.remove(File)
    print(f"{File} deleted successfully")

