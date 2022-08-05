import os
import sys
import api
from domain.title import Title
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
    
def renameMedia(fileName, pathDir):
    print(f"-- Processing [{fileName}]")

    extension = string_helpers.getFileExtension(fileName) 
    text = string_helpers.removeFileExtension(fileName)
    print(text)
    api_result = api.searchEpisode(text)

    results = api_result

    for t in results:
        title = Title(t['id'], t['title'], t['description'], fileName, extension)
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

type = sys.argv[1]
fileName = sys.argv[2]

if os.path.exists(fileName) != True:
	print("Path not valid")
	os._exit(1)

path = Path(fileName)
pathDir = path.parent.absolute()

if type != "episode" and type != "series":
	print("Please enter arg to as episode or series")
	os._exit(1)

mediaName = fileName

if type == "episode":
    mediaName = os.path.basename(path)

renameMedia(mediaName, pathDir)

print(f"Unable to match: {mediaName}")