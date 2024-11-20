class Book:
  def __init__(self, title, author, copies):
     self.title = title
     self.author = author
     self.copies = copies

  def __str__(self):
     return f"Title: {self.title}, Author: {self.author}, Copies: {self.copies}"
  
class Library:
  def __init__(self):
     self.books = []

  def add_book(self, book):
     self.books.append(book)

  def list_books(self):
     for book in self.books:
       print(book)

  def find_book(self,books,title):
     for i in books:
        book_words= i.split()
        if book_words[1] == title:
           return i
        else:
           return "Is not on the list"
  def print_list(self,object):
     print(list(object))
     
     
     
# Example Usage

library = Library()
library.add_book(Book("Python 101", "John Doe", 3))
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))
library.list_books()
example = [
    'Title: Python 101, Author: John Doe, Copies: 3',
    'Title: Data Science Handbook, Author: Jane Smith, Copies: 5',
    'Title: AI for Beginners, Author: Alice Brown, Copies: 2',
    'Title: Machine Learning, Author: Bob White, Copies: 4'
]
found=library.find_book(example,'Data Science')
print(f'The book found: {found}')

library.print_list(library)
#print(list(library))