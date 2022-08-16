import requests

api_key="k_z6069o8g"

def search(url):
	print(f"-- Calling [{url}]")

	response = requests.request("GET", url)
	results = response.json()["results"]
	return results

def searchEpisode(file_name, query):
	search_methods = []
	if query is not None:
		search_methods.append(query)
	search_methods.append(file_name)
	try: 
		search_methods.append(file_name.split(']')[1])
	except:
		print("-search method warning-")

	matches = []
	for text in search_methods:
		url = f"https://imdb-api.com/en/API/SearchEpisode/{api_key}/{text}"
		results =  search(url)
		if len(results) > 0:
			matches += results
	return matches

def searchSeries(text, query):
	search_methods = []
	if query is not None:
		search_methods.append(query)
	search_methods.append(text)
	url = f"https://imdb-api.com/en/API/SearchSeries/{api_key}/{text}"
	return search(url)