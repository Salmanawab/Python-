# TASK 1-PART-3
def update_price(isbn, new_price, inventory):
    if isbn in inventory:
        title, author, price, genres = inventory[isbn]
        inventory[isbn] = (title, author, new_price, genres)

# Example use
book_library = {
    "978-3-16-148410-0": ("The Great Adventure", "sajjad", 3000.99, {"fiction", "adventure"}),
    "978-1-23-456789-0": ("Mystery of the Old House", "Jane Smith", 6000.99, {"mystery", "thriller"})
}

update_price("978-3-16-148410-0",9000, book_library)
print(book_library)