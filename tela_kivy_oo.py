# coding: utf-8

from kivy.app import App
from kivy.uix.label import Label


class MeuPrograma(App):

    def build(self):
        l = Label()
        l.text = "Minha Tela OO, usando class"
        return l


MeuPrograma().run()
