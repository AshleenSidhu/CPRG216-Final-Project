from book import Book
from typing import Final
import csv
genre_ = {"Romance":0,
         "Mystery":1,
         "Science Fiction":2,
         "Thriller":3,
         "Young Adult":4,
         "Children's Fiction":5,
         "Self-help":6,
         "Fantasy":7,
         "Historical Fiction":8,
         "Poetry":9,
         }


def load_books(book, file_name):
    
    book_obj = open(file_name, "r")
    book_list = []
    
    for line in book_obj:
        split_books = line.rstrip().split(",")
        book_list.append(Book(split_books[0], split_books[1], split_books[2], int(split_books[3]), eval(split_books[4])))
    return  book_list

def print_books(book):
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title","Author", "Genre", "Availability"))
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("--------------"
                                                    ,"----------------------"
                                                    ,"----------------------"
                                                    , "-------------------"
                                                    , "------------"))
    for b in book:
        print(b)

def add_book(book):
    input_ISBN = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    input_title = input("Enter title: ")
    input_name = input("Enter author name: ")
    
    while True:
        input_genre = input("Enter genre: ")
        if ( input_genre in "Romance, Mystery, Science Fiction, Thriller, Young Adult,Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry"):
            print("Hee")
            genre_number = genre_[input_genre]

            book.append(Book(input_ISBN,input_title,input_name, int(genre_number), True))
            
            break
        else:
            print("\nInvalid genre.")
            print("Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction, Self-help, Fantasy, Historical Fiction, Poetry")
    
    print("genre_number ==",genre_number)
    print(input_title,"with ISBN",input_ISBN,"successfully added.")
    print_books(book)
    
    
def find_book_by_isbn(book, ISBN):
    #assigning and intializing index variable to 0
    index = 0

    #iterate through the book list
    for index in range(len(book)):
        #print(index)
        if book[index].get_isbn() == ISBN: #compare the isbn of the book with index to find the required isbn that the user is searching for
            return index #return index if isbn is found 
    return -1 #return -1 if isbn is not found 

def remove_book(book):
    #print_books(book)
    ISBN: Final = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    find_book = find_book_by_isbn(book, ISBN)
    #print(find_book)
    if find_book == -1:
        print("No book found with that ISBN")
    else:
         print(book[find_book].get_title(),"with ISBN",book[find_book].get_isbn(),"successfully removed.")
         book_list.pop(find_book)


def save_books(book,file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(book)):
            writer.writerow([book[i].get_isbn()
                             ,book[i].get_title()
                             ,book[i].get_author()
                             ,book[i].get_genre_name()
                             ,book[i].get_availability()])

def return_book(book):
    
    ISBN: Final = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    find_book = find_book_by_isbn(book, ISBN)
    print(find_book)
    if find_book == -1:
        print("No book found with that ISBN")
    else:
         if str(book[find_book].get_availability()) == "Available" :
             print(book[find_book].get_title(),"with ISBN",book[find_book].get_isbn(),"is not currently borrowed.")
         elif str(book[find_book].get_availability()) == "Borrowed" :
             print(book[find_book].get_title(),"with ISBN",book[find_book].get_isbn(),"successfully returned.")
             book[find_book].return_it()


book = []
file_name = "books.csv"

book_list = load_books(book, file_name)

#return_book(book_list)
#save_books(book_list,file_name)
#remove_book(book_list)
#print_books(book_list)
#add_book(book_list)





