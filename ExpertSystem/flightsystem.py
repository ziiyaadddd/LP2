from datetime import datetime, timedelta
import uuid

class Flight:
    def __init__(self, flight_number, departure, arrival, date):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.date = date

class Cargo:
    def __init__(self, cargo_id, origin, destination, weight, flight_number, price):
        self.cargo_id = cargo_id
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.flight_number = flight_number
        self.price = price

class AirlineSystem:
    def __init__(self):
        self.flights = []
        self.cargos = []
        self.cargo_weight_limit = 100  # Setting cargo weight limit

    def add_flight(self, flight_number, departure, arrival, date):
        flight = Flight(flight_number, departure, arrival, date)
        self.flights.append(flight)

    def add_cargo(self, cargo_id, origin, destination, weight, flight_number, price):
        cargo = Cargo(cargo_id, origin, destination, weight, flight_number, price)
        self.cargos.append(cargo)

    def display_flights(self, departure, arrival):
        print(f"Available Flights from {departure} to {arrival}:")
        available_flights = [flight for flight in self.flights if flight.departure.lower() == departure and flight.arrival.lower() == arrival]
        if available_flights:
            for idx, flight in enumerate(available_flights, start=1):
                print(f"{idx}. Flight Number: {flight.flight_number}, Date: {flight.date}")
        else:
            print("No available flights for the selected route.")

    def get_cargo_price(self, origin, destination, weight):
        return 20 * weight

    def generate_cargo_id(self):
        return str(uuid.uuid4().hex)[:6]

    def ship_cargo(self):
        print("\nCargo Shipment:")
        origin = self.validate_location("Enter origin location: ")
        destination = self.validate_location("Enter destination location: ")
        weight = float(input("Enter weight (in kg): "))

        if weight > self.cargo_weight_limit:
            print("Cargo weight exceeds the limit. Please choose a lower weight.")
            return

        price = self.get_cargo_price(origin, destination, weight)
        print(f"Price for shipping cargo from {origin} to {destination} with weight {weight} kg: ${price}")

        self.display_flights(origin, destination)

        flight_choice = self.validate_flight_choice("Enter the number of the flight you choose: ", origin, destination)
        selected_flight = [flight for flight in self.flights if flight.departure.lower() == origin and flight.arrival.lower() == destination][flight_choice - 1]

        # Increase price by $30 for the earliest flight
        if selected_flight == min(self.flights, key=lambda x: x.date):
            price += 30
            print("Price increased by $30 for the earliest flight.")

        cargo_id = self.generate_cargo_id()
        self.add_cargo(cargo_id, origin, destination, weight, selected_flight.flight_number, price)
        print(f"Your cargo with ID {cargo_id} has been confirmed for shipment on flight {selected_flight.flight_number}.")

    def validate_location(self, message):
        while True:
            location = input(message).strip().lower()
            if location in ['usa', 'uk', 'china', 'japan', 'indonesia', 'malaysia', 'singapore', 'qatar', 'india', 'france', 'spain']:
                return location
            else:
                print("Wrong input. Please enter a valid location.")

    def validate_flight_choice(self, message, origin, destination):
        available_flights = [flight for flight in self.flights if flight.departure.lower() == origin and flight.arrival.lower() == destination]
        while True:
            try:
                flight_choice = int(input(message))
                if 1 <= flight_choice <= len(available_flights):
                    return flight_choice
                else:
                    print("Invalid flight number. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def book_flight(self):
        print("\nFlight Booking:")
        departure = self.validate_location("Enter departure location: ")
        arrival = self.validate_location("Enter arrival location: ")

        available_flights = [flight for flight in self.flights if flight.departure.lower() == departure and flight.arrival.lower() == arrival]

        if not available_flights:
            print("No available flights for the selected route.")
            return

        self.display_flights(departure, arrival)

        flight_choice = self.validate_flight_choice("Enter the number of the flight you choose: ", departure, arrival)
        selected_flight = available_flights[flight_choice - 1]
        print(f"You have booked flight {selected_flight.flight_number} from {selected_flight.departure} to {selected_flight.arrival} on {selected_flight.date}.")

def main():
    airline_system = AirlineSystem()

    # Add sample flights with dates for the next 3 days
    today = datetime.now().date()
    for i in range(3):
        for departure in ['usa', 'uk', 'china', 'japan', 'indonesia', 'malaysia', 'singapore', 'qatar', 'india', 'france', 'spain']:
            for arrival in ['usa', 'uk', 'china', 'japan', 'indonesia', 'malaysia', 'singapore', 'qatar', 'india', 'france', 'spain']:
                if departure != arrival:
                    airline_system.add_flight(f"{departure[0].upper()}{arrival[0].upper()}{i+1}", departure, arrival, today + timedelta(days=i))

    print("Currently we connect to the following countries:")
    print(['usa', 'uk', 'china', 'japan', 'indonesia', 'malaysia', 'singapore', 'qatar', 'india', 'france', 'spain'])
    print("\nWelcome to the Airline Booking and Cargo Shipment System")
    while True:
        choice = input("Do you want to ship cargo (c) or book a flight (f)? (enter 'q' to quit): ").strip().lower()
        if choice == 'c':
            airline_system.ship_cargo()
        elif choice == 'f':
            airline_system.book_flight()
        elif choice == 'q':
            feedback = input("Please provide feedback: ")
            print("Thank you for your feedback.")
            print("For further assistance, please contact us at support@example.com or call us at +123456789.")
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'c', 'f', or 'q'.")

if __name__ == "__main__":
    main()
