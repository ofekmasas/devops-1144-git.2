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

  def find_book(self,title):
     for i in self.books:
        if i.title==title:
           return True
     
     return False



  def print_list(self,object):
     print(list(object))
     
 
     
# Example Usage
library = Library()
if(library.find_book("Data Science Handbook") == True):
   print("The book was found")
else:
   print("The book was not found (before adding it)")
library.add_book(Book("Python 101", "John Doe", 3))
library.add_book(Book("Data Science Handbook", "Jane Smith", 5))
print(library.books)
library.list_books()


# if(library.find_book("Data Science Handbook") == True):
#    print("The book was found")
# else:
#    print("The book was not found")


