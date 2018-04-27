# -*- coding: utf-8 -*-
"""Stores details of movies and displays them on a website."""

import media
import fresh_tomatoes

"""Creating six Movie objects, initialising these objects with title, storyline,
    poster image link and video trailer link of respective movies"""

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission ",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

life_of_pi = media.Movie("Life of Pi",
                     "A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery.",
                     "https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg",
                     "https://youtu.be/j9Hjrs6WQ8M")

brave =  media.Movie("Brave",
                     "Determined to make her own path in life",
                     "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
                     "https://youtu.be/TEHWDA_6e3M")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "While on a trip to Paris with his fiancée's family, a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight",
                     "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                     "https://youtu.be/FAfR8omt-CY")

pulp_fiction = media.Movie("Pulp Fiction",
                     "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                     "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                     "https://youtu.be/s7EdQ4FqbhY")


barfi = media.Movie("Barfi",
                     "Shruti loves Barfi, a hearing and speech-impaired man, but marries someone else.Years later, she learns that he is in love with an autistic girl, and feels the need to rethink her own marriage",
                     "https://upload.wikimedia.org/wikipedia/en/2/2e/Barfi%21_poster.jpg",
                     "https://youtu.be/8ijur-W6vW8")


# Store the Movie objects in a list
movies = [avatar,life_of_pi,brave,midnight_in_paris,pulp_fiction,barfi]
#passing list of movies to function open_movies_page(), which is defined inside fresh_tomatoes module
fresh_tomatoes.open_movies_page(movies)






