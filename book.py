"""
Book Class - This class implements and returns the attributes and methods to display books
availability, title, author, isbn, and the genre.
Author: Phattharaporn I. and Ashleen S.
Date: 2024-04-11
"""
from typing import Final 

class Book:
    """
    This class implements attributes and methods, with setters and getters to display book properties
    
    """

    # Constant genre name dictionary 
    GENRE_NAMES: Final = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry",
    }

    # Constructor that has five perameters isbn, title, author, genre, and available 
    def __init__(self, isbn, title, author, genre, available):
        #implement private attributes 
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available

    # Getter Methods
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    # Getter method that returns the name of the genre 
    def get_genre_name(self):
        return self.GENRE_NAMES[self.__genre]

    # Getter method that finds the availability of the book
    def get_availability(self):
        if self.__available == "True":
            return "Available"
        else:
            return "Borrowed"


    # Setters
    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre


    # Sets book's available attribute to False
    def borrow_it(self):
        self.__available = False

    # Sets book's available attribute to True
    def return_it(self):
        self.__available = True

    # Returns book formatted string 
    def __str__(self):
        return f"{self.__isbn:<15s}{self.__title:<26s}{self.__author:<26s}{self.get_genre_name():<21s}{self.get_availability()}"

