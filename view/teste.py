from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from core import funcoes_todolist, funcoes_main
from dao import bdToDoList
from utils import colors, fonts
from utils.ToolTip import Tooltip


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


class InterfaceToDoList:
    Botao_Codigo: str

    width = 1280
    height = 700
    def __init__(self):

        self.janela = Tk()
        self.janela.iconbitmap('assets/IconToDoList.ico')
        self.janela.title("To-Do List")
        center_window(self.janela, self.width, self.height)
        self.janela.config(background=colors.COR_BRANCA)

if __name__ == '__main__':
    InterfaceToDoList()