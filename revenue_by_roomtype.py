import json
from collections import defaultdict
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def calculate_revenue(bookings):
    room_revenue = defaultdict(float)
    for booking in bookings:
        room_type = booking["room_type"]
        total_cost = booking["total_cost"]
        room_revenue[room_type] += total_cost
    return dict(room_revenue)

print("Revenue by Room Type:",calculate_revenue(booking_data["bookings"]))