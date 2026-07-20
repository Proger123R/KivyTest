from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.widget import Widget
from kivy.uix.button import Button
from gdzapi import GDZ

class MyApp(App):
    def build(self):
        return Button()

if __name__ == "__main__":
    MyApp().run()