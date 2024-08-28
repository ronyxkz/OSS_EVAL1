class LibraryInventory:
    def __init__(self):
        self.books = {} 

    def add_book(self, isbn, title, author, genre, availability):
       
            self.books[isbn] = {
                'title': title,
                'author': author,
                'genre': genre,
                'availability': availability
            }
            print(f"Book '{title}' added successfully.")

    def update(self, isbn, title=None, author=None, genre=None, availability=None):
       
            if title is not None:
                self.books[isbn]['title'] = title
            if author is not None:
                self.books[isbn]['author'] = author
            if genre is not None:
                self.books[isbn]['genre'] = genre
            if availability is not None:
                self.books[isbn]['availability'] = availability
            print(f"Book with ISBN {isbn} updated successfully.")

    def search(self, isbn):
        book = self.books.get(isbn)
        if book:
            return book
        else:
            print(f"Book with ISBN {isbn} not found.")
            return None

if __name__ == "__main__":

    library = LibraryInventory()
    
  
    library.add_book('1234', 'game of thrones', 'RR martin', 'fiction', True)
    library.add_book('5678', 'rich dad poor dad', 'IDK', 'motivation', False)
    
  
    library.update('1234', availability=False)
    

    book = library.search('1234')
    if book:
        print("Book Details:")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print(f"Availability: {'Available' if book['availability'] else 'Not Available'}")
        print()

    library.add_book('36827', 'jaypee', 'megha mam', 'autobiography', True)

    book = library.search('36827')
    if book:
        print("Book Details:")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print(f"Availability: {'Available' if book['availability'] else 'Not Available'}")
        print()
    
    
    

