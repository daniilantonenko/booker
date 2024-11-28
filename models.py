import json
from typing import List

class Book:
    """Класс для представления книги."""
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        return {
            "id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict):
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )


class Library:
    """Класс для управления библиотекой."""
    DATA_FILE = "data/books.json"

    def __init__(self):
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        """Загружает книги из файла JSON."""
        try:
            with open(self.DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        """Сохраняет книги в файл JSON."""
        with open(self.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет новую книгу."""
        new_id = max((book.book_id for book in self.books), default=0) + 1
        book = Book(new_id, title, author, year)
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id: int):
        """Удаляет книгу по ID."""
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def find_books(self, query: str, field: str) -> List[Book]:
        """Ищет книги по указанному полю."""
        field_map = {"title": "title", "author": "author", "year": "year"}
        if field not in field_map:
            raise ValueError("Недопустимое поле для поиска.")
        return [book for book in self.books if query.lower() in str(getattr(book, field)).lower()]

    def change_status(self, book_id: int, new_status: str):
        """Изменяет статус книги."""
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                break
        else:
            raise ValueError("Книга с таким ID не найдена.")
        self.save_books()

    def list_books(self) -> List[Book]:
        """Возвращает список всех книг."""
        return self.books