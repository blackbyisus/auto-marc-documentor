# Validatoor for both Authors before constructing the object

class AuthorsValidator:
    def __init__(self, main_auth, secondary_auth):
        self.main_auth = main_auth
        self.secondary_auth = secondary_auth
    
    def authors_are_valid(self):
        main_auth = self.main_auth.strip().replace("-"," ")
        secondary_auth = self.secondary_auth.strip().replace("-", " ")
        if main_auth.isalpha() and secondary_auth.isalpha():
            return True
        else:
            return False


    