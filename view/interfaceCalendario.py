from tkinter import *
from tkcalendar import Calendar
from core.coreCalendario import Funcoes


class Interface:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Calendário")
        self.janela.geometry("1280x700")
        self.janela.config(background='#F2F2F0')
        self.janela.resizable(width=FALSE, height=FALSE)

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

        self.funcoes = Funcoes(self.frame_calendario, self.cal, self.frame_tabela, self.janela)

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
