# First type of usage
from gdzapi import GDZ

gdz = GDZ()

for subject in gdz.subjects:
    if subject.name == "Биология":
        book = gdz.get_books(subject)[0]
        print(f"Book: {book.name}")

        pages = gdz.get_pages(book.url)
        print(f"Number of pages: {len(pages)}")

        if pages:
            solutions = gdz.get_gdz(pages[0].url)
            image_url = solutions[0].image_src
            print(image_url)

# --------------------------------------------------------------

# Second type of usage
