from secrets import choice
import shutil, os
from PIL import Image
import glob
from contextlib import suppress
from tkinter import Tk, filedialog
import time


#Create Folders to put the imgs in ,if the folderis alreasy exists then the folder is Directory
def CreateFolders(PATH):

    for Folder in Folders:
    #Test if a path is a directory
        path = os.path.join(PATH,Folder)
        if os.path.exists(path):
            print(path + ' : exists')
            if os.path.isdir(path):
                print(path + ' : is a directory')
                print(" ")


        #Create a directory
        dir = os.path.join(PATH,Folder)
        if not os.path.exists(dir):
            os.mkdir(dir)
            print('Folder |"{}"| Has Been created successfuly'.format(Folder))

#append 2 folders witch images will be sorted in as a list
        newpath = os.path.join(PATH,Folder)
        newpaths.append(newpath)

#for scan all items in the folder and it's type
def StoreImgs(Scaner):
    counter=0
    for img in glob.iglob(os.path.join(Scaner,'*.*')):
        #to  print file's Name not file's path
        file_name = os.path.basename(img)
        #to ignor all unwanted data type
        with suppress(Exception):

            image = Image.open(img)
            width = image.width
            height = image.height
            if width>=height:
                shutil.copy(img, newpaths[0])
                print('\n |"{}"| === MOVED TO => |"{}"| Successfully!"'.format(file_name, Folder1))

            else:
                shutil.copy(img, newpaths[1])
                print('\n |"{}"| === MOVED TO => |"{}"| Successfully!"'.format(file_name, Folder2))

            counter+=1

    print('\n[',counter,'] Operations have done\n')
    time.sleep(5)

Folder1='Desktop imgs'
Folder2='Mobile imgs'
Folders=[Folder1,Folder2]
newpaths=[]