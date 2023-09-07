import tkinter
from tkinter import *
from utils import colors, fonts
from core import funcoes_main
from core import funcoes_bloco



def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


class Anotacoes:
    width = 1280
    height = 700

    def __init__(self):
        global numero_paginas_salvas
        self.janela = Tk()
        self.janela.title("Bloco de notas")
        center_window(self.janela, self.width, self.height)
        self.janela.config(background='#F2F2F0')
        self.janela.resizable(width=FALSE, height=FALSE)



        frame_top = Frame(self.janela, width=1280, height=125, bg=colors.COR_BRANCA, relief=SOLID)
        frame_top.pack(padx=0, pady=0)

        frame_detalhes = Frame(frame_top, width=1280, height=174, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
        frame_detalhes.pack(padx=0, pady=0)

        Texto_Productivity = "Productivity"
        label = Label(frame_top, text=Texto_Productivity, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                      font=('monospace', 40))
        label.place(x=34, y=50)

        Botao_Home = "Home"
        label = Button(frame_top, text=Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), command=lambda: funcoes_main.fechar_janela_home(self.texto, self.janela),
                       relief=FLAT
                       )
        label.place(x=625, y=50)

        Botao_Codigo = "DashBoard"
        label = Button(frame_top, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32),  relief=FLAT)
        label.place(x=800, y=50)

        Botao_Team = "Sobre"
        label = Button(frame_top, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), relief=FLAT, command=lambda: funcoes_main.fechar_janela_team(self.texto, self.janela))
        label.place(x=1068, y=50)

        frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
        frame_detalhes_borda.pack(padx=0, pady=0)

        centralizar = tkinter.Label(self.janela, text="Bloco de anotações", font="Arial 20")
        centralizar.pack()

        self.texto = Text(self.janela, wrap="word", height=18, width=100, font=fonts.fonte_conteudo)
        self.texto.pack()
        self.texto.focus_force()


        menu_janela = Menu(self.janela)
        file_menu_janela_bloco_notas = Menu(menu_janela, tearoff=0)
        menu_janela.add_cascade(label="Arquivo", menu=file_menu_janela_bloco_notas)
        file_menu_janela_bloco_notas.add_command(label="Nova página", command=lambda: funcoes_bloco.destruir(self.janela, self.texto))
        file_menu_janela_bloco_notas.add_command(label="Abrir...", command=lambda: funcoes_bloco.abrir_arquivo_janela(self.texto))
        file_menu_janela_bloco_notas.add_command(label="Salvar", command=lambda: funcoes_bloco.salvar_arquivo_janela(self.texto))
        file_menu_janela_bloco_notas.add_command(label="Salvar como...",
                                                 command=lambda: funcoes_bloco.salvar_como_arquivo_janela(self.texto))
        file_menu_janela_bloco_notas.add_separator()
        file_menu_janela_bloco_notas.add_command(label="Sair", command=lambda: funcoes_main.fechar_janela_home(self.texto, self.janela))
        menu_janela.add_command(label="Procurar", command=lambda: funcoes_bloco.pesquisar_palavra(self.texto))
        menu_janela.add_command(label="Desmarcar texto", command=lambda: funcoes_bloco.desmarcar_palavra(self.texto))
        menu_janela.add_command(label="Contador", command=lambda: funcoes_bloco.contador())
        self.janela.config(menu=menu_janela)
        self.janela.protocol("WM_DELETE_WINDOW", lambda: funcoes_main.fechar_janela_home(self.texto, self.janela))
        self.janela.mainloop()
