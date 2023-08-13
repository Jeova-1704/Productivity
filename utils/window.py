from tkinter import *

from utils.colors import COR_BRANCA


def get_modelo_janela():
    main_window = Tk()

    main_window.title("Janela Principal")
    main_window.geometry('1280x700')
    main_window.config(background=COR_BRANCA)
    main_window.resizable(width=FALSE, height=FALSE)

    return main_window
