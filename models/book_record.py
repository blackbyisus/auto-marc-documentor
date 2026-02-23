from models.authors import Authors
from models.publication_info import PublicationInfo
from models.specifications import Specification


class BookRecord:
    def __init__(self, title, isbn, authors: Authors, publication: PublicationInfo, specs: Specification):
        self.title = title
        self.isbn = isbn
        self.authors = authors
        self.publication= publication
        self.specs = specs



