import json
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def find_guest_history(bookings, guest_name):
    booking_history = []
    for booking in bookings:
        if booking["guest_name"] == guest_name:
            booking_history.append(booking)
    return booking_history

print(find_guest_history(booking_data["bookings"],"Jane Smith"))