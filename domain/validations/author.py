# Validator for both Authors before constructing the object

class AuthorValidator:
    def __init__(self, auth):
        self.auth = auth
    
    def is_valid_author(self):
        auth = self.auth.strip().replace("-", " ")
        if auth.isalpha():
            return True
        else:
            return False

