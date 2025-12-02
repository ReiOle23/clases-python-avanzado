from dataclasses import dataclass

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
    loan_date: str
    loaned_to: User
    
@dataclass
class Library:
    id: int
    books: dict
    