import json
from collections import defaultdict
with open("hotel_booking_data.json", "r") as file:
    booking_data = json.load(file)
def find_top_keywords(bookings):
    all_words_count = defaultdict(int)
    for booking in bookings:
        comments = booking["feedback"]["comments"]
        for word in comments.split():
            if word in all_words_count:
                all_words_count[word] += 1
            else:
                all_words_count[word] = 1
    keywords = list(all_words_count.items())
    sorted_keywords = sorted(keywords, key=lambda x: x[1], reverse=True)
    top_keywords = sorted_keywords[:3]
    return top_keywords
print("The top keywords in the the feedback are:", find_top_keywords(booking_data["bookings"]))

