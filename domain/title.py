import helpers.string_helpers as string_helpers

class Title:
    def __init__(self, id, title, description, fileName, extension):
        self.id = id
        self.title = title
        self.description = description
        self.fileName = fileName
        self.extension = extension
        self.series_title = string_helpers.getSeriesTitleFromDescription(description)
        self.year = string_helpers.getYearFromDescription(description)
        self.episode_code = string_helpers.getEpisodeCodeFromDescription(description)
        self.plex_title = self.formPlexTitle()

        print("done")

    def formPlexTitle(self):
        return f"{self.series_title} ({self.year}) - {self.episode_code} - {self.title}{self.extension}"