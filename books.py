import numpy as np
import pandas as pd

data = pd.read_csv("books.csv")

#List the Top 10 authors by their average rating.
work = data[['authors','average_rating']]
total_rating = work.groupby(['authors']).agg({'average_rating' : 'mean'})
num = work.groupby('authors').size().reset_index(name='count')
authors_average = total_rating.sort_values('average_rating', ascending=False)
top_ten_rating = authors_average.head(10)
print("TOP TEN AUTHORS BY THEIR AVERAGE RATING")
print('\n')
print(top_ten_rating)
top_ten_rating.to_csv('averagerating.csv', encoding='utf-8')

#Recommend 10 books similar to "The Golden Compass" by Philip Pullman.
#Initially, we are only considering the other books written by the same author
same_author = data[data['authors'].str.contains("Philip Pullman")==True]
# We were only able to get a total of 7 books excluding the golden compass book
#Therefore, we are using other criterias like average rating, language code and publication year to find the remaining three identical books.
sim_book = data.loc[(data['average_rating'] == 3.94)]
sim_book = sim_book.loc[sim_book['language_code'] == 'eng']
sim_book = sim_book.loc[(sim_book['original_publication_year'] > 1993) & (sim_book['original_publication_year'] < 1996)]

ten_similar_books = pd.concat([same_author,sim_book])
ten_similar_books = ten_similar_books[ten_similar_books.title != 'The Golden Compass (His Dark Materials, #1)']
just_books = ten_similar_books['title']
print('\n')
print("RECOMMENDING 10 BOOKS SIMILAR TO THE GOLDEN COMPASS BY PHLIP PULLMAN")
print('\n')

print("A CSV file will also be created in the same folder where the python code is stored where you can view the entire information about the recommended books")
print("Name of the csv file is ten.csv")

print('\n')

print(just_books)
ten_similar_books.to_csv('ten.csv', encoding='utf-8', index=False)
