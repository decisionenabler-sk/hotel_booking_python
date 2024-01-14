import json
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def calculate_total_revenue(booking_data):
    revenue = 0
    for booking in booking_data["bookings"]:
        revenue += booking["total_cost"]
    return revenue

total_revenue = calculate_total_revenue(booking_data)
print(f"Total Revenue: $", total_revenue)