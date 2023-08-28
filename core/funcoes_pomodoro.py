from tkinter import *
from turtledemo.nim import randomrow

from utils import colors, fonts
from PIL import ImageTk, Image

import time
import os

"""foco = 25
pausa = 5"""


def conversao(t):
    pass
    # de min para segundos:
    """return t * 60"""


def pomodoro(foco, pausa):
    pass
    """f = conversao(foco)
    p = conversao(pausa)
    temporizador(f, "FOCO")
    os.system("cls")  # clear do windows
    temporizador(p, "PAUSA")
    os.system("cls")"""

#####################################################################
# Variável global para rastrear se a janela está aberta ou não
janela_aberta = False
janela_config = None

def abrir_janela():
    global janela_aberta, janela_config

    # Verifica se a janela já está aberta
    if janela_aberta:
        return

    # Cria a janela e configura suas propriedades
    janela_config = Toplevel()
    janela_config.title("SETTINGS")
    janela_config.geometry('284x379')
    janela_config.resizable(width=False, height=False)
    janela_config.iconbitmap("assets/favicon.ico")
    janela_config.resizable(width=False, height=False)

    img = PhotoImage(file="../view/assets/pomodoro_config.png")
    bg_label = Label(janela_config, image=img)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = img

    def qntd(janela_config):

        r_pomodoro = Entry(janela_config, width= 34, height= 20)
        r_pomodoro.place(x= 62, y= 252)

        r_intervalos = Entry(janela_config, width= 34, height = 20)
        r_pomodoro.place(x= 62, y= 219)

    #chamando as funções
    qntd(janela_config)

    # Define o sinalizador para indicar que a janela está aberta
    janela_aberta = True

    # Configura um callback para fechar a janela e redefinir o sinalizador
    janela_config.protocol("WM_DELETE_WINDOW", fechar_janela)

def fechar_janela():
    global janela_aberta
    janela_aberta = False
    janela_config.destroy()


################################################################################################

'''configuração em uma nova abinha do tempo de pausa, tempo de foco'''

def temporizador(tempo, label):
    pass


#pomodoro(foco, pausa)