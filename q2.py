file = open('q1text.txt', 'r')

movies = []

for line in file:
    fields = line.strip().split('|')
    name = fields[0]
    year = fields[1]
    duration = int(fields[2])
    gross = float(fields[3])
    rating = float(fields[4])
    genres = fields[5].split(', ')

    movie = {'name': name, 'year': year, 'duration': duration, 'gross': gross, 'rating': rating, 'genres': genres}
    movies.append(movie)

file.close()

temp_movies = movies

temp_movies = sorted(temp_movies, key=lambda movie: (-movie['rating'], movie['duration']))

print("Top 100 sorted movies:")
for i in range(100):
    movie = temp_movies[i]
    print(f"{i+1}. {movie['name']}")

print("Filter Options:")
print("1. Duration")
print("2. Imdb Rating")
print("3. Year of Release")
print("4. Genre")

filter_type = int(input("Enter choice:"))

if filter_type == 1:
    print("Enter the range:")
    duration_min, duration_max = map(int, input().split())
    filtered_movies = [movie for movie in movies if duration_min <= movie['duration'] <= duration_max]
elif filter_type == 2:
    print("Enter the range:")
    rating_min, rating_max = map(float, input().split())
    filtered_movies = [movie for movie in movies if rating_min <= movie['rating'] <= rating_max]
elif filter_type == 3:
    print("Enter the range:")
    year_min, year_max = map(int, input().split())
    filtered_movies = [movie for movie in movies if year_min <= int(movie['year']) <= year_max]
elif filter_type == 4:
    genre = input("Enter a genre: ")
    filtered_movies = []
    for i in range(1000):
        xx = movies[i]
        temp = xx['genres']
        #print(temp)
        flag = False
        for cur in temp:
            if cur == genre or cur == genre + ",":
                flag = True
                break
        if flag == True:
            filtered_movies.append(xx)
else:
    print("Invalid filter type.")
    exit()

for i, movie in enumerate(filtered_movies):
    print(f"{movie['name']}")