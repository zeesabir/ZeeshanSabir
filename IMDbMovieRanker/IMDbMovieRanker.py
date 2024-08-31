from imdb import IMDb

# Initialize IMDb object
ia = IMDb()

# Movie name input from user
movie_name = input("Please enter the movie name: ")

# Search for the movie
movies = ia.search_movie(movie_name)

if movies:
    movie = movies[0]  # Get the first movie result
    ia.update(movie)  # Update the movie object to fetch details
    rating = movie.get('rating')
    title = movie.get('title')
    
    if rating:
        print(f"The IMDb rating for {title} is {rating}.")
    else:
        print(f"Rating for {title} not found.")
else:
    print(f"No results found for {movie_name}.")
