class SpecsValidator:
    def __init__(self, pages, height):
        self.pages = pages
        self.height = height
    
    def is_valid_pages(self):
        if self.pages.isnumeric():
            return True
        else:
            return False
        
    def is_valid_height(self):
        if int(self.height) in range(5,60):
            return True
        else:
            return False
        
    def specs_are_valid(self):
        return(
            self.is_valid_height()
            and self.is_valid_pages()
        )
