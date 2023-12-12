import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books_total_two_books_added(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_same_book_twice_total_one_book_added(self):
        collector = BooksCollector()

        new_book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(new_book)
        collector.add_new_book(new_book)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book', [
        'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции',
        'Алиса в Стране Чудес, Или Странствие в Странную Страну по страницам престранной пространной истории',
        'Мне бы хотелось, чтоб меня кто-нибудь где-нибудь ждал… (сборник)'
    ])
    def test_add_new_book_add_book_name_longer_than_40_symbols_no_book_added(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 0

    def test_add_book_library_adds_5items(self, book_library):
        collector = BooksCollector()

        for book, genre in book_library:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert len(collector.get_books_genre()) == 5

    @pytest.mark.parametrize('book,book_genre',
                             [
                                 ["Автостопом по галактике", "Фантастика"],
                                 ["Пила", "Ужасы"],
                                 ["Убийство в Восточном экспрессе", "Детективы"],
                                 ["Ведьма-хранительница", "Комедии"],
                                 ['Домовенок Кузя', 'Мультфильмы']
                             ])
    def test_add_book_set_genre_for_existent_genre_name_genre_is_set(self, book, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, book_genre)

        assert len(collector.get_books_genre()) == 1 and collector.get_books_genre().get(book) == book_genre

    def test_set_book_genre_for_non_existent_genre_name_genre_not_set(self):
        collector = BooksCollector()

        book = 'Русские народные сказки'
        book_genre = 'Сказки'
        collector.add_new_book(book)
        collector.set_book_genre(book, book_genre)

        assert len(collector.get_books_genre()) == 1 and collector.get_book_genre(book) == ''

    def test_get_books_with_specific_genre_book_library_contains_one_book_per_genre(self, filled_book_collector):
        for genres in filled_book_collector.genre:
            assert len(filled_book_collector.get_books_with_specific_genre(genres)) == 1

    def test_get_books_for_children_book_library_contains_3items(self, filled_book_collector):
        assert len(filled_book_collector.get_books_for_children()) == 3

    def test_get_books_for_children_book_library_contains_no_rating_books(self, filled_book_collector):
        for age_rating_genre in filled_book_collector.genre_age_rating:
            assert (filled_book_collector.get_books_with_specific_genre(age_rating_genre)
                    not in filled_book_collector.get_books_for_children())

    def test_delete_book_from_favorites_makes_book_deleted(self, fantasy):
        collector = BooksCollector()

        for book in fantasy:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        collector.delete_book_from_favorites(fantasy[0])

        assert (len(collector.get_list_of_favorites_books()) == 1
                and fantasy[0] not in collector.get_list_of_favorites_books()
                and fantasy[1] in collector.get_list_of_favorites_books())

    def test_add_book_to_favorites_twice_books_added_once(lib):
        collector = BooksCollector()

        favorite_book = 'Гиперион'
        collector.add_new_book(favorite_book)

        collector.add_book_in_favorites(favorite_book)
        collector.add_book_in_favorites(favorite_book)

        assert (len(collector.get_list_of_favorites_books()) == 1
                and favorite_book in collector.get_list_of_favorites_books())
