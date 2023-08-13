from tkinter import *
import tkinter as tk
import webbrowser
from utils.colors import *
from utils.window import get_window

janela = get_window()


def limpar_janela():
    global janela

    janela.destroy()

    janela = get_window()


def criar_Frame_Top(janela):
    frame_top = Frame(janela, width=1280, height=125, bg=COR_BRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top,width=1280,height=174,bg=COR_CINZA_ESCURO,relief=SOLID)
    frame_detalhes.pack(padx=0,pady=0)

    Texto_Productivity = "Productivity"
    label = tk.Label(frame_top, text=Texto_Productivity,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 40))
    label.place(x=34,y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32),relief=FLAT )
    label.place(x=625,y=50)

    Botao_Codigo = "Código"
    label = Button(frame_top, text=Botao_Codigo,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32), relief=FLAT,command= abrir_navegador)
    label.place(x=846,y=50)

    Botao_Team = "Team"
    label = Button(frame_top, text=Botao_Team,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32),relief=FLAT, command=lambda: abrir_janela_team())
    label.place(x=1068,y=50)

    frame_detalhes_borda = Frame(frame_top,width=1280,height=4,bg=COR_CINZA_CLARO,relief=SOLID)
    frame_detalhes_borda.pack(padx=0,pady=0)


def criar_home():
    frame_top = Frame(janela, width=1280, height=125, bg=COR_BRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top,width=1280,height=174,bg=COR_CINZA_ESCURO,relief=SOLID)
    frame_detalhes.pack(padx=0,pady=0)

    Texto_Productivity = "Productivity"
    label = tk.Label(frame_top, text=Texto_Productivity,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 40))
    label.place(x=34,y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32),relief=FLAT )
    label.place(x=625,y=50)

    Botao_Codigo = "Código"
    label = Button(frame_top, text=Botao_Codigo,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32), relief=FLAT,command= abrir_navegador)
    label.place(x=846,y=50)

    Botao_Team = "Team"
    label = Button(frame_top, text=Botao_Team,fg=COR_BRANCA,  bg=COR_CINZA_ESCURO,font=('monospace', 32),relief=FLAT, command=lambda: abrir_janela_team())
    label.place(x=1068,y=50)

    frame_detalhes_borda = Frame(frame_top,width=1280,height=4,bg=COR_CINZA_CLARO,relief=SOLID)
    frame_detalhes_borda.pack(padx=0,pady=0)

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
    label_ToDoList = Button(frame_meio, image=img_ToDoList, relief=FLAT, bg=COR_CINZA_ESCURO)
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

    criar_home()


def abrir_janela_team():
    limpar_janela()

    frame_top = Frame(janela, width=1280, height=125, bg=COR_BRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top, width=1280, height=174, bg=COR_CINZA_ESCURO, relief=SOLID)
    frame_detalhes.pack(padx=0, pady=0)

    Texto_Productivity = "Productivity"
    label = tk.Label(frame_top, text=Texto_Productivity, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 40))
    label.place(x=34, y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT,
                   command=lambda: voltar_home())
    label.place(x=625, y=50)

    Botao_Codigo = "Código"
    label = Button(frame_top, text=Botao_Codigo, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 32),
                   relief=FLAT, command=abrir_navegador)
    label.place(x=846, y=50)

    Botao_Team = "Team"
    label = Button(frame_top, text=Botao_Team, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT,
                   command=lambda: abrir_janela_team())
    label.place(x=1068, y=50)

    frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=COR_CINZA_CLARO, relief=SOLID)
    frame_detalhes_borda.pack(padx=0, pady=0)
