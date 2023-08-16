from tkinter import *
import tkinter as tk
import webbrowser
from utils.colors import *
from utils.window import get_modelo_janela
from view import ToDoList

janela = get_modelo_janela()

def renderizar_header():
    global janela

    frame_top = Frame(janela, width=1280, height=125, bg=COR_BRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top,width=1280,height=174,bg=COR_CINZA_ESCURO,relief=SOLID)
    frame_detalhes.pack(padx=0,pady=0)

    Texto_Productivity = "Productivity"
    label = tk.Label(frame_top, text=Texto_Productivity,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 40))
    label.place(x=34,y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32),relief=FLAT, command=renderizar_home)
    label.place(x=625,y=50)

    Botao_Codigo = "DashBoard"
    label = Button(frame_top, text=Botao_Codigo,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32), relief=FLAT)
    label.place(x=800,y=50)

    Botao_Team = "Sobre"
    label = Button(frame_top, text=Botao_Team,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32),relief=FLAT, command=renderizar_tela_team)
    label.place(x=1068,y=50)

    frame_detalhes_borda = Frame(frame_top,width=1280,height=4,bg=COR_CINZA_CLARO,relief=SOLID)
    frame_detalhes_borda.pack(padx=0, pady=0)

def limpar_janela(janela_para_fechar=False):

    if janela_para_fechar:
        janela_para_fechar.destroy()
    else:
        global janela
        janela.destroy()
        janela = get_modelo_janela()

def renderizar_home(janela_para_fechar=False):
    if janela_para_fechar:
        limpar_janela(janela_para_fechar)
    else:
        limpar_janela()

    renderizar_header()

    frame_meio = Frame(janela, width=1280, height=220, bg=COR_BRANCA, relief=SOLID)
    frame_meio.pack(padx=0, pady=0, side='right')

    img_logo = PhotoImage(file='../view/assets/logo_productivity.png')
    label = Label(frame_meio, image=img_logo)
    label.pack(padx=90, pady=0, side='left')

    frame_centro_Borda = Label(frame_meio, width=1, height=240, bg=COR_CINZA_CLARO, relief=FLAT)
    frame_centro_Borda.place(x=380, y=0)

    frame_centro = Frame(frame_meio, width=900, height=240, bg=COR_CINZA_ESCURO, relief=SOLID)
    frame_centro.pack(padx=0, pady=0, side='right')

    img_ToDoList = PhotoImage(file='../view/assets/Ellipse 1.png')
    label_ToDoList = Button(frame_meio, image=img_ToDoList, relief=FLAT, bg=COR_CINZA_ESCURO,command=renderizar_ToDoList)
    label_ToDoList.place(x=385, y=23)


    img_Anotacoes = PhotoImage(file='../view/assets/Ellipse 2.png')
    label_Anotacoes = Button(frame_meio, image=img_Anotacoes, relief=FLAT, bg=COR_CINZA_ESCURO)
    label_Anotacoes.place(x=602, y=23)

    img_Calendario = PhotoImage(file='../view/assets/Ellipse 3.png')
    label_Calendario = Button(frame_meio, image=img_Calendario, relief=FLAT, bg=COR_CINZA_ESCURO)
    label_Calendario.place(x=821, y=23)

    img_Pomodoro = PhotoImage(file='../view/assets/Ellipse 4.png')
    label_Pomodoro = Button(frame_meio, image=img_Pomodoro, relief=FLAT, bg=COR_CINZA_ESCURO)
    label_Pomodoro.place(x=1040, y=23)

    janela.mainloop()

def abrir_navegador():
    nova_url = "https://github.com/Jeova-1704/Projeto-programacao-1"
    webbrowser.open(nova_url)

def voltar_home():
    limpar_janela()

    renderizar_home()

def renderizar_tela_team():
    limpar_janela()

    renderizar_header()

    frame_equipe = Frame(janela,width=1280,height=80,bg=COR_BRANCA,relief=SOLID)
    frame_equipe.pack(padx=0,pady=0)

    label_nomes = Label(frame_equipe,text="Desenvolvedores :",
                        fg=COR_CINZA_ESCURO,bg=COR_BRANCA,font=('mulish', 30, "bold"))
    label_nomes.place(x=465,y=15)

    frame_meio_team = Frame(janela, width=1280, height=420, bg=COR_BRANCA, relief=SOLID)
    frame_meio_team.pack(padx=0, pady=0)

    img_logo = PhotoImage(file='../view/assets/Group 8.png')
    label = Label(frame_meio_team, image=img_logo)
    label.pack(padx=0, pady=0)

    Botao_Codigo = "Código GitHub"
    label = Button(janela, text=Botao_Codigo,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 16), relief=FLAT, command=abrir_navegador)
    label.pack(padx=0,pady=20)

    janela.mainloop()

def renderizar_ToDoList():
    janela.destroy()

    ToDoList.criar_janela_todo_list()





