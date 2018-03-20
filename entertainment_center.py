import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

black_panther = media.Movie("Black Panther",
                            "African superhero defends Wakanda",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                            "https://www.youtube.com/watch?v=xjDjIWPwcPU")

tag = media.Movie("Tag",
                  "old classmates who have been playing out a game of tag for decades",
                  "https://ia.media-imdb.com/images/M/MV5BMjExMTM4MTQ2OV5BMl5BanBnXkFtZTgwMjA5NjgwNTM@._V1_UX182_CR0,"
                  "0,182,268_AL_.jpg",
                  "https://www.youtube.com/watch?v=N-Jad4oMt_E")

jumanji = media.Movie("Jumanji: Welcome to the Jungle",
                      "board game takes over real life",
                      "https://ia.media-imdb.com/images/M"
                      "/MV5BODQ0NDhjYWItYTMxZi00NTk2LWIzNDEtOWZiYWYxZjc2MTgxXkEyXkFqcGdeQXVyMTQxNzMzNDI"
                      "@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=eA5WqfKsbZg")

sicario = media.Movie("Sicario, Day of the Soldado",
                      "Mexican drug war at the border",
                      "https://ia.media-imdb.com/images/M/MV5BMTY0OTcxNDQyNl5BMl5BanBnXkFtZTgwMzIzOTgwNTM"
                      "@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=sIMChzE_aCo")

avengers = media.Movie("Avengers Infinity War",
                       "Avengers attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts "
                       "an end to the universe.",
                       "https://ia.media-imdb.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM"
                       "@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=iK1R4v0LzAU")

# create movie list here:
my_movies = [toy_story, black_panther, tag, jumanji, sicario, avengers]

# open the movies page in a web browser
fresh_tomatoes.open_movies_page(my_movies)
