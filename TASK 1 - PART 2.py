# TASK 1-PART-2
# use Loop through the inventory dictionary
def search_by_author(author):
    matching_books = []
    for isbn, details in book_library.items():
        if details[1] == author:
            matching_books.append((isbn, details[0]))
    return matching_books

# Example use
book_library = {
    "978-3-16-148410-0": ("The Great Adventure", "Sajjad", 3000.99, {"fiction", "adventure"}),
    "978-1-23-456789-0": ("Mystery of the Old House", "Asadullah", 4000.99, {"mystery", "thriller"}),
    "978-0-12-345678-9": ("Another Adventure", "Faraz", 5000.99, {"fiction"})
}

print(search_by_author("Asadullah"))