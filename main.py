import json
from abc import ABC, abstractmethod
from datetime import datetime


class Service(ABC):
    def __init__(self, service_id, name, price):
        self.service_id = service_id
        self.name = name
        self.price = price

    @abstractmethod
    def description(self):
        pass


class Haircut(Service):
    def description(self):
        return f"A stylish haircut for a fresh look. Price: ${self.price}"


class Facial(Service):
    def description(self):
        return f"A relaxing facial treatment to rejuvenate your skin. Price: ${self.price}"


class Massage(Service):
    def description(self):
        return f"A soothing massage to relieve stress and tension. Price: ${self.price}"



class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Customer Name: {self.name}, Phone: {self.phone}"



class Appointment:
    def __init__(self, customer, service, date_time):
        self.customer = customer
        self.service = service
        self.date_time = date_time

    def details(self):
        return f"Appointment for {self.customer.name} on {self.date_time} for {self.service.name}."



class BeautySalon:
    def __init__(self, services_file):
        self.services = self.load_services(services_file)
        self.customers = []
        self.appointments = []

    def load_services(self, services_file):
        # Load services from JSON file
        with open(services_file, 'r') as file:
            data = json.load(file)
        services = []
        for service_data in data['services']:
            if service_data['name'] == 'Haircut':
                services.append(Haircut(service_data['id'], service_data['name'], service_data['price']))
            elif service_data['name'] == 'Facial':
                services.append(Facial(service_data['id'], service_data['name'], service_data['price']))
            elif service_data['name'] == 'Massage':
                services.append(Massage(service_data['id'], service_data['name'], service_data['price']))
        return services

    def show_services(self):
        print("\nAvailable Services:")
        for service in self.services:
            print(f"{service.service_id}. {service.name} - ${service.price}")

    def add_customer(self, name, phone):
        customer = Customer(name, phone)
        self.customers.append(customer)
        print(f"Customer {name} added successfully.")

    def book_appointment(self, customer_name, service_id, date_time):
        customer = next((c for c in self.customers if c.name == customer_name), None)
        if not customer:
            print(f"Customer {customer_name} not found.")
            return
        service = next((s for s in self.services if s.service_id == service_id), None)
        if not service:
            print("Service not found.")
            return
        appointment = Appointment(customer, service, date_time)
        self.appointments.append(appointment)
        print(f"Appointment booked for {customer_name} on {date_time} for {service.name}.")

    def show_appointments(self):
        print("\nAppointments:")
        for appointment in self.appointments:
            print(appointment.details())



def main():
    salon = BeautySalon('services.json')

    while True:
        print("\nWelcome to the Beauty Salon!")
        print("1. Show Services")
        print("2. Add Customer")
        print("3. Book Appointment")
        print("4. Show Appointments")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            salon.show_services()

        elif choice == '2':
            name = input("Enter customer name: ")
            phone = input("Enter customer phone: ")
            salon.add_customer(name, phone)

        elif choice == '3':
            customer_name = input("Enter customer name: ")
            service_id = int(input("Enter service ID: "))
            date_time = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
            try:
                date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
                salon.book_appointment(customer_name, service_id, date_time)
            except ValueError:
                print("Invalid date format.")

        elif choice == '4':
            salon.show_appointments()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
