import helpers.string_helpers as string_helpers

class EpisodeTitle:
    def __init__(self, id, episodeTitle, description, fileName, extension):
        self.id = id
        self.title = episodeTitle
        self.description = description
        self.fileName = fileName
        self.extension = extension
        self.series_title = string_helpers.getSeriesTitleFromDescription(description)
        self.year = string_helpers.getYearFromDescription(description)
        self.episode_code = string_helpers.getEpisodeCodeFromDescription(description)
        self.plex_title = self.formPlexTitle()

    def formPlexTitle(self):
        return f"{self.series_title} ({self.year}) - {self.episode_code} - {self.title}{self.extension}"

class SeriesTitle:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description
        self.year = string_helpers.getYearFromDescription(description)
        self.plex_title = self.formPlexSeriesTitle()

    def formPlexTitle(self):
        return f"{self.title} ({self.year})"