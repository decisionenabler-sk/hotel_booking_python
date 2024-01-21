import json
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def find_popular_service(bookings):
    services = {}
    for booking in bookings:
        for service in booking["additional_services"]:
            if service in services:
                services[service] += 1
            else:
                services[service] = 1
    # there can be multiple services that are most popular hence the list
    popular_services = [key for key,value in services.items() if value == max(services.values())]
    return popular_services
print(find_popular_service(booking_data["bookings"]))