class Visitor:
    def __init__(self, name, age, nationality):
        # Initialize the Visitor object with the provided attributes
        self.name = name
        self.age = age
        self.nationality = nationality

    def display(self):
        # Display information about the visitor
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Nationality: {self.nationality}")
