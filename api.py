import requests

api_key="k_z6069o8g"

def search(url):
	print(f"-- Calling [{url}]")

	response = requests.request("GET", url)
	results = response.json()["results"]
	return results

def searchEpisode(file_name):
	search_methods = []
	search_methods.append(file_name)
	try: 
		search_methods.append(file_name.split(']')[1])
	except:
		print("-search method warning-")

	for text in search_methods:
		url = f"https://imdb-api.com/en/API/SearchEpisode/{api_key}/{text}"
		results =  search(url)
		if len(results) > 0:
			return results		

def searchSeries(text):
	url = f"https://imdb-api.com/en/API/SearchSeries/{api_key}/{text}"
	return search(url)