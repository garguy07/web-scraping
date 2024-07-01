import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

output_file = open('q1text.txt', 'w')

genre_freq = {}

for i in range (1, 11):
#for i in range (1, 3):
    k = str(i)
    url = "https://www.imdb.com/list/ls098063263/?st_dt=&mode=detail&page=" + k + "&sort=list_order,asc"
    #print(url)
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    movie_section = soup.find('div', {'class': 'lister-list'})
    #print(movie_section)

    for movie in movie_section.find_all('div', {'class': 'lister-item mode-detail'}):
        #print("wtf\n")
        duration_element = movie.find('span', {'class': 'runtime'})
        #print(duration_element)
        title_element = movie.find('h3', {'class': 'lister-item-header'})
        #print(title_element)
        year_element = movie.find('span', {'class': 'lister-item-year'})
        #print(year_element)
        gross_element = movie.find('div', {'class': 'list-description'}).find('p').find('b')
        #print(gross_element)
        rating_element = movie.find('span', {'class': 'ipl-rating-star__rating'})
        #print(rating_element)
        genre_element = movie.find('span', class_ = 'genre')
        #print(genre_element)

        duration = duration_element.text.strip(' min')
        title = title_element.find('a').text.strip()
        year = year_element.text.strip('()')
        gross = gross_element.text.strip('$')
        gross = gross.replace(',', '')
        rating = rating_element.text.strip()
        genres = genre_element.text.strip().split(', ')

        year = year.replace('I', '')
        year = year.replace('V', '')
        year = year.replace('X', '')
        year = year.replace('L', '')
        year = year.replace('(', '')
        year = year.replace(')', '')
        year = year.replace(' ', '')

        for genre in genres:
            if genre in genre_freq:
                genre_freq[genre] += 1
            else:
                genre_freq[genre] = 1

        #output_file.write("{title} ({year}): ${gross}M")
        #output_file.write(title + " (" + year + ") : $" + gross + "M\n")
        #output_file.write(title + "," + gross + "\n")
        #output_file.write(title + " " + gross + "\n")
        output_file.write(title + "|" + year + "|" + duration + "|" + gross + "|" + rating + "|")
        for x in genres:
            output_file.write(x + ", ")
        output_file.write("\n")

output_file.close()

g = []
f = []

for xx, yy in genre_freq.items():
    g.append(xx)
    f.append(yy)

plt.bar(g, f)

plt.title('Genre Frequency')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.xticks(rotation=90)

plt.savefig('graph1.png')

plt.show()

x = []
y = []
z = []
flag = False

file = open('q1text.txt', 'r')
for i in range (100):
    values = file.readline().split('|')
    #print(values[0] + " " + values[3])
    if values[0] == "The Lion King" and flag == False:
        values[0] = "The Lion King (2019)"
        flag = True
    x.append(values[0])
    temp = int(values[3])/1000000
    y.append(temp)

plt.plot(x, y)

plt.title('Movie Gross')
plt.xlabel('Movie Name')
plt.ylabel('Gross (in millions)')
plt.xticks(rotation=90)

plt.savefig('graph2.png')

plt.show()

file.close()
