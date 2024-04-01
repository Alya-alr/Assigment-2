class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        # Initialize the Artwork object with the provided attributes
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

    def display(self):
        # Display information about the artwork
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Date of Creation: {self.date_of_creation}")
        print(f"Historical Significance: {self.historical_significance}")
        print(f"Location: {self.location}")