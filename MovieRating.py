
print("=== MOVIE RATING ===")

movie = input("Enter movie title: ")
rating = int(input("Rate the movie (1-5): "))

if rating == 5:
    comment = "Excellent!"
elif rating == 4:
    comment = "Very Good!"
elif rating == 3:
    comment = "Good!"
elif rating == 2:
    comment = "Needs Improvement"
elif rating == 1:
    comment = "Poor"
else:
    comment = "Invalid Rating"

print("\nMovie:", movie)
print("Rating:", rating)
print("Comment:", comment)
