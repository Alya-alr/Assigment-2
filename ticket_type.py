class TicketType:
    def __init__(self, name):
        # Initialize the TicketType object with the provided name
        self.name = name

    def __str__(self):
        # Return the name of the ticket type when the object is converted to a string
        return self.name