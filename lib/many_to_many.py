class Author:
    
    all = []

    def __init__(self, name):
        
        self.name = name
        self.contract_list = []
        self.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
       return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total      

class Book:
    
    all = []

    def __init__(self, title):
        
        self.title = title
        self.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
    
        self.author = author
        self.book = book
        self.date = date       
        self.royalties = royalties
        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        
        contracts = [contract for contract in cls.all if contract.date == date]
        return sorted(contracts, key=lambda x: x.date)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Invalid author")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise ValueError("Invalid book")

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise ValueError("Invalid date")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise ValueError("Invalid royalties")
        