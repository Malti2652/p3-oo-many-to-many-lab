# class Author:
#     pass
class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)




# class Book:
#     pass
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]





# class Contract:
#     pass
class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        self.author._contracts.append(self)
        self.book._contracts.append(self)
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]




