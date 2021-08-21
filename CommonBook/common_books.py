# Exercise - To find all the coding books published within the last two years
# all-coding-books.txt - data file containing all coding book's ID
# books-published-last-two-years.txt - data file containing all book's ID published in last two years
# One approach to find the books in both files.

import time
import pandas as pd
import numpy as np

with open('books-published-last-two-years.txt') as f:
    recent_books = f.read().split('\n')
    
with open('all-coding-books.txt') as f:
    coding_books = f.read().split('\n')

start = time.time()
recent_coding_books = []

for book in recent_books:
    if book in coding_books:
        recent_coding_books.append(book)

print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))
