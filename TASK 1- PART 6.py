# TASK 1-PART 6
def list_all_books(inventory):
    titles = [details[0] for details in inventory.values()]
    titles.sort()
    return titles

# Example usage
book_library = {
    "978-3-16-148410-0": ("The Great Adventure", "Sajjad", 3000.99, {"fiction", "adventure"}),
    "978-1-23-456789-0": ("Mystery of the Old House", "Asadullah", 4000.99, {"mystery", "thriller"})
}

print(list_all_books(book_library))