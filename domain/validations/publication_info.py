#Validator for all publication info is correct
# ADD REFERENCE-BACKEND VALIDATION FOR COUNTRY INPUT

class PublicationValidator:
    def __init__(self, country, publisher, year):
        self.country = country
        self.publisher = publisher
        self.year = year

    def is_valid_country(self):
        return (self.country).isalpha()
            
    def has_valid_year(self):
        return (self.year).isnumeric() and (int(self.year) in range(1800,2026))
      
    
    def is_valid_publisher(self):
        return (self.publisher).isalpha()

    def is_valid_publication(self):
        return(
            self.is_valid_country()
            and self.has_valid_year()
            and self.is_valid_publisher()
        )