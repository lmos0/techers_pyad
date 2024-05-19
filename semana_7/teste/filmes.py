import requests

def search_movie(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=84a1f976"
    response = requests.get(url)
    data = response.json()
    return data

def display_movie_info(movie):
    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
    print("IMDB Rating:", movie["imdbRating"])
    print("Director:", movie["Director"])
    print("Actors:", movie["Actors"])
    print("Plot:", movie["Plot"])
    print("")

def main():
    print("Welcome to Movie Search App!")
    title = input("Enter the title of the movie: ")

    search_result = search_movie(title)

    if search_result["Response"] == "True":
        movies = search_result["Search"]
        for movie in movies:
            display_movie_info(movie)
    else:
        print("No movies found with that title.")

if __name__ == "__main__":
    main()
