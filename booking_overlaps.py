import json
from datetime import datetime
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
# Case 1: Check if the check in and check out date between any two bookings is same (we can do this by nested loop)
# Case 2: Check if the room type for those dates are same 
def find_booking_overlap(booking_data):
        
        overlapping_bookings = []
        for i in range(len(booking_data["bookings"])):
              booking1 = booking_data["bookings"][i]
              check_in_date1 = datetime.strptime(booking1["check_in_date"] , "%Y-%m-%d")
              check_out_date1 = datetime.strptime(booking1["check_out_date"] , "%Y-%m-%d")
              room_type1 = booking1["room_type"]
              for j in range(i+1, len(booking_data["bookings"])):
                    booking2 = booking_data["bookings"][j]
                    check_in_date2 = datetime.strptime(booking2["check_in_date"] , "%Y-%m-%d")
                    check_out_date2 = datetime.strptime(booking2["check_out_date"] , "%Y-%m-%d")
                    room_type2 = booking2["room_type"]
                    if room_type1 == room_type2 and check_in_date1 < check_out_date2 and check_out_date1 > check_in_date2:
                    # Overlapping booking found
                        overlapping_bookings.append((booking1, booking2))
        return overlapping_bookings
if len(find_booking_overlap(booking_data)) ==0:
      print("No overlapping bookings found.")
else:
    print(find_booking_overlap(booking_data))