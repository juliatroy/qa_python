# qa_python
Hello there,

My name is Julia Troy (Smoliy) and here's my Yandex.Practicum project for Sprint 4 "Unit Testing".

The list of test methods that can be found in test.py is the following:
* test_add_new_book_add_two_books_total_two_books_added - pre-coded test, that initially was not running. I've updates one of the methods' names to make it work.
* test_add_new_book_add_same_book_twice_total_one_book_added - adds the same book twice, expects that it is added just once;
* test_add_new_book_add_book_name_longer_than_40_symbols_no_book_added - adds a book with a name which is longer than 40 symbols threshold set for a book name.
* test_add_book_set_genre_for_existent_genre_name_genre_is_set - parametrized set that adds a book and sets a genre for each genre available;
* test_set_book_genre_for_non_existent_genre_name_genre_not_set - adds a book and attempts to set a genre that is not listed in genres list;
* test_get_books_with_specific_genre_book_library_contains_one_book_per_genre - uses fixture that adds a books library, which contains 1 book per genre;
* test_get_books_for_children_book_library_contains_3items - uses fixture, checks that books library contains 3 items belonging to children books list;
* test_get_books_for_children_book_library_contains_no_rating_books - uses fixture, checks tht there are no rating books among children books list;
* test_delete_book_from_favorites_makes_book_deleted - adds and deletes a book from favorites;
* test_add_book_to_favorites_twice_books_added_once - adds a single book to favorites twice, expects it to be listed among favorites only once;