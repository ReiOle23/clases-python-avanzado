from datetime import date
from dateutil.relativedelta import relativedelta
from models import Library, User, Book

class BookService:
    def __init__(self, instance:Book):
        self.instance = instance
    
    def set_new_loan(self, user:User, date_until: date):
        self.instance.set_loan(user,date_until)
        

class LibraryService:
    def __init__(self, instance:Library):
        self.instance = instance
        
    def get_book(self, id:int) -> Book:
        return self.instance.books.get(id,None)
    
    def add_book(self, book: Book):
        self.instance.books[book.id] = book
        
    def _get_loan_new_date(self) -> date:
        today = date.today()
        next_month = today + relativedelta(months=1)
        return next_month
        
    def loan_book(self, user:User, id:int) -> Book:
        book_to_loan = self.instance.books.get(id,None)
        if not book_to_loan:
            return Exception("This book is not on the library")
        book_to_loan.set_loan(user,self._get_loan_new_date())
        return book_to_loan
    