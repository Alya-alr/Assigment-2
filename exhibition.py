class Exhibition:
    def __init__(self, name, location, duration):
        # Initialize the Exhibition object with the provided attributes
        self.name = name
        self.location = location
        self.duration = duration

    def display(self):
        # Display information about the exhibition
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration}")