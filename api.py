import requests

api_key="k_z6069o8g"

def search(url):
	print(f"-- Calling [{url}]")

	response = requests.request("GET", url)
	results = response.json()["results"]
	return results

def searchEpisode(text):
	url = f"https://imdb-api.com/en/API/SearchEpisode/{api_key}/{text}"
	return search(url)

def searchSeries(text):
	raise Exception("Not yet implemented")