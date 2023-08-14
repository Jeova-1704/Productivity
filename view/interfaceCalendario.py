from tkinter import *
from tkcalendar import Calendar
from core.coreCalendario import Funcoes

class Interface:

    COR_BRANCA = "#F2F2F0"
    COR_CINZA_CLARO = "#A5A6A4"
    COR_CINZA_ESCURO = "#737373"
    COR_LARANJA_CLARO = "#BF8450"
    COR_LARANJA_ESCURO = "#BF4C0A"
    fonte_titulo = ("mulish", 22, "bold")
    fonte_conteudo = ("monospace", 16)

    def __init__(self):
        self.janela = Tk()
        self.janela.title("Calendário")
        self.janela.geometry("1280x700")
        self.janela.config(background=self.COR_BRANCA)
        self.janela.resizable(width="FALSE", height="FALSE")

        self.frame_top = Frame(self.janela, width=1280, height=125, bg=self.COR_BRANCA, relief=SOLID)
        self.frame_top.pack(padx=0, pady=0)

        self.frame_detalhes = Frame(self.frame_top, width=1280, height=174, bg=self.COR_CINZA_ESCURO, relief=SOLID)
        self.frame_detalhes.pack(padx=0, pady=0)

        self.Texto_Productivity = "Productivity"
        self.label_productivity = Label(self.frame_top, text=self.Texto_Productivity, fg=self.COR_BRANCA, bg=self.COR_CINZA_ESCURO, font=('monospace', 40))
        self.label_productivity.place(x=34, y=50)

        self.Botao_Home = "Home"
        self.label_home = Button(self.frame_top, text=self.Botao_Home, fg=self.COR_BRANCA, bg=self.COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
        self.label_home.place(x=625, y=50)

        self.Botao_Codigo = "Código"
        self.label_codigo = Button(self.frame_top, text=self.Botao_Codigo, fg=self.COR_BRANCA, bg=self.COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
        self.label_codigo.place(x=846, y=50)

        self.Botao_Team = "Team"
        self.label_team = Button(self.frame_top, text=self.Botao_Team, fg=self.COR_BRANCA, bg=self.COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
        self.label_team.place(x=1068, y=50)

        self.frame_detalhes_borda = Frame(self.frame_top, width=1280, height=4, bg=self.COR_CINZA_CLARO, relief=SOLID)
        self.frame_detalhes_borda.pack(padx=0, pady=0)

        self.frame_calendario = Frame(self.janela, bg=self.COR_BRANCA)
        self.frame_calendario.pack(side="left", fill="both", expand=True)

        self.frame_tabela = Frame(self.janela, width=200, height=100, bg=self.COR_CINZA_CLARO, relief=SOLID)
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

        self.funcoes = Funcoes(self.frame_calendario, self.cal, self.frame_tabela)

        self.botao_agendar = Button(
            self.frame_calendario,
            text="Clique aqui para agendar seu evento",
            command=self.funcoes.selecionar_data,
            font=self.fonte_conteudo
        )
        self.botao_agendar.pack(padx=5, pady=5)

        self.janela.mainloop()

if __name__ == "__main__":
    interface = Interface()
