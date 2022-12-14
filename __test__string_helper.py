import helpers.string_helpers as string_helpers
import unittest

class TestStringHelperMethods(unittest.TestCase):
    
    def setUp(self):
        self.mock_desc = "(1992) (TV Episode) - Season 4 | Episode 2 - The Simpsons (1989) (TV Series)"
        self.mock_file = "A Streetcar Named Marge.mp4"
        self.mock_folder = "The Simpsons (Complete) Season 4"

    def test_getYearFromDescription(self):
        year = string_helpers.getYearFromDescription(self.mock_desc)
        self.assertEqual(year, "1992")

    def test_getEpisodeCodeFromDescription(self):
        episode_code = string_helpers.getEpisodeCodeFromDescription(self.mock_desc)
        self.assertEqual(episode_code, "s04e02")

    def test_getSeriesTitleFromDescription(self):
        episode_code = string_helpers.getSeriesTitleFromDescription(self.mock_desc)
        self.assertEqual(episode_code, "The Simpsons")

    def test_append0IfLessThan10_05(self):
        zero_5 = string_helpers.append0IfLessThan10(5)
        self.assertEqual(zero_5, "05")

    def test_append0IfLessThan10_002(self):
        zero_zero_2 = string_helpers.append0IfLessThan10("002")
        self.assertEqual(zero_zero_2, "02")

    def test_getSeasonNumber(self):
        folder_name = string_helpers.getSeasonNumber(self.mock_folder)
        self.assertEqual(folder_name, "Season 04")
    
    def test_removeFileExtension(self):
        clean_string = string_helpers.removeFileExtension(self.mock_file)
        self.assertEqual(clean_string, "A Streetcar Named Marge")

    def test_getFileExtension(self):
        extension = string_helpers.getFileExtension(self.mock_file)
        self.assertEqual(extension, ".mp4")

    def test_hasNumber(self):
        has_number = string_helpers.hasNumber("Season 09")
        self.assertEqual(True, has_number)

if __name__ == '__main__':
    unittest.main()