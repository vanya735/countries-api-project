# -*- coding: utf-8 -*-

class Car:
    def __init__(self, car_id, brand, model, year, available=True):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.available = available

    def display_info(self):
        print(f"{self.car_id}: {self.brand} {self.model} ({self.year}) - "
              f"{'Available' if self.available else 'Not Available'}")

class Client:
    def __init__(self, name):
        self.name = name

    def view_available_cars(self, rental_system):
        print(f"\nДоступні авто для {self.name}:")
        rental_system.show_available_cars()

    def book_car(self, car_id, rental_system):
        rental_system.create_rental(self, car_id)

class Rental:
    def __init__(self, rental_id, client, car):
        self.rental_id = rental_id
        self.client = client
        self.car = car

    def generate_confirmation(self):
        print("\n=== Підтвердження Прокату ===")
        print(f"Номер оренди: {self.rental_id}")
        print(f"Клієнт: {self.client.name}")
        print(f"Авто: {self.car.brand} {self.car.model}")
        print("==============================\n")

class RentalSystem:
    def __init__(self):
        self.cars = []
        self.rentals = []

    def load_cars_from_list(self, cars_list):
        for c in cars_list:
            car = Car(c["car_id"], c["brand"], c["model"], c["year"], c["available"])
            self.cars.append(car)

    def show_available_cars(self):
        for car in self.cars:
            if car.available:
                car.display_info()

    def create_rental(self, client, car_id):
        for car in self.cars:
            if car.car_id == car_id and car.available:
                print(f"\nБронювання авто {car.brand} {car.model}...")
                car.available = False
                rental = Rental(len(self.rentals)+1, client, car)
                self.rentals.append(rental)
                rental.generate_confirmation()
                return
        print("❌ Авто недоступне або не знайдено.")

if __name__ == "__main__":
    car_data = [
        {"car_id": 1, "brand": "Toyota", "model": "Corolla", "year": 2020, "available": True},
        {"car_id": 2, "brand": "Honda", "model": "Civic", "year": 2019, "available": True},
        {"car_id": 3, "brand": "Ford", "model": "Focus", "year": 2021, "available": True},
    ]

    rental_system = RentalSystem()
    rental_system.load_cars_from_list(car_data)

    client_name = input("Введіть ваше ім'я: ")
    client = Client(client_name)

    while True:
        client.view_available_cars(rental_system)
        choice = input("Введіть номер авто для бронювання (або 'q' для виходу): ")
        if choice.lower() == 'q':
            print("Дякуємо! До побачення!")
            break
        if not choice.isdigit():
            print("❌ Будь ласка, введіть правильний номер авто.")
            continue
        client.book_car(int(choice), rental_system)
