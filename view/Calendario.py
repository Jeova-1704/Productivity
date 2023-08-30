from tkinter import *
from tkcalendar import Calendar
from core import funcoes_calendario, funcoes_main
from utils import colors


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
        self.janela.iconbitmap('assets/calendario.ico')
        self.janela.title("Calendário")
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
                       font=('monospace', 32), relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela)
                       )
        label.place(x=625, y=50)

        Botao_Codigo = "DashBoard"
        label = Button(frame_top, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32),
                       relief=FLAT)
        label.place(x=800, y=50)

        Botao_Team = "Sobre"
        label = Button(frame_top, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), relief=FLAT, command=lambda: funcoes_main.renderizar_team(self.janela))
        label.place(x=1068, y=50)

        frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
        frame_detalhes_borda.pack(padx=0, pady=0)

        self.frame_calendario = Frame(self.janela, bg='#F2F2F0')
        self.frame_calendario.pack(side="left", fill="both", expand=True)

        self.frame_tabela = Frame(self.janela, width=200, height=100, bg="#A5A6A4", relief=SOLID)
        self.frame_tabela.pack(side="right", padx=5, pady=10, fill="both", expand=True)

        self.cal = Calendar(
            self.frame_calendario,
            selectmode="day",
            year=2023,
            month=1,
            day=1,
            locale="pt_BR",
            date_pattern="dd/mm/yyyy"
        )

        self.cal.configure(
            background="#737373",
            foreground="#A5A6A4",
            selectbackground="#BF4C0A",
            selectforeground="#F2F2F0",
            font=("monospace", 14)
        )

        self.cal.pack(side="top", padx=10, pady=20, fill="both", expand=True)

        self.funcoes = funcoes_calendario.Funcoes(self.frame_calendario, self.cal, self.frame_tabela, self.janela)

        self.botao_agendar = Button(
            self.frame_calendario,
            text="Clique aqui para agendar seu evento",
            command=self.funcoes.selecionar_data,
            font="monospace",
            bg="#BF4C0A",
            fg="#F2F2F0",
            width=50,
            height=2
        )
        self.botao_agendar.pack(padx=30, pady=15)

        self.janela.mainloop()


if __name__ == "__main__":
    interface = Interface()
