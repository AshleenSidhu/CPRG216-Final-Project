"""
Description: A library management application which loads all books from a CSV into a list, then allows mutliple menu options,
such as search, borrow, return, and exit options. Additional secure options are unlocked with a password and allows librarians to 
add, remove and print catalog for books. 

Author: Phattharaporn I. and Ashleen S.
Date: 2024-04-11
"""
from book import Book
import os

def load_books(file_name):
    #recieves empty list 
    book = []

    book_obj = open(file_name, "r")

    for line in book_obj:
        books = line.rstrip().split(",")
        book.append(books)
    return len(book)


def print_menu():
    pass



def search_books():
    pass



def borrow_book():
    pass



def find_book_by_isbn():
    pass



def return_book():
    pass




def add_book():
    pass




def remove_book():
    pass




def print_books():
    pass




def save_books():
    pass






def main():
    print("Starting the system...")
    file_name = str(input("Enter book catalog filename: "))

    if os.path.exists(file_name): #if file does exists enter confirmation message
        print("Book catalog has been loaded\n", end="")
        book = load_books(file_name)
    else: #file does not exist enter error message and leave program
        print(f"File not found. Re-enter book catalog filename: ")
        return
    
    options = 

    while(options != 0):
        print()