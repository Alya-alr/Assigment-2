class SpecialEvent:
    def __init__(self, name, location, duration):
        # Initialize the SpecialEvent object with the provided attributes
        self.name = name
        self.location = location
        self.duration = duration

    def display(self):
        # Display information about the special event
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Duration: {self.duration}")