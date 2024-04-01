class Ticket:
    def __init__(self, ticket_type, price, validity):
        # Initialize the Ticket object with the provided attributes
        self.ticket_type = ticket_type
        self.price = price
        self.validity = validity

    def calculate_price(self):
        # Calculate the price of the ticket
        return self.price

    def display(self):
        # Display information about the ticket
        print(f"Ticket Type: {self.ticket_type}")
        print(f"Price: {self.price}")
        print(f"Validity: {self.validity}")