class SpecsValidator:
    def __init__(self, pages, height):
        self.pages = pages
        self.height = height

    def specs_are_valid(self):
        if (self.pages).isnumeric() and (self.height).isnumeric():
            return True 
        else:
            return False