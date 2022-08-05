import os
import glob

# Parent directory
parent_dir = ".\\__fixtures__\\"

# Remove Directories
files = glob.glob(f"{parent_dir}*")
for f in files:
    isDirectory = os.path.isdir(f)
    if isDirectory:
        os.rmdir(f)
    else:
        os.remove(f)

# Create Test Dir
directory = "The Simpsons"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

# Create Test Media
media = "A Streetcar Named Marge.mp4"
mediaPath = os.path.join(parent_dir, media)
f = open(mediaPath, "x")