# Program to clear the clutter inside a folder on computer. 
# Should us os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in the folder. Do the same for other file formats.
# dafdf.png -->1.png
# dafdf.png -->2.png
# dafdf.png -->3.png
# dafdf.png -->4.png


import os

files = os.listdir('clutterFolder')
print(files)
i =1
for f in files:
    if f.endswith('.png'): #and (f != f"{i}.png"):
        print(f)
        os.rename(f"clutterFolder/{f}", f"clutterFolder/{i}.png")
        i+=1