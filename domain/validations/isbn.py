class IsbnValidator:
    def __init__(self, isbn):
        self.isbn = isbn
    
    def has_valid_len(self):
        return len(self.isbn) in (10,13)
    
    def is_numeric(self):
        return self.isbn.isnumeric()

    def is_valid_isbn(self):
        return (
            self.has_valid_len()
            and self.is_numeric()
        )