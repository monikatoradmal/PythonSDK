from book import Book
import booksSDK


book = Book('Mother',120)
print(booksSDK.add_books(book))
print((booksSDK.get_books()))