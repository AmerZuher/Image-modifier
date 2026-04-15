from DuplicateRemover import DuplicateRemover

dirname = r"C:\Users\amerz\Desktop\dd"


# Remove Duplicates
dr = DuplicateRemover(dirname)
dr.find_duplicates()

# Find Similar Images
dr.find_similar(r"C:\Users\amerz\Desktop\dd",70)