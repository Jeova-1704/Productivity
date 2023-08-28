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

def salvar_inputs(qntd_pomodoros, qtnd_intervalos, duracao_pomodoro, duracao_pausaC, duracao_pausaM, duracao_pausaL, janela):
    global v_pomodoro, v_intervalos, t_pomodoro, t_pausaC, t_pausaM, t_pausaL

    v_pomodoro = int(qntd_pomodoros.get())
    v_intervalos = int(qtnd_intervalos.get())
    t_pomodoro= int(duracao_pomodoro.get())
    t_pausaC= int(duracao_pausaC.get())
    t_pausaM= int(duracao_pausaM.get())
    t_pausaL= int(duracao_pausaL.get())
    print(v_pomodoro)



def abrir_janela():
    global janela_aberta, janela_config

    # Verifica se a janela já está aberta
    if janela_aberta:
        return

    # Cria a janela e configura suas propriedades
    janela_config = Toplevel()
    janela_config.title("SETTINGS")
    janela_config.geometry('284x450')
    janela_config.resizable(width=False, height=False)
    janela_config.iconbitmap("assets/favicon.ico")
    janela_config.resizable(width=False, height=False)

    img = PhotoImage(file="../view/assets/pomodoro_config.png")
    bg_label = Label(janela_config, image=img)
    bg_label.place(relwidth=1, relheight=1)
    bg_label.image = img

    #os inputs da janela config --------------------------------------------------------------------------------------------

    qntd_pomodoros_var = StringVar()
    qntd_pomodoros = Entry( janela_config, textvariable=qntd_pomodoros_var, width=5, justify="center", relief="sunken" )
    qntd_pomodoros.place(x=62, y=142)

    qntd_intervalos_var = StringVar()
    qntd_intervalos = Entry( janela_config, textvariable=qntd_intervalos_var, width=5, justify="center", relief="sunken" )
    qntd_intervalos.place(x=62, y=175)

    duracao_pomodoro_var = StringVar()
    duracao_pomodoro = Entry( janela_config, textvariable=duracao_pomodoro_var, width=5, justify="center",
                              relief="sunken" )
    duracao_pomodoro.place( x=62, y=265 )

    duracao_pausaC_var = StringVar()
    duracao_pausaC = Entry( janela_config, textvariable=duracao_pausaC_var, width=5, justify="center", relief="sunken" )
    duracao_pausaC.place(x=62, y=296)

    duracao_pausaM_var = StringVar()
    duracao_pausaM = Entry( janela_config, textvariable=duracao_pausaM_var, width=5, justify="center", relief="sunken" )
    duracao_pausaM.place(x=62, y=330)

    duracao_pausaL_var = StringVar()
    duracao_pausaL = Entry( janela_config, textvariable=duracao_pausaL_var, width=5, justify="center", relief="sunken" )
    duracao_pausaL.place(x=62, y=362)


    #botao de salvar dados
    botao_salvar = Button(janela_config, text= " SALVAR ", relief="flat", bg=colors.COR_LARANJA_CLARO, font=fonts.fonte_botao,
                          fg=colors.COR_BRANCA, command=lambda : salvar_inputs(qntd_pomodoros, qntd_intervalos, duracao_pomodoro,
                                                                      duracao_pausaC, duracao_pausaM, duracao_pausaL, janela_config ))
    botao_salvar.place(x= 109, y= 420)

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