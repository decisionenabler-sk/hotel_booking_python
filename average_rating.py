import json
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def calculate_average_rating(booking_data):
    booking_count = len(booking_data["bookings"])
    all_ratings = 0
    for booking in booking_data["bookings"]:
        all_ratings += booking["feedback"]["rating"]
    if booking_count == 0:
        return 0  # Return 0 if there are no bookings to avoid division by zero
    else:
        average_rating = round(all_ratings/booking_count,2)
    return average_rating
print(calculate_average_rating(booking_data))