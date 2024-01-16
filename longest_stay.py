import json
from datetime import datetime
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def find_longest_stay_booking(booking_data):
    longest_stay = None
    longest_booking = None
    for booking in booking_data["bookings"]:
        days = (datetime.strptime(booking["check_out_date"], "%Y-%m-%d") - datetime.strptime(booking["check_in_date"], "%Y-%m-%d")).days
        booking["stay"] = int(days)
        if longest_booking is None or days > longest_stay:
            longest_stay = days
            longest_booking = booking
    # print(longest_booking)
    return longest_booking
find_longest_stay_booking(booking_data)