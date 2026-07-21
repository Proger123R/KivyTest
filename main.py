from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from gdzapi import AsyncGDZ
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
import asyncio


sm = ScreenManager()

class ClassScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.add_widget(self.layout)
        self.create_buttons()

        self.class_num = None
        self.page_num = None
        self.subject = None

    def create_buttons(self):
        for cls_num in range(1, 12):
            text = f"{cls_num} класс"

            btn = Button(text=text)
            btn.bind(on_press=lambda instance, c=cls_num: self.cls_press(c))
            self.layout.add_widget(btn)

    def cls_press(self, c):
        self.class_num = c
        App.get_running_app().current_class = c
        if c == 5:
            sm.current = 'SubjectClass5'
            print(f"[DEBUG    ] {c}")
        if c == 6:
            sm.current = 'class_screen6'
        if c == 7:
            sm.current = 'class_screen7'
        if c == 8:
            sm.current = 'class_screen8'
        if c == 9:
            sm.current = 'class_screen9'


class SubjectClass5(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_buttons5()

    def create_buttons5(self):
        subjectsfor5 = ["Математика", "Русский язык", "Биология", "Английский Язык"]
        for sub in subjectsfor5:
            print(f"[DEBUG     ] Created {sub} button!")
            btn = Button(text=sub)
            btn.bind(on_press=lambda instance, c=sub: self.toTaskScreen(c))
            self.layout5.add_widget(btn)

    def toTaskScreen(self, c):
        App.get_running_app().current_subject = c
        if c == "Математика":
            sm.current = "taskScreen"
        if c == "Русский язык":
            sm.current = "taskScreen"
        if c == "Биология":
            sm.current = "taskScreen"
        if c == "Английский Язык":
            sm.current = "taskScreen"


class SubjectClass6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_buttons5()

    def create_buttons5(self):
        subjectsfor5 = ["Математика", "Русский язык", "Биология", "Английский"]
        for sub in subjectsfor5:
            print(f"[DEBUG     ] Created {sub} button!")
            btn = Button(text=sub)
            btn.bind(on_press=lambda instance, c=sub: self.toTaskScreen(c))
            self.layout5.add_widget(btn)

    def toTaskScreen(self, c):
        App.get_running_app().current_subject = c
        if c == "Математика":
            sm.current = "taskScreen"
        if c == "Русский язык":
            sm.current = "taskScreen"
        if c == "Биология":
            sm.current = "taskScreen"
        if c == "Английский Язык":
            sm.current = "taskScreen"



class SubjectClass7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_buttons5()

    def create_buttons5(self):
        subjectsfor5 = ["Алгебра", "Геометрия", "Вероятность", "Русский язык", "Английский язык", "Физика", "Информатика"]
        for sub in subjectsfor5:
            print(f"[DEBUG     ] Created {sub} button!")
            btn = Button(text=sub)
            btn.bind(on_press=lambda instance, c=sub: self.toTaskScreen(c))
            self.layout5.add_widget(btn)

    def toTaskScreen(self, c):
        App.get_running_app().current_subject = c
        if c == "Алгебра":
            sm.current = "taskScreen"
        if c == "Русский язык":
            sm.current = "taskScreen"
        if c == "Геометрия":
            sm.current = "taskScreen"
        if c == "Вероятность":
            sm.current = "taskScreen"
        if c == "Физика":
            sm.current = "taskScreen"
        if c == "Информатика":
            sm.current = "taskScreen"
        if c == "Английский Язык":
            sm.current = "taskScreen"



class SubjectClass8(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_buttons5()

    def create_buttons5(self):
        subjectsfor5 = ["Алгебра", "Геометрия", "Вероятность", "Русский язык", "Английский язык", "Физика", "Информатика", "Химия"]
        for sub in subjectsfor5:
            print(f"[DEBUG     ] Created {sub} button!")
            btn = Button(text=sub)
            btn.bind(on_press=lambda instance, c=sub: self.toTaskScreen(c))
            self.layout5.add_widget(btn)

    def toTaskScreen(self, c):
        App.get_running_app().current_subject = c
        if c == "Алгебра":
            sm.current = "taskScreen"
        if c == "Русский язык":
            sm.current = "taskScreen"
        if c == "Геометрия":
            sm.current = "taskScreen"
        if c == "Вероятность":
            sm.current = "taskScreen"
        if c == "Физика":
            sm.current = "taskScreen"
        if c == "Информатика":
            sm.current = "taskScreen"
        if c == "Английский Язык":
            sm.current = "taskScreen"
        if c == "Химия":
            sm.current = "taskScreen"



class SubjectClass9(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_buttons5()

    def create_buttons5(self):
        subjectsfor5 = ["Алгебра", "Геометрия", "Вероятность", "Русский язык", "Английский язык", "Физика", "Информатика", "Химия"]
        for sub in subjectsfor5:
            print(f"[DEBUG     ] Created {sub} button!")
            btn = Button(text=sub)
            btn.bind(on_press=lambda instance, c=sub: self.toTaskScreen(c))
            self.layout5.add_widget(btn)

    def toTaskScreen(self, c):
        App.get_running_app().current_subject = c
        if c == "Алгебра":
            sm.current = "taskScreen"
        if c == "Русский язык":
            sm.current = "taskScreen"
        if c == "Геометрия":
            sm.current = "taskScreen"
        if c == "Вероятность":
            sm.current = "taskScreen"
        if c == "Физика":
            sm.current = "taskScreen"
        if c == "Информатика":
            sm.current = "taskScreen"
        if c == "Английский Язык":
            sm.current = "taskScreen"
        if c == "Химия":
            sm.current = "taskScreen"

class TaskScreenFor(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_entry()

    def create_entry(self):
        self.inputTask = TextInput(text="", multiline=False)
        self.layout5.add_widget(self.inputTask)

        btn = Button(text="send", on_press=self.toResult)
        self.layout5.add_widget(btn)

    def toResult(self, instance):
        App.get_running_app().current_task = self.inputTask.text
        sm.current = "result"

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout5 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout5)
        self.create_image()

    async def getImageUrl(self):
        app = App.get_running_app()

        subject = getattr(app, "current_subject", None)
        class_num = getattr(app, "current_class", None)
        page_num = int(getattr(app, "current_task", None))

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

    def create_image(self):
        self.btn = Button(text="send", on_press=self.get)
        self.layout5.add_widget(self.btn)

    def get(self, instance):
        self.layout5.remove_widget(self.btn)
        image_url = asyncio.run(self.getImageUrl())
        finalUrl = "https:" + image_url

        img = AsyncImage(source=finalUrl, allow_stretch=True, keep_ratio=False)

        self.layout5.add_widget(img)


class MyApp(App):

    def build(self):
        self.current_class = None
        self.current_subject = None
        self.current_task = None

        sm.add_widget(ClassScreen(name="class_screen"))
        sm.add_widget(SubjectClass5(name="SubjectClass5"))
        sm.add_widget(SubjectClass6(name="class_screen6"))
        sm.add_widget(SubjectClass7(name="class_screen7"))
        sm.add_widget(SubjectClass8(name="class_screen8"))
        sm.add_widget(SubjectClass9(name="class_screen9"))

        sm.add_widget(TaskScreenFor(name="taskScreen"))
        sm.add_widget(Result(name="result"))

        return sm

if __name__ == "__main__":
    MyApp().run()