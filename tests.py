import unittest
from models import Library, Book


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Инициализация перед каждым тестом."""
        self.library = Library()
        # Заменяем реальные данные тестовыми
        self.library.books = [
            Book(1, "Книга 1", "Автор 1", 2000, "в наличии"),
            Book(2, "Книга 2", "Автор 2", 2005, "выдана"),
            Book(3, "Книга 3", "Автор 3", 2010, "в наличии"),
        ]

    def test_add_book(self):
        """Проверка добавления книги."""
        self.library.add_book("Книга 4", "Автор 4", 2020)
        self.assertEqual(len(self.library.books), 4)
        self.assertEqual(self.library.books[-1].title, "Книга 4")

    def test_remove_book(self):
        """Проверка удаления книги."""
        self.library.remove_book(1)
        self.assertEqual(len(self.library.books), 2)
        self.assertFalse(any(book.book_id == 1 for book in self.library.books))

    def test_find_books(self):
        """Проверка поиска книг."""
        result = self.library.find_books("Книга 1", "title")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].author, "Автор 1")

    def test_change_status(self):
        """Проверка изменения статуса книги."""
        self.library.change_status(2, "в наличии")
        book = next(book for book in self.library.books if book.book_id == 2)
        self.assertEqual(book.status, "в наличии")

    def test_list_books(self):
        """Проверка списка всех книг."""
        books = self.library.list_books()
        self.assertEqual(len(books), 3)
        self.assertEqual(books[0].title, "Книга 1")

    def test_invalid_remove_book(self):
        """Проверка удаления несуществующей книги."""
        if not any(book.book_id == book_id for book in self.books):
            raise ValueError("Книга с таким ID не найдена.")
        with self.assertRaises(ValueError):
            self.library.remove_book(99)

    def test_invalid_change_status(self):
        """Проверка изменения статуса несуществующей книги."""
        with self.assertRaises(ValueError):
            self.library.change_status(99, "в наличии")


if __name__ == "__main__":
    unittest.main()
