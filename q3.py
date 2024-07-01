import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('sh.txt', 'r') as file:
    sh_text = file.read().lower()

with open('stopwords.txt', 'r') as file:
    stopwords = set(file.read().splitlines())

no_punct = ''
for char in sh_text:
    if char not in string.punctuation:
        no_punct += char

lines = no_punct.split('\n')
new_lines = []

cnt = 0

for line in lines:
    words = line.split()
    new_words = []
    for word in words:
        if word not in stopwords and word != '':
            #print("wtf")
            new_words.append(word)
            cnt += 1
    
    if len(new_words) > 0:
        new_lines.append(' '.join(new_words))

#print(new_words)

sh_text = '\n'.join(new_lines)

word_counts = {}
for line in new_lines:
    words = line.split()
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

most_common_word = ''
highest_count = 0

for word in word_counts:
    if word_counts[word] > highest_count:
        highest_count = word_counts[word]
        most_common_word = word

wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(word_counts)

wordcloud.to_file('wordcloud.png')

plt.figure(figsize=(8,8))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

print("Most common word:", most_common_word)

total_word_length = 0

for line in new_lines:
    words = line.split()
    
    for word in words:
        total_word_length += len(word)

avg_word_length = total_word_length / cnt

print("Average word length:", "{0:.2f}".format(avg_word_length))