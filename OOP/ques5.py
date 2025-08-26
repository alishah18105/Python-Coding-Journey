#Write a class Train which has methods to book a ticket, get the status (number of seats), and get fare information 
# of trains running under Pakistan Railways.

import random


class Train:
    def __init__(self, name, total_seats, frm, to):
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.frm = frm
        self.to = to

    def book_ticket(self, number_of_tickets):
        if number_of_tickets <= self.available_seats:
            self.available_seats -= number_of_tickets
            print(f"{number_of_tickets} ticket(s) booked successfully on {self.name} From {self.frm} To {self.to}.")
        else:
            print(f"Only {self.available_seats} seat(s) available. Cannot book {number_of_tickets} ticket(s).")

    def get_status(self):
        print(f"Train: {self.name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")

    def get_fare_info(self):
        print(f"Fare per ticket of {self.name}: Pkr {random.randint(7000,15000)}")

book_ticket = Train("Business Express", 100, "Karachi", "Lahore")
book_ticket.book_ticket(5)
book_ticket.get_status()
book_ticket.get_fare_info() 
