from domain.validations.isbn import IsbnValidator
from domain.validations.publication_info import PublicationValidator

def main():

    title = "DEEZ NUTS"
    isbn = "2737637531235"
    authors = ("Jesus", "Bob")
    year = "1800"
    publisher = "Cengage"
    country = "México"
    specs = ("123 pg", "23cm")
    isbnvalidator = IsbnValidator(isbn)
    publication_validator = PublicationValidator(country, publisher, year)
    print(publication_validator.is_valid_publication())
    print(isbnvalidator.is_valid_isbn())
    
main()
