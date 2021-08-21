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

## Tip #1: Use vector operations over loops when possible

start = time.time()
recent_coding_books = np.intersect1d(recent_books, coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))

## Tip #2: Know your data structures and which methods are faster

start = time.time()
recent_coding_books = set(recent_books).intersection(coding_books)
print(len(recent_coding_books))
print('Duration: {} seconds'.format(time.time() - start))