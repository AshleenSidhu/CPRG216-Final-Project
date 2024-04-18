"""
Description: A library management application which loads all books from a CSV into a list, then allows mutliple menu options,
such as search, borrow, return, and exit options. Additional secure options are unlocked with a password and allows librarians to 
add, remove and print catalog for books. 

Author: Phattharaporn I. and Ashleen S.
Date: 2024-04-11
"""

from book import Book
import os

#dictionary for menu selections
menu_options = {
    "1": ". Search for books",
    "2": ". Borrow a book",
    "3": ". Return a book",
    "0": ". Exit the system"
}

#heading string
menu_heading = ("\nReader's Guild Library - Main Menu")

#function for loading books from a file
def load_books(books, file_name):
    book_obj = open(file_name, "r")

    for line in book_obj:
        split_books = line.rstrip().split(",")
        book = Book(split_books[0], split_books[1], split_books[2], split_books[3], split_books[4])
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

#fubction for searching books
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
            print(f"'{books[index].get_title()}' with ISBN {books[index].get_isbn()} successfully borrowed.")
            books[index].borrow_it() #invokes the borrow method
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


def return_book(books):
    pass




def add_book(books):
    pass




def remove_book(books):
    pass


#function for printing books
def print_books(books):
    #display book heading
    print(f"{'ISBN':<15}{'Title':<26}{'Author':<26}{'Genre':<21}{'Availability'}")
    print("-" * 14, "-" * 25,  "-" * 25, "-" * 20, "-" * 12)

    #formats each book in the book list
    for book in books:
        print(f"{book.get_isbn()} {book.get_title():<25} {book.get_author():<25} {book.get_genre_name():<20} {book.get_availability()}")


def save_books(books, file_name):
    pass

#main function
def main():
    #empty list for books
    books = []

    #starts the program
    print("Starting the system...")
    file_name = input("Enter book catalog filename: ")

    #loops if file name is invalid so user has to re-enter another file name
    while not os.path.exists(file_name):
        file_name = input(f"File not found. Re-enter book catalog filename: ")
    
    #if file name is valid call the load books function and displays appropriate message
    load_books(books, file_name)
    print("Book catalog has been loaded\n", end="")


    while True:
        #displays menu and gets users selection input
        user_choice = print_menu(menu_heading, menu_options)

        #if user selects librarian menu options
        if user_choice == "2130":
        
            print("\nReader's Guild Library - Librarian Menu\n" + "=" * 39)

            #print_menu(menu_heading, menu_options)
            del menu_options["0"]
            menu_options["4"] = ". Add a book"
            menu_options["5"] = ". Remove a book"
            menu_options["6"] = ". Print catalog"
            menu_options["0"] = ". Exit the system"

            #prints the librarian menu options
            for key, value in menu_options.items():
                print(f"{key}{value}")

            librarian_choice = input("Enter your selection: ")

            #user selects library additional options
            if librarian_choice == "4":
                print("\n-- Add a book --")
                add_book(books)
            if librarian_choice == "5":
                print("\n-- Remove a book --")
                remove_book(books)
            if librarian_choice == "6":
                print("\n-- Print catalog --")
                print_books(books)

            if librarian_choice in menu_options:
                user_choice = librarian_choice
        
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
        if user_choice == "2":
            print("\n-- Borrow a book --")
            
            #calls the borrow_book function
            borrow_book(books)
        
        # selection 3
        if user_choice == "3":
            print("\n-- Return a book --")
            
        # selection 0 
        if user_choice == "0":
            print("\n-- Exit the system --")
            save_books(books)
            print("Book catalog has been saved.\nGood Bye!")

  
if __name__ == "__main__":
    main()