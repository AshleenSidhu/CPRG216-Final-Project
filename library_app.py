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
import csv


#function for loading books from a file
def load_books(books, file_name):
    book_obj = open(file_name, "r")

    for line in book_obj:
        split_books = line.rstrip().split(",")
        book = Book(split_books[0], split_books[1], split_books[2], int(split_books[3]), split_books[4])
        books.append(book)
    return len(books)

#function for printing the menu
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
        if user_choice in menu_options or user_choice == "2130":
            return user_choice 
        else: #otherwise if menu option is not found print error message
            print("Invalid option")

#function for searching books
def search_books(books, user_search):
    #list for the user searches to be saved to
    search_result = []
    
    #searches through each book in the book list for the user input
    for book in books:
        if user_search.lower() in book.get_isbn() or \
            user_search.lower() in book.get_title().lower() or \
            user_search.lower() in book.get_author().lower() or \
            user_search.lower() in book.get_genre_name().lower():
                search_result.append(book)
    #if the search list is 0 then there are no books matching the atrributes in the book list
    if len(search_result) == 0:
        print("No matching books found.")
    return search_result 

#function for borrowing books
def borrow_book(books):
    #input ISBN from the user and calls find_book_by_isbn()
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    #finds the ISBN through calling the find_book_by_isbn function
    index = find_book_by_isbn(books, isbn)

    #if the input from the user is invalid print error message
    if index == -1:
        print("No book found with that ISBN.")
    else:
        #otherwise if book is found then display it's availablility
        if books[index].get_availability() == "Available":
            books[index].borrow_it() #invokes the borrow method
            print(f"'{books[index].get_title()}' with ISBN {books[index].get_isbn()} successfully borrowed.")
        else: 
            print(f"'{books[index].get_title()}' with ISBN {books[index].get_isbn()} is not currently available.")

#function for finding the book by ISBN
def find_book_by_isbn(books, isbn):
    #assigning and intializing index variable to 0
    index = 0

    #iterate through the book list
    for index in range(len(books)):
        if books[index].get_isbn() == isbn: #compare the isbn of the book with index to find the required isbn that the user is searching for
            return index #return index if isbn is found 
    return -1 #return -1 if isbn is not found 

#function for returning books
def return_book(books):
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(books, isbn)
 
    if index == -1:
        print("No book found with that ISBN.")
    else:
         if books[index].get_availability() == "Available" :
            print(f"'{books[index].get_title()}' with ISBN {books[index].get_isbn()} is not currently borrowed.")
         elif books[index].get_availability() == "Borrowed" :
            print(f"'{books[index].get_title()}' with ISBN {books[index].get_isbn()} successfully returned.")
            books[index].return_it()

#function for adding books
def add_book(books):
    input_isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    input_title = input("Enter title: ")
    input_name = input("Enter author name: ")
    
    genre_number = None
    while genre_number is None:
        input_genre = input("Enter genre: ")

        for key, value in Book.GENRE_NAMES.items():
            if input_genre.lower() == value.lower():
                genre_number = key
                break
        if genre_number is None:
            print("Invalid genre. Choices are:", ", ".join(Book.GENRE_NAMES.values()))

    #adds the book to the book list
    books.append(Book(input_isbn, input_title, input_name, int(genre_number), "True"))
    #print("genre_number ==",genre_number)
    print(f"'{input_title}' with ISBN {input_isbn} successfully added.")
    
    
#function for removing books
def remove_book(books):
    #print_books(book)
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(books, isbn)

    if index == -1:
        print("No book found with that ISBN.")
    else:
         print(f"'{books[index].get_title()}' with ISBN {books[index].get_isbn()} successfully removed.")
         books.pop(index)


#function for printing books
def print_books(books):
    #display book heading
    print(f"{'ISBN':<15}{'Title':<26}{'Author':<26}{'Genre':<21s}{'Availability'}")
    print("-" * 14, "-" * 25,  "-" * 25, "-" * 20, "-" * 12)

    #formats each book in the book list
    for book in books:
        print(book)

#function for saving books
def save_books(books, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(books)):
            
            writer.writerow([books[i].get_isbn()
                             ,books[i].get_title()
                             ,books[i].get_author()
                             ,books[i].get_genre()
                             ,books[i].get_availability()])

#main function
def main():
    #empty list for books
    books = []

    #dictionary for menu selections
    MAIN_MENU: Final = {
    "1": ". Search for books",
    "2": ". Borrow a book",
    "3": ". Return a book",
    "0": ". Exit the system"
    }

    #dictionary for librarian menu selections
    LIBRARIAN_MENU: Final = {
    "1": ". Search for books",
    "2": ". Borrow a book",
    "3": ". Return a book",
    "4": ". Add a book",
    "5": ". Remove a book",
    "6": ". Print catalog",
    "0": ". Exit the system"
    }

     #variable assigned for main menu header string
    MAIN_HEADING: Final = ("\nReader's Guild Library - Main Menu")
    LIBRARIAN_HEADING: Final = ("\nReader's Guild Library - Librarian Menu")

    #starts the program
    print("Starting the system...")
    file_name = input("Enter book catalog filename: ")

    #loops if file name is invalid so user has to re-enter another file name
    while not os.path.exists(file_name):
        file_name = input(f"File not found. Re-enter book catalog filename: ")
    
    #if file name is valid call the load books function and displays appropriate message
    load_books(books, file_name)
    print("Book catalog has been loaded\n", end="")

    menu_heading = MAIN_HEADING
    menu_options = MAIN_MENU
    is_librarian = False

    while True:
        #displays menu and gets users selection input
        user_choice = print_menu(menu_heading, menu_options)

        #if user enters special passcode 2130 then librarian options are unlocked
        if user_choice == "2130":
            menu_heading = LIBRARIAN_HEADING
            menu_options = LIBRARIAN_MENU
            is_librarian = True
            user_choice = print_menu(menu_heading, menu_options)

       # selection 1
        if user_choice == "1":
            print("\n-- Search for books --")

            #input search string from user
            user_search = input("Enter search value: ")
            #calls search books function
            matched_books = search_books(books, user_search)
            #if matching search is found then prints the search results 
            if matched_books:
                print_books(matched_books)
            
        # selection 2 
        elif user_choice == "2":
            print("\n-- Borrow a book --")
            
            #calls the borrow_book function
            borrow_book(books)
        
        # selection 3
        elif user_choice == "3":
            print("\n-- Return a book --")
            return_book(books)    

        elif user_choice == "4" and is_librarian:
            print("\n-- Add a book --")
            add_book(books)
            
        elif user_choice == "5" and is_librarian:
            print("\n-- Remove a book --")
            remove_book(books)
    
        elif user_choice == "6" and is_librarian:
            print("\n-- Print catalog --")
            print_books(books)

        # selection 0 
        if user_choice == "0":
            break

    print("\n-- Exit the system --")
    save_books(books, file_name)
    print("Book catalog has been saved.\nGood Bye!")

  
if __name__ == "__main__":
    main()