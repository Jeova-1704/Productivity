import webbrowser
from tkinter import *

import view.dashboard
from utils import colors
from view import ToDoList, Calendario, Team
from core import funcoes_bloco
from view import Main_bloco_notas


def abrir_navegador():
    nova_url = "https://github.com/Jeova-1704/Projeto-programacao-1"
    webbrowser.open(nova_url)


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


def renderizer_main():
    width = 1280
    height = 700
    janela = Tk()
    janela.iconbitmap('../view/assets/logo.ico')
    janela.title("Janela Principal")
    center_window(janela, width, height)
    janela.config(background=colors.COR_BRANCA)
    janela.resizable(width=FALSE, height=FALSE)

    frame_top = Frame(janela, width=1280, height=125, bg=colors.COR_BRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top, width=1280, height=174, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
    frame_detalhes.pack(padx=0, pady=0)

    Texto_Productivity = "Productivity"
    label = Label(frame_top, text=Texto_Productivity, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                  font=('monospace', 40))
    label.place(x=34, y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                   font=('monospace', 32), relief=FLAT, command=lambda: renderizar_home(janela))
    label.place(x=625, y=50)

    Botao_Codigo = "DashBoard"
    label = Button(frame_top, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                   font=('monospace', 32), relief=FLAT)
    label.place(x=800, y=50)

    Botao_Team = "Sobre"
    label = Button(frame_top, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                   font=('monospace', 32), command=lambda: renderizar_team(janela), relief=FLAT)
    label.place(x=1068, y=50)

    frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
    frame_detalhes_borda.pack(padx=0, pady=0)

    frame_meio = Frame(janela, width=1280, height=220, bg=colors.COR_BRANCA, relief=SOLID)
    frame_meio.pack(padx=0, pady=0, side='right')

    img_logo = PhotoImage(file='assets/logo_productivity.png')
    label = Label(frame_meio, image=img_logo)
    label.pack(padx=90, pady=0, side='left')

    frame_centro_Borda = Label(frame_meio, width=1, height=240, bg=colors.COR_CINZA_CLARO, relief=FLAT)
    frame_centro_Borda.place(x=380, y=0)

    frame_centro = Frame(frame_meio, width=900, height=240, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
    frame_centro.pack(padx=0, pady=0, side='right')

    img_ToDoList = PhotoImage(file='assets/Ellipse 1.png')
    label_ToDoList = Button(frame_meio, image=img_ToDoList, relief=FLAT, bg=colors.COR_CINZA_ESCURO,
                            command=lambda: renderizar_todoList(janela))
    label_ToDoList.place(x=385, y=23)

    img_Anotacoes = PhotoImage(file='assets/Ellipse 2.png')
    label_Anotacoes = Button(frame_meio, image=img_Anotacoes, relief=FLAT, bg=colors.COR_CINZA_ESCURO,
                             command=lambda: renderizar_anotacoes(janela))
    label_Anotacoes.place(x=602, y=23)

    img_Calendario = PhotoImage(file='assets/Ellipse 3.png')
    label_Calendario = Button(frame_meio, image=img_Calendario, relief=FLAT, bg=colors.COR_CINZA_ESCURO,
                              command=lambda: renderizar_calendario(janela))
    label_Calendario.place(x=821, y=23)

    img_Pomodoro = PhotoImage(file='assets/Ellipse 4.png')
    label_Pomodoro = Button(frame_meio, image=img_Pomodoro, relief=FLAT, bg=colors.COR_CINZA_ESCURO)
    label_Pomodoro.place(x=1040, y=23)

    janela.mainloop()


def renderizar_home(janela):
    janela.destroy()
    renderizer_main()


def renderizar_todoList(janela_main):
    janela_main.destroy()
    ToDoList.InterfaceToDoList()


def renderizar_calendario(janela_main):
    janela_main.destroy()
    Calendario.Interface()


def renderizar_team(janela_main):
    janela_main.destroy()
    Team.Interface()


def renderizar_anotacoes(janela_main):
    janela_main.destroy()
    Main_bloco_notas.Anotacoes()

def renderizar_pomodoro(janela_main):
    janela_main.destroy()
    #abrir classe


def renderizar_dashboard(janela_autal):
    janela_autal.destroy()
    view.dashboard.InterfaceDashboard()


def renderizar_team_anotacoes(janela_main):
    janela_main.destroy()
    Team.Interface()


def renderizar_home_anotacoes(janela):
    janela.destroy()
    renderizer_main()


def fechar_janela_home(texto, janela):
    conteudo_janela = texto.get("1.0", "end-1c")
    if conteudo_janela != "":
        mensagem = funcoes_bloco.messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            funcoes_bloco.salvar_arquivo_janela(texto)
            janela.destroy()
            renderizer_main()
        else:
            janela.destroy()
            renderizer_main()
    else:
        janela.destroy()
        renderizer_main()


def fechar_janela_team(texto, janela):
    conteudo_janela = texto.get("1.0", "end-1c")
    if conteudo_janela != "":
        mensagem = funcoes_bloco.messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            funcoes_bloco.salvar_arquivo_janela(texto)
            janela.destroy()
            Team.Interface()
        else:
            janela.destroy()
            Team.Interface()
    else:
        janela.destroy()
        Team.Interface()
