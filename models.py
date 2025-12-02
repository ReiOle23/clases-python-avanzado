from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    id: int
    name: str
    surnames: str
    
@dataclass
class Book:
    id: int
    title: str
    author: str
    loan_date: date
    loaned_to: User
    
    def set_loan(self, user:User, date_until: date):
        self.loan_date = date_until
        self.loaned_to = user

@dataclass
class Library:
    id: int
    books: dict
    