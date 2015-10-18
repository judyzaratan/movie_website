import media
import fresh_tomatoes

silver_linings = media.Movie("Silver Linings Playbook",
                        "A romantic comedy about a man who tries to rebuild his life and relationships after a stint in a mental hospital",
                        "http://www.impawards.com/2012/posters/silver_linings_playbook.jpg",
                        "https://www.youtube.com/watch?v=Lj5_FhLaaQQ")
#calls init function to create a new movie

guardians = media.Movie("Guardians of the Galaxy",
                       "A comic based movie",
                       "http://static2.hypable.com/wp-content/uploads/2014/05/guardians-of-the-galaxy-poster-new-HD.jpg",
                       "https://www.youtube.com/watch?v=GQRqShJGIJc")

into_darkness = media.Movie("Star Trek Into Darkness",
                     "Crew of Starship Enterprise deal with a terrorist who has a personal vendetta against Spock ",
                     "http://www.impawards.com/2013/posters/star_trek_into_darkness_ver2_xlg.jpg",
                     "https://www.youtube.com/watch?v=r5gdbUC9mWU")

wall_e = media.Movie("Wall-E",
                    "A story about a little robot who changes the Universe",
                    "http://www.impawards.com/2008/posters/wall_e.jpg",
                    "https://www.youtube.com/watch?v=alIq_wG9FNk")
lego = media.Movie("The Lego Movie",
                    "A computer animated movie about the Lego Universe",
                    "http://vignette4.wikia.nocookie.net/transcripts/images/e/ea/LEGO-Movie-Poster-2014-HIgh-Resolution.jpg/revision/latest?cb=20150313225134",
                    "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

batman = media.Movie("Batman Begins",
                     "The story of how Bruce Wayne, a young billionaire, becomes a crime-fighting superhero for the city of Gotham",
                     "http://nsamovie.com/wp-content/uploads/2013/01/batman_begins_teaser_c.jpg",
                     "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

movies = [silver_linings, guardians, into_darkness, wall_e, lego, batman]
fresh_tomatoes.open_movies_page(movies)
