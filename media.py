import webbrowser


class Movie:
    """ Movie class to model movie data

    Attributes:
        title (str): movie title
        storyline (str): brief plot description
        poster_image_url (str): url of the movie poster art
        trailer_youtube_url (str): url of the movie trailer on youtube

    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # use webbrowser to open the trailer URL
        webbrowser.open(self.trailer_youtube_url)
