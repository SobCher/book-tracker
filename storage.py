import json
import os

FILE_NAME = "books.json"


def load_books():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_book(book):
    books = load_books()

    # Проверка дубликатов
    for existing_book in books:
        if (
            existing_book["author"].lower() == book["author"].lower()
            and existing_book["title"].lower() == book["title"].lower()
        ):
            print("Такая книга уже существует.")
            return

    books.append(book)
    save_books(books)
    print("Книга добавлена.")


def delete_book(title):
    books = load_books()

    updated_books = [
        book for book in books
        if book["title"].lower() != title.lower()
    ]

    if len(updated_books) == len(books):
        print("Книга не найдена.")
    else:
        save_books(updated_books)
        print("Книга удалена.")