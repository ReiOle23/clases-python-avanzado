import pytest
from models import Library, User, Book
from controllers import LibraryService, BookService

    
@pytest.fixture
def library():
    instance = Library(1,{})
    return LibraryService(instance)

@pytest.fixture
def user():
    return User(1,"Julia","Gutierrez")

@pytest.fixture
def lotr_book():
    instance = Book(2,"Lord of the rings","JRR Tolkien",None,None)
    return BookService(instance)
        
def test_library_has_no_book(library, lotr_book):
    assert library.get_book(lotr_book.instance.id) is None
    
def test_library_has_book(library, lotr_book):
    library.add_book(lotr_book.instance)
    book_obj = library.get_book(lotr_book.instance.id)
    assert book_obj is not None
    assert book_obj.id == lotr_book.instance.id
    
def test_user_loan_book(library, lotr_book, user):
    library.add_book(lotr_book.instance)
    book_obj = library.loan_book(user, lotr_book.instance.id)
    assert book_obj.id == lotr_book.instance.id
    assert book_obj.loaned_to == user
    