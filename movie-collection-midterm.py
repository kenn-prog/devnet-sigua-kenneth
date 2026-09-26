"""
Midterm Practical Exam — Movie Collection Manager
Student: Kenneth Sigua
"""

movie_list = [
    {
        "movie_title":"spiderman 3",
        "director":"Kenneth",
        "status":{"Watched":1},
    }, 
]

def display_menu():
    print("===  Movie Collection Manager ===") #menu na to
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")
    pass


def add_movie(movie_list):
    movie = [] #mapupunta mga added movie dito
    movie_title = input("Enter movie title: ")
    if movie_title in movies:
        print("The movie is exist!")
    movie.append(movie_title)

    director = input("Enter director: ")
    movie.append(director)
    status = input("Enter status: ")
    movie.append(status)

    print("Movie added successfully")
    return movie
    pass


def view_movies(movie_list):
    print("=== All Movies ===")
    for x,y,z in movie_list.items():
        print(x,y,z)
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    return None


# def main():
    
#     display_menu()
#     user_choice = input(int("Choose an option:"))

#     if user_choice == 1:
#         add_movie(movie_list)
#     elif user_choice == 2:
#         view_movies(movie_list)
#     elif user_choice == 3:
#         count_watched_unwatched()
#     elif user_choice == 4:
#         find_movie()
#     elif user_choice == 5:
#         #break:

    #pass


#main()
view_movies(movie_list)