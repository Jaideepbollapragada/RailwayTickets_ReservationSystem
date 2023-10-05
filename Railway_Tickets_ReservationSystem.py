# Import the 'random' module for generating random numbers
import random

# Define a class 'Account' to represent user accounts


class Account():
    # Constructor: Initialize the account with a username and password
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Method to check if the entered password matches the account's password
    def check_password(self, password):
        return self.password == password

# Define a class 'Train' to represent train details


class Train:
    # Constructor: Initialize the train with train number, source, destination, and total seats
    def __init__(self, train_number, source, destination, total_seats):
        self.train_number = train_number
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats  # Initially, all seats are available

# Define a class 'Passenger' to represent passenger information


class Passenger:
    # Constructor: Initialize the passenger with a name, age, and train number
    def __init__(self, name, age, train_number):
        self.name = name
        self.age = age
        self.train_number = train_number

# Define a class 'Ticket' to represent a booked ticket


class Ticket:
    # Constructor: Initialize the ticket with a PNR (Passenger Name Record) and a passenger reference
    def __init__(self, pnr, passenger):
        self.pnr = pnr
        self.passenger = passenger


# Create an empty list to store user accounts
accounts = []

# Create a list of available train objects with initial details
trains = [
    Train("12345", "New York", "Chicago", 50),
    Train("67890", "Chicago", "Los Angeles", 75),
    Train("54321", "Los Angeles", "San Francisco", 60)
]

# Create an empty list to store booked tickets
tickets = []

# Initialize a variable to keep track of the currently logged-in user
login_account = None

# Function to create a user account


def create_account():
    username = input("Enter username: ")  # Prompt the user to enter a username
    password = input("Enter password: ")  # Prompt the user to enter a password
    # Create an 'Account' object and add it to the 'accounts' list
    accounts.append(Account(username, password))
    print("Account created successfully.")  # Print a success message

# Function to log in


def login():
    global login_account  # Use the global 'login_account' variable
    username = input("Enter username: ")  # Prompt the user to enter a username
    password = input("Enter password: ")  # Prompt the user to enter a password
    for account in accounts:  # Iterate through the list of accounts
        # Check if username and password match
        if account.username == username and account.check_password(password):
            login_account = account  # Set the logged-in account
            # Print a success message
            print(f"{username} is logged in successfully.")
            return
    # Print an error message if login fails
    print("Invalid username or password.")

# Function to display available trains


def display_trains():
    print("\nTrains Available:")  # Print a header
    for train in trains:  # Iterate through the list of trains
        print(f"Train Number: {train.train_number}")  # Print train number
        print(f"Source: {train.source}")  # Print source
        print(f"Destination: {train.destination}")  # Print destination
        # Print available seats
        print(f"Available Seats: {train.available_seats}")
        print("---------------")  # Print a separator

# Function to book tickets


def book_tickets():
    if login_account is None:  # Check if a user is logged in
        # Print an error message
        print("You must be logged in to book tickets.")
        return

    # Prompt the user to enter a train number
    train_number = input("Enter Train Number: ")
    # Find the selected train
    train = next((t for t in trains if t.train_number == train_number), None)

    if train:
        if train.available_seats > 0:  # Check if there are available seats on the selected train
            # Prompt for the number of tickets
            num_tickets = int(input("Enter the number of tickets to book: "))
            if num_tickets <= train.available_seats:  # Check if there are enough available seats
                for _ in range(num_tickets):  # Loop to book multiple tickets
                    # Prompt for passenger name
                    name = input("Enter Passenger Name: ")
                    # Prompt for passenger age
                    age = input("Enter Passenger Age: ")
                    # Create a 'Passenger' object
                    passenger = Passenger(name, age, train_number)
                    pnr = generate_random_pnr()  # Generate a random PNR
                    ticket = Ticket(pnr, passenger)  # Create a 'Ticket' object
                    train.available_seats -= 1  # Decrease the available seats on the train
                    # Add the booked ticket to the 'tickets' list
                    tickets.append(ticket)

                    # Set the train_number attribute for the logged-in user
                    login_account.train_number = train_number

                    # Print a success message
                    print(f"Ticket booked successfully. PNR: {pnr}")
            else:
                # Print an error message
                print("Not enough available seats on this train.")
        else:
            # Print an error message
            print("No available seats on this train.")
    else:
        # Print an error message if the train is not found
        print(f"Train {train_number} not found.")

# Function to view booked tickets for the logged-in user


def view_booked_tickets():
    if login_account is None:  # Check if a user is logged in
        # Print an error message
        print("You must be logged in to view booked tickets.")
        return

    print("\nBooked Tickets:")  # Print a header
    booked_tickets = [ticket for ticket in tickets if ticket.passenger.train_number ==
                      login_account.train_number]  # Filter booked tickets for the logged-in user
    if not booked_tickets:  # Check if there are no booked tickets
        print("No booked tickets found.")  # Print a message
    else:
        for ticket in booked_tickets:  # Iterate through booked tickets
            # Get the train number from the ticket
            train_number = ticket.passenger.train_number
            # Find the corresponding train
            train = next(
                (t for t in trains if t.train_number == train_number), None)
            if train:  # Check if the train is found
                print(f"PNR: {ticket.pnr}")  # Print the PNR
                # Print train number
                print(f"Train Number: {train.train_number}")
                print(f"Source: {train.source}")  # Print source
                print(f"Destination: {train.destination}")  # Print destination
                # Print passenger name
                print(f"Passenger Name: {ticket.passenger.name}")
                # Print passenger age
                print(f"Passenger Age: {ticket.passenger.age}")
                print("---------------")  # Print a separator

# Function to generate a random PNR number


def generate_random_pnr():
    # Generate a random integer between 100000 and 999999
    return random.randint(100000, 999999)


# Main loop
while True:
    print("\nMenu:")  # Print the menu
    print("1. Create Account")  # Print the option to create an account
    print("2. Login")  # Print the option to log in
    print("3. Display Trains")  # Print the option to display available trains
    print("4. Book Tickets")  # Print the option to book tickets
    print("5. View Booked Tickets")  # Print the option to view booked tickets
    print("6. Exit")  # Print the option to exit
    # Prompt the user to enter their choice
    choice = input("Enter your choice: ")

    if choice == "1":  # If the choice is "1"
        create_account()  # Call the 'create_account' function
    elif choice == "2":  # If the choice is "2"
        login()  # Call the 'login' function
    elif choice == "3":  # If the choice is "3"
        display_trains()  # Call the 'display_trains' function
    elif choice == "4":  # If the choice is "4"
        book_tickets()  # Call the 'book_tickets' function
    elif choice == "5":  # If the choice is "5"
        view_booked_tickets()  # Call the 'view_booked_tickets' function
    elif choice == "6":  # If the choice is "6"
        break  # Exit the loop to end the program
    else:
        # Print an error message for an invalid choice
        print("Invalid choice. Please try again.")
