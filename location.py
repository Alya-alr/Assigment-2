class Location:
    def __init__(self, name):
        # Initialize the Location object with the provided name
        self.name = name

    def __str__(self):
        # Return the name of the location when the object is converted to a string
        return self.name