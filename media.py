import webbrowser


class Movie():
    # underscore to tell user that is reserved
    # creates space in memory for that instance
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # open trailer video popup
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
