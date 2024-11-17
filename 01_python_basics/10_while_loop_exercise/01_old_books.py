favorite_book = input()

counted_books = 0

while True:
    book = input()

    if book == "No More Books":
        print(f"The book you search is not here!\nYou checked {counted_books} books.")
        break
    elif book == favorite_book:
        print(f"You checked {counted_books} books and found it.")
        break
    else:
        counted_books += 1
