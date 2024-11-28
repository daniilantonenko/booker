from models import Library

def main():
    library = Library()

    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Изменить статус книги")
        print("5. Показать все книги")
        print("6. Выход")
        choice = input("Выберите действие (1-6): ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания книги: "))
                library.add_book(title, author, year)
                print("Книга успешно добавлена!")
            elif choice == "2":
                book_id = int(input("Введите ID книги для удаления: "))
                library.remove_book(book_id)
                print("Книга успешно удалена!")
            elif choice == "3":
                field = input("Введите поле для поиска (title, author, year): ").lower()
                query = input("Введите значение для поиска: ")
                found_books = library.find_books(query, field)
                if found_books:
                    print("Найденные книги:")
                    for book in found_books:
                        print(book.to_dict())
                else:
                    print("Книги не найдены.")
            elif choice == "4":
                book_id = int(input("Введите ID книги для изменения статуса: "))
                new_status = input("Введите новый статус (в наличии/выдана): ")
                library.change_status(book_id, new_status)
                print("Статус книги успешно изменён!")
            elif choice == "5":
                books = library.list_books()
                if books:
                    print("Список книг:")
                    for book in books:
                        print(book.to_dict())
                else:
                    print("Библиотека пуста.")
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()
