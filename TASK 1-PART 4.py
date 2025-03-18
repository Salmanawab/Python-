# Task 1-Part 4
def standardize_genres(inventory):
    for isbn, details in inventory.items():
        title, author, price, genres = details
        cleaned_genres = {genre.strip().lower() for genre in genres}
        inventory[isbn] = (title, author, price, cleaned_genres)

# Example usage
book_library = {
    "978-3-16-148410-0": ("The Great Adventure", "Sajjad", 3000, {"fiction ", " Adventure"}),
    "978-1-23-456789-0": ("Mystery of the Old House", "Asadullah", 4000, {"Mystery", " Thriller "})
}

standardize_genres(book_library)
print(book_library)