import pytest

from main import BooksCollector


@pytest.fixture
def book_library():
    lib = [
        ["Мир-кольцо", "Фантастика"],
        ["Голодный дом", "Ужасы"],
        ["Десять негритят", "Детективы"],
        ["12 стульев", "Комедии"],
        ['Сказка о царе Салтане', 'Мультфильмы']
    ]
    return lib


@pytest.fixture
def filled_book_collector(book_library):
    collector = BooksCollector()

    for book, genre in book_library:
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

    return collector


@pytest.fixture
def fantasy():
    fantasy_names = (
        'Нейромант',
        'Дюна'
    )
    return fantasy_names
