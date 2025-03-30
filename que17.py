books = [
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
{"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
{"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
{"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]
#remove books
books.remove(books[0])
#add books
new_list=[{"title": "The himalayan", "author": "F. howland", "year": 1994}]
for new_books in new_list:
    books.append(new_books)
print(books)

#search a book by title
user=input("Enter a book title: ")
for i in books:
    if user==i['title']:
        print(i)
        break
    else:
        print("No books were found")

#Search for a book by author (optional)
user=input("Enter a book author: ")
for i in books:
    if user==i['author']:
        print(i)
        break
    else:
        print("No authors were found")

for book in books:
    print(book)

