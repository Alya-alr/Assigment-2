import tkinter as tk
from tkinter import messagebox

def purchase_ticket():
    # Create a new window
    purchase_window = tk.Toplevel(root)
    purchase_window.title("Purchase Ticket")

    # Add labels and entry fields for user input
    tk.Label(purchase_window, text="Visitor Name:").pack()
    visitor_name_entry = tk.Entry(purchase_window)
    visitor_name_entry.pack()

    tk.Label(purchase_window, text="Visitor Age:").pack()
    visitor_age_entry = tk.Entry(purchase_window)
    visitor_age_entry.pack()

    tk.Label(purchase_window, text="Ticket Type:").pack()
    ticket_type_entry = tk.Entry(purchase_window)
    ticket_type_entry.pack()

    def process_purchase():
        visitor_name = visitor_name_entry.get()
        visitor_age = int(visitor_age_entry.get())
        ticket_type = ticket_type_entry.get()

        # Process ticket purchase (add your logic here)
        # This is where you would calculate the ticket price, display a receipt, etc.
        # For now, just display a message box with the entered information
        messagebox.showinfo("Ticket Purchase", f"Visitor Name: {visitor_name}\nVisitor Age: {visitor_age}\nTicket Type: {ticket_type}")

        # Close the purchase window after processing
        purchase_window.destroy()

    # Add a button to submit the ticket purchase
    tk.Button(purchase_window, text="Purchase Ticket", command=process_purchase).pack()

# Create the main application window
root = tk.Tk()
root.title("Museum Ticketing System")

# Add a button to open the ticket purchase form
tk.Button(root, text="Purchase Ticket", command=purchase_ticket).pack()

# Start the Tkinter event loop
root.mainloop()
