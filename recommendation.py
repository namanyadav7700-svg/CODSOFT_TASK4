print("===== Recommendation System =====")

categories = {
    "movie": ["3 Idiots", "KGF", "Pushpa", "Dangal"],
    "book": ["Rich Dad Poor Dad", "Atomic Habits", "The Alchemist"],
    "music": ["Arijit Singh", "Atif Aslam", "Sonu Nigam"]
}

print("Available Categories:")
print("1. movie")
print("2. book")
print("3. music")

choice = input("\nEnter category: ").lower()

if choice in categories:
    print("\nRecommended for you:")
    for item in categories[choice]:
        print("-", item)
else:
    print("Sorry! Category not found.")