# First type of usage
from gdzapi import GDZ
from gdzapi import AsyncGDZ
import asyncio

gdz = GDZ()

            #for subject in gdz.subjects:
             #   if subject.name == "Биология":
              #      book = gdz.get_books(subject)[0]
               #     print(f"Book: {book.name}")
#
 #                   pages = gdz.get_pages(book.url)
  ##
    #                if pages:
     #                   solutions = gdz.get_gdz(pages[0].url)
      #                  image_url = solutions[0].image_src
       #                 print(image_url)





""" Hello dear reader of my code
    Im not good at programming
    Its my first project in kivy
    This file just testing GDZapi"""


def getAnswer(subject, page: int, classes):
    for sub in gdz.subjects:
        if sub.name == f"{subject}":
             book = gdz.get_books(sub)[classes]
             print(f"Book: {book.name}")

             pages = gdz.get_pages(book.url)
             print(f"Pages: {len(pages)}")

             if pages:
                  solution = gdz.get_gdz(pages[page].url)
                  image_url = solution[0].image_src
                  print(image_url)

def TEst(subject, page, classess):
    for cls in gdz.classes:
        if cls.id == classess:
            for sub in gdz.subjects:
                if sub.name == f"{subject}":
                    book = gdz.get_books(sub)[classess]
                    print(f"Book: {book.name}")

                    pages = gdz.get_pages(book.url)
                    print(f"Pages: {len(pages)}")

                    if pages:
                        solution = gdz.get_gdz(pages[page].url)
                        image_url = solution[0].image_src
                        print(image_url)


def TestSearch(inpuit):
    books = gdz.search_books(inpuit)
    for book in books:
        if "Ю.Н Макарычев" in book.authors:
            downloadable_images = []
            for i in book.pages:
                for j in i.solutions:
                    downloadable_images.append(j.image_src)
            print(downloadable_images)
            if inpuit: #this is code for author
                filtered = [b for b in books if any(inpuit.lower() in a.lower() for a in b.authors)] #and inpuit to author
                if filtered:
                    books = filtered
                else:
                    print("Книг с таким автором не найдено, покажу все подходящие по предмету и классу.")

def work(subject, class_num, page_num):
    query = f"{subject} {class_num} класс"
    books = gdz.search_books(query)

    if not books:
        print("Книг не найдено. Попробуй уточнить предмет или класс.")
        exit()

    book = books[0]
    print(f"\nВыбрана книга: {book.name}, авторы: {', '.join(book.authors)}")

    pages = gdz.get_pages(book.url)
    page = next((p for p in pages if p.number == page_num), None)

    print(f"\nРешения для страницы {page_num}:")

    if pages:
        solution = gdz.get_gdz(pages[page_num].url)
        image_url = solution[0].image_src
        print(image_url)

async def getImageUrl(subject, class_num, page_num):

    async with AsyncGDZ() as gdz:
        query = f"{subject} {class_num} класс"
        books =  await gdz.search_books(query)

        book = books[0]
        print(f"\nВыбрана книга: {book.name}, авторы: {', '.join(book.authors)}")

        pages = await gdz.get_pages(book.url)
        page = page_num - 1

        print(f"\nРешения для страницы {page_num}:")

        if pages:
            solution = await gdz.get_gdz(pages[page].url)
            image_url = solution[0].image_src
            return image_url
while True:
    #subject = input("Enter subject: ")
    #page = int(input("enter page:"))
    #classs = int(input("Enter class: "))
    #TEst(subject, page, classs)

    #ag = input("Enter tag: ")
    #aut = input("Enter author: ")
    #TestSearch(tag)

    subj = input("Enter subject: ")
    page = int(input("Enter page: "))
    cls = input("Enter class: ")
    asyncio.run(getImageUrl(subj, cls, page))
