from artwork import Artwork
from exhibition import Exhibition
from location import Location
from special_event import SpecialEvent
from ticket import Ticket
from tour import Tour
from visitor import Visitor


def main():
    # Create some sample data
    louvre = Location("Louvre Museum")
    mona_lisa = Artwork("Mona Lisa", "Leonardo da Vinci", "1503-1506", "Renaissance portrait", louvre)
    expo_1 = Exhibition("Expo 1", louvre, "1 week")
    tour_1 = Tour("2024-04-01", 20, "Guide 1")
    event_1 = SpecialEvent("Concert", louvre, "2 hours")

    # User input for ticket purchase
    visitor_name = input("Enter visitor name: ")
    visitor_age = int(input("Enter visitor age: "))
    ticket_type = input("Enter ticket type (Adult/Child/Student/Senior/Group/Special): ")

    # Assume visitor ID card check is performed elsewhere in the system to determine ticket type
    if ticket_type in ["Adult", "Child", "Student", "Senior"]:
        ticket_price = 63.00
    elif ticket_type == "Group":
        ticket_price = 63.00 / 2  # 50% discount for groups
    elif ticket_type == "Special":
        ticket_price = float(input("Enter ticket price for special event: "))
    else:
        print("Invalid ticket type entered.")
        return

    # Calculate total price with VAT
    total_price = ticket_price * 1.05

    # Create a ticket object
    ticket = Ticket(ticket_type, total_price, "1 day")

    # Display ticket information
    ticket.display()


if __name__ == "__main__":
    main()
