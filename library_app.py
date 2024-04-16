"""
Description: A library management application which loads all books from a CSV into a list, then allows mutliple menu options,
such as search, borrow, return, and exit options. Additional secure options are unlocked with a password and allows librarians to 
add, remove and print catalog for books. 

Author: Phattharaporn I. and Ashleen S.
Date: 2024-04-11
"""

from book import Book
from typing import Final
import os

#disctionary for menu selections
menu_options = {
    "1": ". Search for books",
    "2": ". Borrow a book",
    "3": ". Return a book",
    "0": ". Exit the system"
}

#heading string
menu_heading = ("\nReader's Guild Library - Main Menu")

#function for adding 
def load_books(book, file_name):
    
    book_obj = open(file_name, "r")

    for line in book_obj:
        split_books = line.rstrip().split(",")
        books = Book(split_books[0], split_books[1], split_books[2], split_books[3], split_books[4])
        book.append(books)
    return len(book)


def print_menu(menu_heading, menu_options):
    #prints the heading
    print(menu_heading)
    print("=" * len(menu_heading))

    #prints the menu options from dictionary
    for key, value in menu_options.items():
        print(f"{key}{value}")

    #asks user for a selection from the menu
    while True:
        user_choice = input("Enter your selection: ")
        if user_choice in menu_options:
            return user_choice 
        else: #otherwise if menu option is not found print error message
            print("Invalid option")


def search_books(book, user_search):
    #list for the user searches to be saved to
    search_result = []
    
    if user_search in book:
        search_result.append(book)
        #print_books()
    else:
        print("No matching books found.")


def borrow_book(book):
    #input ISBN from the user and calls find_book_by_isbn()
    ISBN: Final =input("Enter the 13-digit ISBN (format 999-9999999999): ")

    #finds the ISBN through calling the find_book_by_isbn function
    find_book = find_book_by_isbn(book, ISBN)

    #if the input from the user is invalid print error message
    if find_book is None:
        print("No book found with that ISBN")
        return
    
    #otherwise if book is found then display it's availablility
    if book.get_availability() == "Available":
        print(f"{book.get_title()} with ISBN {book.get_isbn()} successfully borrowed.")
        book.borrow_it() #invokes the borrow method
    else: 
        print(f"{book.get_title()} with ISBN {book.get_isbn()} is not currently available.")
        return


def find_book_by_isbn(book, ISBN):
    #assigning and intializing index variable to 0
    index = 0

    #iterate through the book list
    for index in range(len(book)):
        if book[index].get_isbn() == ISBN: #compare the isbn of the book with index to find the required isbn that the user is searching for
            return index #return index if isbn is found 
    return -1 #return -1 if isbn is not found 


def return_book():
    pass




def add_book():
    pass




def remove_book():
    pass




def print_books(book, user_search):
    pass




def save_books():
    pass



def main():
    #book empty list 
    book = []

    print("Starting the system...")
    file_name = input("Enter book catalog filename: ")

    #checks to see if file name is valid    
    if os.path.exists(file_name): #if file does exists enter confirmation message
        print("Book catalog has been loaded\n", end="")
        book = load_books(book, file_name)
    else: #file does not exist enter error message and leave program
        print(f"File not found. Re-enter book catalog filename: ")


    while True:

        #displays menu and gets users selection input
        user_choice = print_menu(menu_heading, menu_options)

        # choice 1
        if user_choice == "1":
            print("-- Search for books --")
            #input search string from user
            user_search = input("Enter search value: ")
            #calls search_books function
            search_books(book, user_search)
            
        # choice is 2 
        if user_choice == "2":
            print("-- Borrow a book --")
            #calls the borrow_book function
            borrow_book(book)
            
            
        save_books()

    
if __name__ == "__main__":
    main()