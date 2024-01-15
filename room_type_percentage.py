import json
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def calculate_room_type_percentage(booking_data):
    total_bookings = len(booking_data["bookings"])
    room_type_bookings = {}
    for booking in booking_data["bookings"]:
        room_type_bookings[booking["room_type"]] = room_type_bookings.get(booking["room_type"], 0) + 1
    room_type_bookings = {key: round(value * 100 / total_bookings, 2) for key, value in room_type_bookings.items()}
    return room_type_bookings
print(calculate_room_type_percentage(booking_data))