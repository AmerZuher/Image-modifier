from PIL import Image
import imagehash
import os
import numpy as np
import  time
from contextlib import suppress


class DuplicateRemover:
    def __init__(self,dirname,hash_size = 8):
        self.dirname = dirname
        self.hash_size = hash_size
        
    #Find and Delete Duplicates
    def find_duplicates(self):
        
        fnames = os.listdir(self.dirname)
        hashes = {}
        duplicates = []
        print("Finding Duplicates Now!\n")
        #search  for Dupli imgs 
        for image in fnames:
            with suppress(Exception):
                with Image.open(os.path.join(self.dirname,image)) as img:
                    temp_hash = imagehash.average_hash(img, self.hash_size)
                    if temp_hash in hashes:
                        print("Duplicate {} \nfound for Image {}!\n".format(image,hashes[temp_hash]))
                        duplicates.append(image)
                    else:
                        hashes[temp_hash] = image
                
                #to choose the biggest img as a primary img
                counter=0
                primary=duplicate[0]
                index=0
                for dupli in duplicate:
                    if dupli>primary:
                        dupli=primary
                        indix=counter

                    else:
                        continue    
                    
                    counter+=1
                    temp=duplicate[0]
                    duplicate[0]=primary
                    duplicate[index]=temp

                
        #Del Dupli imgs 
        if len(duplicates) != 0:
            a = input("Do you want to delete these {} Images? Press Y or N:  ".format(len(duplicates)))
            space_saved = 0
            if(a.strip().lower() == "y"):
                for duplicate in duplicates:
                    space_saved += os.path.getsize(os.path.join(self.dirname,duplicate))
                    
                    os.remove(os.path.join(self.dirname,duplicate))
                    print("{} Deleted Succesfully!".format(duplicate))
    
                print("\n\nYou saved {} mb of Space!".format(round(space_saved/1000000),2))
                time.sleep(2)

            else:
                print("Thank you for Using Duplicate Remover")
                time.sleep(2)

        else:
            print("No Duplicates Found :(")
            time.sleep(2)
            
        
            
    #find similar imgs         
    def find_similar(self,location,similarity=80):
        fnames = os.listdir(self.dirname)
        threshold = 1 - similarity/100
        diff_limit = int(threshold*(self.hash_size**2))
        
        with Image.open(location) as img:
            hash1 = imagehash.average_hash(img, self.hash_size).hash
        
        print("Finding Similar Images to {} Now!\n".format(location))
        for image in fnames:
            with Image.open(os.path.join(self.dirname,image)) as img:
                hash2 = imagehash.average_hash(img, self.hash_size).hash
                
                if np.count_nonzero(hash1 != hash2) <= diff_limit:
                    print("{} image found {}% similar to {}".format(image,similarity,location))

                    
                    
                    
                
        
            