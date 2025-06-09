import os
import random

class Booking:
    def __init__(self):
        self.rates = {
            "Standard": 50,
            "Deluxe": 100,
            "Suite": 180
        }

    def book_room(self, guests=1, days=1, room_type="Standard"):
        # Validate room type
        if room_type not in self.rates:
            print(f"\nRoom type '{room_type}' is not available. Defaulting to 'Standard'.")
            room_type = "Standard"

        rate_per_day = self.rates[room_type]
        total_cost = rate_per_day * days
        reference = f"BK{random.randint(1000, 9999)}"

        # Booking summary
        summary = (
            f"Booking Confirmation:\n"
            f"Booking Ref No. : {reference}\n"
            f"Room Type       : {room_type}\n"
            f"Guests          : {guests}\n"
            f"Days            : {days}\n"
            f"Rate per Day    : ${rate_per_day}\n"
            f"Total Cost      : ${total_cost}\n"
        )
        print("\n" + summary)

        # Save to file
        self.save_booking(reference, guests, days, room_type, rate_per_day, total_cost)

    def save_booking(self, ref, guests, days, room_type, rate_per_day, total_cost):
        file_exists = os.path.isfile("bookings.txt")
        write_header = False

        # Check if file exists and is empty, if yes, write header
        if not file_exists or os.path.getsize("bookings.txt") == 0:
            write_header = True
        
        try:
            with open("bookings.txt", "a") as file:
                
                if write_header:
                    file.write(
                        "BookingRefNo | RoomType | NoOfGuests | NoOfDays | RatePerDay | TotalCost\n"
                    )
                
                file.write(
                    f"{ref} | {room_type} | {guests} guests | {days} days | "
                    f"${rate_per_day}/day | Total: ${total_cost}\n"
                )
            print("Booking saved to 'bookings.txt'\n")
        except Exception as e:
            print(f"Failed to save booking: {e}")


def run_booking():
    print("Welcome to the Hotel Booking System\n")

    try:
        guests = int(input("Enter number of guests: "))
        days = int(input("Enter number of days: "))
        room_type = input("Enter room type (Standard / Deluxe / Suite): ").title()

        booking = Booking()
        booking.book_room(guests, days, room_type)

    except ValueError:
        print("Invalid input! Please enter numeric values for guests and days.\n")


# Run the system
run_booking()
