from tkinter import *
from utils import colors
from core import funcoes_main


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


class Interface:
    width = 1280
    height = 700

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Equipe")
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
                       font=('monospace', 32), relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela))
        label.place(x=625, y=50)

        Botao_Codigo = "DashBoard"
        label = Button(frame_top, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), relief=FLAT)
        label.place(x=800, y=50)

        Botao_Team = "Sobre"
        label = Button(frame_top, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), relief=FLAT)
        label.place(x=1068, y=50)

        frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
        frame_detalhes_borda.pack(padx=0, pady=0)

        frame_equipe = Frame(self.janela, width=1280, height=80, bg=colors.COR_BRANCA, relief=SOLID)
        frame_equipe.pack(padx=0, pady=0)
        label_nomes = Label(frame_equipe, text="Desenvolvedores :",
                            fg=colors.COR_CINZA_ESCURO, bg=colors.COR_BRANCA, font=('mulish', 30, "bold"))
        label_nomes.place(x=465, y=15)
        frame_meio_team = Frame(self.janela, width=1280, height=420, bg=colors.COR_BRANCA, relief=SOLID)
        frame_meio_team.pack(padx=0, pady=0)
        img_logo = PhotoImage(file='assets/Group 8.png')
        label = Label(frame_meio_team, image=img_logo)
        label.pack(padx=0, pady=0)
        Botao_Codigo = "Código GitHub"
        label = Button(self.janela, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 16), relief=FLAT,
                       command=funcoes_main.abrir_navegador)
        label.pack(padx=0, pady=20)
        self.janela.mainloop()


if __name__ == "__main__":
    interface = Interface()
