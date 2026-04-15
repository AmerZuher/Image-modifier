from DuplicateRemover import DuplicateRemover
from CategoryImgs import CreateFolders,StoreImgs
import shutil, os
from tkinter import Tk, filedialog
import time


print("================================================================================")

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

Breaker=True
while Breaker:
    
    print('''IN This Program u can
    0:Exit
    1:Category Imgs
    2:Delete Duplicated Imga
    3:Not  Yet    
    ''')
    
    Choice=int(input('Pls Choose One Of These Options : '))
    print("\n================================================================================")

    if Choice==0:
        print('Program Will Stop Now ')
        break

    elif Choice==1:
        
        print('\nPls Choose The Path imgs will be sorted in')
        print('  ')
        time.sleep(2)
        open_file1 = filedialog.askdirectory() # Returns opened path as str
        #PATH=r'C:\Users\amerz\Desktop\xD'
        PATH=open_file1
        
        CreateFolders(PATH)

        print("\n================================================================================")

        #Scaner=input('pls enter the path witch will arrange images : ')
        #Scaner=r'C:\Users\amerz\Desktop\ff'
        print('\nPls Choose The Path of imgs')
        print('  ')
        time.sleep(2)
        open_file2 = filedialog.askdirectory() # Returns opened path as str\
        Scaner=open_file2
        StoreImgs(Scaner)
    

    elif Choice==2:
        open_file3 = filedialog.askdirectory() # Returns opened path as str\
        dirname=open_file3
        dr = DuplicateRemover(dirname)
        dr.find_duplicates()
        dr.find_similar(dirname,70)


    else:
        print(f'there is no choice have the Number ({Choice}) ,pls try again ...')
    print("================================================================================")





