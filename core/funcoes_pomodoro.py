from tkinter import *
from tkinter import messagebox
from turtle import update
from view import pomodoro
from turtledemo.nim import randomrow

from utils import colors, fonts
from PIL import ImageTk, Image

import time
from playsound import playsound
from view import pomodoro

def conversao(t):
    # de min para segundos:
    return t * 60


#####################################################################
# Variável global para rastrear se a janela está aberta ou não
janela_aberta = False
janela_config = None


def salvar_inputs(qntd_ciclos, duracao_pomodoro, duracao_pausaC, duracao_pausaM, duracao_pausaL):
    global v_ciclos, t_pomodoro, t_pausaC, t_pausaM, t_pausaL

    v_ciclos.set(int(qntd_ciclos.get()))
    t_pomodoro = int(duracao_pomodoro.get())
    t_pausaC = int(duracao_pausaC.get())
    t_pausaM = int(duracao_pausaM.get())
    t_pausaL = int(duracao_pausaL.get())


def abrir_janela():
    global janela_aberta, janela_config

    # Verifica se a janela já está aberta
    if janela_aberta:
        return

    # Cria a janela e configura suas propriedades
    janela_config = Toplevel()
    janela_config.title( "SETTINGS" )
    janela_config.geometry( '284x450' )
    janela_config.resizable( width=False, height=False )
    janela_config.iconbitmap( "assets/favicon.ico" )
    janela_config.resizable( width=False, height=False )

    img = PhotoImage( file="../view/assets/pomodoro_config.png" )
    bg_label = Label( janela_config, image=img )
    bg_label.place( relwidth=1, relheight=1 )
    bg_label.image = img

    # os inputs da janela config --------------------------------------------------------------------------------------------

    qntd_ciclos_var = StringVar()
    qntd_ciclos = Entry( janela_config, textvariable=qntd_ciclos_var, width=5, justify="center", relief="sunken" )
    qntd_ciclos.place( x=62, y=152 )

    duracao_pomodoro_var = StringVar()
    duracao_pomodoro = Entry( janela_config, textvariable=duracao_pomodoro_var, width=5, justify="center",
                              relief="sunken" )
    duracao_pomodoro.place( x=62, y=265 )

    duracao_pausaC_var = StringVar()
    duracao_pausaC = Entry( janela_config, textvariable=duracao_pausaC_var, width=5, justify="center", relief="sunken" )
    duracao_pausaC.place( x=62, y=296 )

    duracao_pausaM_var = StringVar()
    duracao_pausaM = Entry( janela_config, textvariable=duracao_pausaM_var, width=5, justify="center", relief="sunken" )
    duracao_pausaM.place( x=62, y=330 )

    duracao_pausaL_var = StringVar()
    duracao_pausaL = Entry( janela_config, textvariable=duracao_pausaL_var, width=5, justify="center", relief="sunken" )
    duracao_pausaL.place( x=62, y=362 )

    # botao de salvar dados
    botao_salvar = Button( janela_config, text=" SALVAR ", relief="flat", bg=colors.COR_LARANJA_CLARO,
                           font=fonts.fonte_botao,
                           fg=colors.COR_BRANCA,
                           command=lambda: salvar_inputs( qntd_ciclos, duracao_pomodoro,
                                                          duracao_pausaC, duracao_pausaM, duracao_pausaL) )
    botao_salvar.place( x=109, y=420 )

    # Define o sinalizador para indicar que a janela está aberta
    janela_aberta = True

    # Configura um callback para fechar a janela e redefinir o sinalizador
    janela_config.protocol( "WM_DELETE_WINDOW", fechar_janela )


def fechar_janela():
    global janela_aberta
    janela_aberta = False
    janela_config.destroy()


################################################################################################

def iniciarPausa(tempo_pomodoro,label,janela,t_pausa,ciclos,label_Vciclos):
    minutos = 0
    segundos = 5
    while minutos > 0 or segundos >= 0:
        timeformat = '{:02d} : {:02d}'.format(minutos, segundos)
        label.config(text=timeformat)
        janela.update()
        time.sleep(1)
        segundos -= 1
        if segundos < 0 :
                if minutos == 0:
                    segundos = 0
                    timeformat = '{:02d} : {:02d}'.format(minutos, segundos)
                    janela.update()
                    break
                else:
                    minutos -= 1
                    segundos = 59
    if ciclos > 0:
        ciclos -= 1
        playsound("../view/assets/clock.wav")
        label_Vciclos.config(text=ciclos)
        messagebox.showinfo("Muito bem!", "Partiu dar uma pausa? \n Clique no botão ok!")
        iniciarPausa(tempo_pomodoro,label,janela ,t_pausa,ciclos,label_Vciclos)
    elif ciclos == 0:
        playsound("../view/assets/clock.wav")
        label_Vciclos.config(text=ciclos)
        messagebox.showinfo("Muito bem!", "Você concluiu o pomodoro , Parabéns!")




def iniciarPomodoro(label,tempo_pomodoro, janela, ciclos,label_Vciclos, tempo_pm, tempo_pl):

    if tempo_pm:
        t_pausa = 10
    elif tempo_pl:
        t_pausa = 15
    else:
        t_pausa = 5

    minutos = 0
    segundos = 5

    while minutos > 0 or segundos >= 0:
        timeformat = '{:02d} : {:02d}'.format(minutos, segundos)
        label.config(text=timeformat)
        janela.update()
        time.sleep(1)
        segundos -= 1
        if segundos < 0 :
            if minutos == 0:
                segundos = 0
                timeformat = '{:02d} : {:02d}'.format(minutos, segundos)
                janela.update()
                break
            else:
                minutos -= 1
                segundos = 59

    if ciclos >= 0:
        playsound("../view/assets/clock.wav")
        label_Vciclos.config( text=ciclos )
        messagebox.showinfo("Muito bem!", "Partiu dar uma pausa? \n Clique no botão ok!")
        iniciarPausa(tempo_pomodoro,label,janela ,t_pausa,ciclos,label_Vciclos)








'''def break_():
    timer = conversao( t_pausa )
    while timer >= 0:
        work_break( timer )
        if timer == 0:
            # terminou a pausa, toca musica e troca o temporizador para foco
            playsound( "sound.ogg" )
            messagebox.showinfo( "Simbora!", "Bora voltar pro foco? \n Clique no botão de foco!" )
        timer -= 1
'''
# pomodoro(foco, pausa)
