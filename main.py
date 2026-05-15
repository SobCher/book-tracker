from models import Book
from storage import load_books, add_book, delete_book
from stats import average_rating, author_statistics


def show_menu():
    print("\n=== Трекер прочитанных книг ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")


def add_new_book():
    author = input("Автор: ")
    title = input("Название: ")

    while True:
        try:
            rating = int(input("Оценка (1-5): "))

            if 1 <= rating <= 5:
                break

            print("Оценка должна быть от 1 до 5.")

        except ValueError:
            print("Введите число.")

    read_date = input("Дата прочтения: ")

    book = Book(author, title, rating, read_date)

    add_book(book.to_dict())


def show_books():
    books = load_books()

    if not books:
        print("Список книг пуст.")
        return

    for index, book in enumerate(books, start=1):
        print(
            f"{index}. {book['author']} — "
            f"{book['title']} | "
            f"Оценка: {book['rating']} | "
            f"Дата: {book['read_date']}"
        )


def show_average_rating():
    books = load_books()
    avg = average_rating(books)

    print(f"Средняя оценка: {avg:.2f}")


def show_author_stats():
    books = load_books()
    stats = author_statistics(books)

    if not stats:
        print("Нет данных.")
        return

    for author, count in stats.items():
        print(f"{author}: {count} книг")


def main():
    while True:
        show_menu()

        choice = input("Выберите пункт: ")

        if choice == "1":
            add_new_book()

        elif choice == "2":
            show_books()

        elif choice == "3":
            show_average_rating()

        elif choice == "4":
            show_author_stats()

        elif choice == "5":
            title = input("Введите название книги: ")
            delete_book(title)

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()