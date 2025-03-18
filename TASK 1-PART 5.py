def display_inventory():
    for isbn, details in book_library.items():
        print(f"ISBN: {isbn}")
        print(f"Title: {details[0]}")
        print(f"Author: {details[1]}")
        print(f"Price:  {details[2]:.2f}")
        print(f"Genres: {', '.join(details[3])}")
        print("-" * 30)

# Example usage
book_library = {
    "978-3-16-148410-0": ("The Great Adventure", "Sajjad", 4000.99, {"fiction", "adventure"}),
    "978-1-23-456789-0": ("Mystery of the Old House", "Asadullah", 5000.99, {"mystery", "thriller"})
}

display_inventory()