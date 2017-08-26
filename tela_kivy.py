# coding: utf-8


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window


ed = TextInput(text="eXcript")


def click():
    print(ed.text)


def build():
    layout = FloatLayout()

    #ed = TextInput(text="eXcript")
    #global ed
    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button()
    bt.text = "Clique Aqui"
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.y = 150
    bt.x = 170
    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout

Window.size = 600, 600

janela = App()
janela.title = "eXcript"
janela.build = build
janela.run()