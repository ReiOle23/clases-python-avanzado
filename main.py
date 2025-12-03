import argparse
from models import Library, User, Book
from controllers import LibraryService, BookService, Database

# This project is a Library manager. 
# The cli can be used in so many different libraries
# There are superadmins and users, which can interact with the program.
# Superadmins can create new library, add books to a library and create users.
# Users can search a book from a library and loan it if its available.

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='library_loan')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Superadmin: Add Library
    add_library_parser = subparsers.add_parser('add-library', help='As a superadmin, add a library')
    add_library_parser.add_argument('name', help='Library name')
    add_library_parser.add_argument('location', help='Library location')
    
    # Superadmin: Add Book
    add_book_parser = subparsers.add_parser('add-book', help='As a superadmin, register new book')
    add_book_parser.add_argument('title', help='Book title')
    add_book_parser.add_argument('author', help='Book author')
    add_book_parser.add_argument('--isbn', help='Book ISBN (optional)')
    
    # Superadmin: Add User
    add_user_parser = subparsers.add_parser('add-user', help='As a superadmin, register new user')
    add_user_parser.add_argument('username', help='Username')
    add_user_parser.add_argument('email', help='User email')
    
    # User: Search Book
    search_book_parser = subparsers.add_parser('search-book', help='User can search for a book')
    search_book_parser.add_argument('query', help='Search query (title or author)')
    
    # User: Loan Book
    loan_book_parser = subparsers.add_parser('loan-book', help='User can loan a book')
    loan_book_parser.add_argument('book_id', help='Book ID to loan')
    loan_book_parser.add_argument('user_id', help='User ID')
    
    args = parser.parse_args()
    if args.command == 'add-library':
        print(f"Adding library: {args.name} at {args.location}")
        LibraryService().create_library(args.name, args.location)
        # library = Library(name=args.name, location=args.location)
        # LibraryService.add_library(library)
        
    elif args.command == 'add-book':
        print(f"Adding book: {args.title} by {args.author}")
        # book = Book(title=args.title, author=args.author, isbn=args.isbn)
        # BookService.add_book(book)
        
    elif args.command == 'add-user':
        print(f"Adding user: {args.username} ({args.email})")
        # user = User(username=args.username, email=args.email)
        # Database.add_user(user)
        
    elif args.command == 'search-book':
        print(f"Searching for: {args.query}")
        # BookService.search(args.query)
        
    elif args.command == 'loan-book':
        print(f"Loaning book {args.book_id} to user {args.user_id}")
        # BookService.loan(args.book_id, args.user_id)
        
    else:
        parser.print_help()
        
        
        
# patron monolitos
# Arquitecture
# .
# └── software_biblioteca/
#     ├── .env
#     ├── config.ini
#     ├── biblioteca/
#     │   ├── __init__.py
#     │   ├── config.py
#     │   ├── domain/
#     │   │   ├── __init__.py
#     │   │   └── models.py
#     │   ├── repository/
#     │   │   ├── __init__.py
#     │   │   ├── interfaces.py
#     │   │   └── json_repo.py
#     │   ├── services/
#     │   │   ├── __init__.py
#     │   │   └── book_service.py
#     │   └── adapters/
#     │       ├── __init__.py
#     │       └── cli.py
#     ├── data/
#     │   └── database.json
#     └── tests/
#         ├── __init__.py
#         ├── conftest.py
#         ├── test_repository.py
#         └── test_services.py
