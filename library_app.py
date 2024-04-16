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
def load_books(books, file_name):
    
    book_obj = open(file_name, "r")

    for line in book_obj:
        split_books = line.rstrip().split(",")
        book = Book(split_books[0], split_books[1], split_books[2], split_books[3], split_books[4])
        books.append(book)
    return len(books)


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


def search_books(books, user_search):
    #list for the user searches to be saved to
    search_result = []
    
    #searches through each book in the book list for the user input
    for book in books:
        if user_search in book.get_isbn() or \
            user_search in book.get_title().lower() or \
            user_search in book.get_author().lower() or \
            user_search in book.get_genre().lower():
                search_result.append(book)
    #if the search list is 0 then there are no books matching the atrributes in the book list
    if len(search_result) == 0:
        print("No matching books found.")
    return search_result 


def borrow_book(books):
    #input ISBN from the user and calls find_book_by_isbn()
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    #finds the ISBN through calling the find_book_by_isbn function
    index = find_book_by_isbn(books, isbn)

    #if the input from the user is invalid print error message
    if index == -1:
        print("No book found with that ISBN")
    
    #otherwise if book is found then display it's availablility
    if books[index].get_availability() == "Available":
        print(f"{books.get_title()} with ISBN {books.get_isbn()} successfully borrowed.")
        books.borrow_it() #invokes the borrow method
    else: 
        print(f"{books.get_title()} with ISBN {books.get_isbn()} is not currently available.")
        return


def find_book_by_isbn(books, isbn):
    #assigning and intializing index variable to 0
    index = 0

    #iterate through the book list
    for index in range(len(books)):
        if books[index].get_isbn() == isbn: #compare the isbn of the book with index to find the required isbn that the user is searching for
            return index #return index if isbn is found 
    return -1 #return -1 if isbn is not found 


def return_book(books):
    pass




def add_book(books):
    pass




def remove_book(books):
    pass




def print_books(books):
    pass




def save_books(books, file_name):
    pass



def main():
    #book empty list 
    books = []

    print("Starting the system...")
    file_name = input("Enter book catalog filename: ")
    while not os.path.exists(file_name):
        file_name = input(f"File not found. Re-enter book catalog filename: ")
        # file_name = input("Enter book catalog filename: ")
    
    load_books(books, file_name)
    print("Book catalog has been loaded\n", end="")
    # #checks to see if file name is valid    
    # if os.path.exists(file_name): #if file does exists enter confirmation message
    #     print("Book catalog has been loaded\n", end="")
    #     load_books(books, file_name)
    # else: #file does not exist enter error message and leave program
    #     print(f"File not found. Re-enter book catalog filename: ")

    find_book_by_isbn(books, ISBN)

    while True:
        #displays menu and gets users selection input
        user_choice = print_menu(menu_heading, menu_options)

        # choice 1
        if user_choice == "1":
            print("\n-- Search for books --")

            #input search string from user
            user_search = input("Enter search value: ")
            #calls search books function
            matched_books = search_books(books, user_search)
            print_books(books)
            print(*matched_books)
            
        # choice is 2 
        if user_choice == "2":
            print("\n-- Borrow a book --")
            #input ISBN from the user and calls find_book_by_isbn()
            #isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
            #calls the borrow_book function
            borrow_book(books)
            
            
        save_books()

    
if __name__ == "__main__":
    main()