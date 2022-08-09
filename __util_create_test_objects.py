import os
import glob
from pathlib import Path

def delete(parent_dir):
    files = glob.glob(f"{parent_dir}*")
    for f in files:
        isDirectory = os.path.isdir(f)
        if isDirectory:
            os.rmdir(f)
        else:
            os.remove(f)

# Parent directory
parent_dir = ".\\__fixtures__\\"

# Remove Directories
delete(parent_dir)



# Create Test Dir
series_directory_name = "The Simpsons"
series_path = os.path.join(parent_dir, series_directory_name)
print(series_path)
os.mkdir(series_path)

# Create Test Dir
season_directory_04 = "Season 04"
path = os.path.join(series_path, season_directory_04)
os.mkdir(path)

# Create Test Dir
season_directory_05 = "The Simpsons - Season 5"
path = os.path.join(series_path, season_directory_05)
os.mkdir(path)

media_file_name_5 = "The Simpsons [5x01] Homer's Barbershop Quartet.avi"
media_path = os.path.join(series_path, season_directory_05, media_file_name_5)
f = open(media_path, "x")

# Create Test Dir
season_directory_01 = "Simpson 1"
path = os.path.join(series_path, season_directory_01)
os.mkdir(path)

# Create Test Media
media_file_name = "A Streetcar Named Marge.mp4"
media_path = os.path.join(series_path, season_directory_04, media_file_name)
f = open(media_path, "x")
