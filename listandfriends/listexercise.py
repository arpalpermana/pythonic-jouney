# list exercise using case

books = []

while True:
    book_title = str(input("Input the book title \t: "))
    book_author = str(input("Input the book author \t: "))

    new_book = [book_title, book_author]

    books.append(new_book)

    for book in books:
        print(f"Book {book[0]} is written by {book[1]}")

    end = True if input("Finish input? y/n \t").lower() == "y" else False
    if end:
        print("Program is finished")
        break
