import AK_fav_movies
import media

# Toy Story movie information
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

# Avatar movie information
avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "http://www.youtube.com/watch?v=-9ceBgWV8io")

# Good Will Hunting movie information
gwhunting = media.Movie("Good Will Hunting", "A young janitor story to be a mathematician from MIT Math professor and get treatment from therapist", "https://en.wikipedia.org/wiki/Good_Will_Hunting#/media/File:Good_Will_Hunting.png", "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

# School of Rock movie information
school_of_rock = media.Movie("School of Rock", "An enthusiastic guitarist Dewey Finn gets thrown out of his bar band and finds himself in desperate need of work.", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Ratatouille movie information
ratatouille = media.Movie("Ratatouille", "Remy dreams of becoming a great chef, despite being a rat in a definitely rodent-phobic profession.", "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Midnight in Paris movie information
midnight_in_paris = media.Movie("Midnight in Paris", "Gil Pender is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone.", "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")

# Hunger games movie information
hunger_games = media.Movie("Hunger Games", "In what was once North America, the Capitol of Panem maintains its hold on its 12 districts by forcing them each to select a boy and a girl to compete in a nationally televised event", "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Star Wars 3(Revenge of the Sith) -  movie information
Star_Wars_3 = media.Movie("Star Wars 3 : Revenge of the Sith", "Since the Clone Wars began, the conflict of Jedi and Chancellor Palpatine has become intense. It takes the birth of Darth Vader.", "https://en.wikipedia.org/wiki/Star_Wars:_Episode_III_%E2%80%93_Revenge_of_the_Sith#/media/File:Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg", "https://www.youtube.com/watch?v=5UnjrG_N8hU")

#Array of movies to enumerate
movies = [toy_story, avatar, gwhunting, Star_Wars_3, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

# open and show my recommended movie trailer website
AK_fav_movies.open_movies_page(movies)
