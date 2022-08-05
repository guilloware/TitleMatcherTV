import unittest
import api
import responses

class TestApi(unittest.TestCase):
    
    def setUp(self):
        self.mock_desc = "(1992) (TV Episode) - Season 4 | Episode 2 - The Simpsons (1989) (TV Series)"

        self.mock_search_episode_results = [{
            "id":"tt0701048",
            "resultType":"Title",
            "image":"https://m.media-amazon.com/images/M/MV5BZjQ3YWEzODEtNmE2Ny00NWU0LTkzNWQtZjM2ZjI5YTFhZDhlXkEyXkFqcGdeQXVyNjcwMzEzMTU@._V1_Ratio1.3182_AL_.jpg",
            "title":"A Streetcar Named Marge",
            "description":"(1992) (TV Episode) - Season 4 | Episode 2 - The Simpsons (1989) (TV Series)"
        }]

        self.mock_search_episode_response = {
            "searchType":"Episode",
            "expression":"the simpsons  a streetcar named marge",
            "results":self.mock_search_episode_results,
            "errorMessage":""
        }

    @responses.activate 
    def test_searchEpisode(self):
        responses.add(
            responses.GET,
            "https://imdb-api.com/en/API/SearchEpisode/%7Bapi_key%7D/%7Btext%7D",
            json=self.mock_search_episode_response,
            status=200,
        )

        response = api.searchEpisode("the simpsons a streetcar named marge")
        self.assertEqual(response, self.mock_search_episode_results)

if __name__ == '__main__':
    unittest.main()