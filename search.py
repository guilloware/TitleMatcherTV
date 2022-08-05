import os
import sys
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


def searchShowTitle(fileName, pathDir, titleType, url):
	print(f"-- Processing [{fileName}]")

	querystring = {"info":"mini_info","limit":"50","page":"1","titleType":f"{titleType}"}

	headers = {
		"X-RapidAPI-Key": "b22445fd67mshb97a6fe0450d222p173669jsn36d9412ba3b5",
		"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	results = response.json()["results"]
	for title in results:
		titleText = title["titleText"]["text"]
		year = title["releaseYear"]["year"] if title["releaseYear"] != None else ""
		suggestedTile = f"{titleText} ({year})"

		print('Found Match:')
		print(f"-> {fileName}")
		print(f"-> {suggestedTile}")

		choice = input("Rename? [y,n]\n")

		if(choice == "y"):
			oldPath = os.path.join(pathDir, fileName)
			newPath = os.path.join(pathDir, suggestedTile)
			print(oldPath)
			print(newPath)
			os.rename(oldPath, newPath)
			print(f"Renamed:\n-> {oldPath}\n-> {newPath}")
			os._exit(1)
		elif(choice == "n"):
			print("...")
		else:
			print("Enter [y] or [n]")

	searchShowTitle(originalTitle, pathDir, titleType, url)

titleType = sys.argv[1]
fileName = sys.argv[2]

if os.path.exists(fileName) != True:
	print("Path not valid")
	os._exit(1)

path = Path(fileName)

if titleType != "tvSeries" and titleType != "tvEpisode":
	print("Please enter arg to as tvEpisode or tvSeries")
	os._exit(1)

titleType = "tvSeries"
originalTitle = ""
pathDir = path.parent.absolute()
if titleType == "tvSeries":
	originalTitle = os.path.basename(path)


url=f"https://moviesdatabase.p.rapidapi.com/titles/search/title/{fileName}"
searchShowTitle(originalTitle, pathDir, titleType, url)

print(f"Unable to match: {originalTitle}")