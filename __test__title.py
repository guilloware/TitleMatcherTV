from domain.title import Title
import unittest

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        id = "tt0701048"
        title = "A Streetcar Named Marge"
        desc = "(1992) (TV Episode) - Season 4 | Episode 2 - The Simpsons (1989) (TV Series)"

        self.title = Title(id, title, desc)
        self.mock_plex_title = "The Simpsons (1992) - s04e02 - A Streetcar Named Marge"

    def test_getYearFromDescription(self):
        plexTitle = self.title.formPlexTitle()
        self.assertEqual(plexTitle, self.mock_plex_title)

if __name__ == '__main__':
    unittest.main()