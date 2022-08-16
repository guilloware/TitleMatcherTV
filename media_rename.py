import os
from re import X
import sys
import api
from domain.title import EpisodeTitle, SeriesTitle
import helpers.string_helpers as string_helpers
from pathlib import Path

def promptContinue(): 
	passed = False
	while passed != True:
		choice = input("Continue With Changes? [y,n]\n")
		if(choice == "y"):
			passed=True
		elif(choice == "n"):
			os._exit()
		else:
			print("Enter [y] or [n]")

def renameEpisode(fileName, pathDir, query):
    print(f"-- Processing [{fileName}]")

    extension = string_helpers.getFileExtension(fileName)
    text = string_helpers.removeFileExtension(fileName)
    print(text)
    api_result = api.searchEpisode(text, query)

    results = api_result

    for t in results:
        title = EpisodeTitle(t['id'], t['title'], t['description'], fileName, extension)
        print('-- Found Match --')
        print(f"-> {fileName}")
        print(f"-> {title.plex_title}")

        choice = input("Rename? [y,n]\n")

        if(choice == "y"):
            oldPath = os.path.join(pathDir, fileName)
            newPath = os.path.join(pathDir, title.plex_title)
            os.rename(oldPath, newPath)
            print(f"--Renamed--\n-> {oldPath}\n-> {newPath}")
            os._exit(1)
        elif(choice == "n"):
            print("...")
        else:
            print("Enter [y] or [n]")

def renameSeries(fileName, pathDir, query):
    searchText = os.path.basename(os.path.dirname(fileName))
    print(f"-- Processing [{fileName}]")
    api_result = api.searchSeries(searchText, query)
    results = api_result

    for t in results:
        print(t)
        title = SeriesTitle(t['id'], t['title'], t['description'])
        print('-- Found Match --')
        print(f"-> {searchText}")
        print(f"-> {title.plex_title}")

        choice = input("Rename? [y,n]\n")

        if(choice == "y"):
            oldPath = os.path.join(pathDir, searchText)
            newPath = os.path.join(pathDir, title.plex_title)
            os.rename(oldPath, newPath)
            print(f"--Renamed--\n-> {oldPath}\n-> {newPath}")
            os._exit(1)
        elif(choice == "n"):
            print("...")
        else:
            print("Enter [y] or [n]")

def renameSeasonFolders(folderDir, parentPath):
    os.walk(folderDir)
    dir = [x[0] for x in os.walk(folderDir)]

    for folder in dir[1:]:
        if string_helpers.hasNumber(folder):
            folderName = Path(folder)
            baseFolderName = os.path.basename(Path(folderName))
            newFolderName = string_helpers.getSeasonNumber(baseFolderName)
            oldPath = os.path.join(folderName)
            newPath = os.path.join(parentPath, newFolderName)
            print(f"--WHAT I GOT--\n-> {oldPath}\n-> {newPath}")

            if oldPath == newPath:
                print("--Folder Name Already Valid--")
            else:
                os.rename(oldPath, newPath)
                print(f"--Renamed--\n-> {oldPath}\n-> {newPath}")
        else:
            print("No season folders found skipping...")
    os._exit(1)

type = sys.argv[1]
fileName = sys.argv[2]
query = sys.argv[3] if len(sys.argv) > 3 else None

if os.path.exists(fileName) != True:
	print("Path not valid")
	os._exit(1)

path = Path(fileName)
pathDir = path.parent.absolute()

if type != "episode" and type != "series" and type != "season":
	print("Please enter arg to as episode or series")
	os._exit(1)

if type == "episode":
    mediaName = os.path.basename(path)
    renameEpisode(mediaName, pathDir, query)
elif type == "season":
    renameSeasonFolders(fileName, path, pathDir, query)
elif type == "series":
    renameSeries(fileName, pathDir, query)

print(f"Unable to match: {fileName}")
