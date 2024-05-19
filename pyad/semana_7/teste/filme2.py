import requests

title = input("Enter the title of the movie: ")  # Prompt the user to enter the movie title

url = f"http://www.omdbapi.com/?t={title}&apikey=84a1f976"
response = requests.get(url)
data = response.json()

if data["Response"] == "True":  # Check if the response is successful
    movie = data  # Define the variable movie

    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
    print("IMDB Rating:", movie["imdbRating"])
    print("Director:", movie["Director"])
    print("Actors:", movie["Actors"])
    print("Plot:", movie["Plot"])
    print("")  # Add a newline
else:
    print("Movie not found or API request failed.")
