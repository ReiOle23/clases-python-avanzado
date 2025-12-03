from datetime import date
from dateutil.relativedelta import relativedelta
from models import Library, User, Book
from dataclasses import asdict
import json
from typing import TypeVar
from contextlib import contextmanager

T_model = TypeVar("Model", User,Book,Library)

class Database:
    database_file = 'database.json'
    
    @classmethod
    @contextmanager
    def using_database(cls, filename: str):
        original_file = cls.database_file
        cls.database_file = filename
        try:
            yield
        finally:
            cls.database_file = original_file
            
    @classmethod
    def generate_id_from(cls, _class:T_model):
        model_type = _class.__name__
        with open(cls.database_file, "r") as json_file:
            data = json.load(json_file)
        objects = list(data[model_type])
        last_id = int(objects[-1])+1 if objects else 1
        return last_id
        
    
    @classmethod
    def clear(cls):
        with open(cls.database_file, "w") as json_file:
            data = {
                "User":{},
                "Book":{},
                "Library":{}
            }
            json.dump(data, json_file, indent=4)
            
    @classmethod
    def get_obj(cls, model_type:str ,id:int):
        with open(cls.database_file, "r") as json_file:
            data = json.load(json_file)
        return data[model_type][str(id)]
    
    @classmethod
    def save_obj(cls, obj:T_model):
        model_type = type(obj).__name__ 
        with open(cls.database_file, "r") as json_file:
            data = json.load(json_file)
        
        data[model_type][str(obj.id)] = asdict(obj)
        with open(cls.database_file, 'w') as json_file:
            json.dump(data, json_file, indent=4)

class BookService:
    def __init__(self, id:int):
        self.instance = Book(**Database.get_obj("Book", id))
        
    def set_new_loan(self, user:User, date_until: date):
        self.instance.loan_date = date_until.isoformat()
        self.instance.loaned_to = user
        Database.save_obj(self.instance)
        

class LibraryService:
        
    def get_library(self, id:int):
        return Library(**Database.get_obj("Library", id))
        
    def create_library(self, name:str, location:str):
        new_id = Database.generate_id_from(Library)
        Database.save_obj(Library(new_id, name, location))
        
    def get_book(self, id:int) -> Book:
        return self.instance.books.get(id,None)
    
    def add_book(self, book: Book):
        self.instance.books[book.id] = book
        Database.save_obj(self.instance)
        
    def _get_loan_new_date(self) -> date:
        today = date.today()
        next_month = today + relativedelta(months=1)
        return next_month
        
    def loan_book(self, user:User, id:int) -> Book:
        book_to_loan = BookService(id)
        if not book_to_loan:
            return Exception("This book is not on the library")
        book_to_loan.set_new_loan(user,self._get_loan_new_date())
        return book_to_loan
    