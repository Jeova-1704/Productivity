# Código para ser seguido nos projetos

# Importação das bibliotecas e outras necessidades: ==========================================================================================================================================

from tkinter import *
from utils import colors, fonts
from core import funcoes_pomodoro,funcoes_main

# Inicalização da janela: ===============================================================================================================================================


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


class InterfacePomodoro():
    width = 1280
    height = 700

    def __init__(self):
        self.janela = Tk()
        self.janela.title("POMODRO")
        self.width = 1280
        self.height = 700
        center_window(self.janela, self.width, self.height)
        self.janela.config(background=colors.COR_BRANCA)
        self.janela.resizable(width=False, height=False)
        self.janela.iconbitmap("assets/favicon.ico")
        # variaveis do pomodoro:

        self.numero_ciclos = 0
        self.v_ciclos = IntVar()
        self.v_ciclos = 4
        self.t_pomodoro = 25
        self.t_pausa = 5
        self.t_pausaC = 5
        self.t_pausaM = 10
        self.t_pausaL = 15

        # Continuação do codigo: ================================================================================================================================================
        # 1 segmento de tela:
        self.navbar = Frame(self.janela, width=1280, height=174, bg=colors.COR_CINZA_ESCURO)
        self.navbar.pack()
        self.Botao_Home = "Home"
        self.label = Button(self.navbar, text=self.Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_h2,
                            relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela)
                            )
        self.label.place(x=625, y=50)

        self.Botao_Codigo = "DashBoard"
        self.label = Button(self.navbar, text=self.Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_h2,
                            relief=FLAT)
        self.label.place(x=800, y=50)

        self.Botao_Team = "Sobre"
        self.label = Button(self.navbar, text=self.Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_h2,
                            command=..., relief=FLAT)
        self.label.place(x=1068, y=50)

        # 2 segmento de tela:

        self.frame_tempo = Frame(self.janela, width=1280, height=532, bg=colors.COR_BRANCA)
        self.frame_tempo.pack()
        self.img_tempo = PhotoImage(file="assets/pomodoro_tempo.png")
        self.label_tempo = Label(self.frame_tempo, image=self.img_tempo)
        self.label_tempo.place(x=251, y=77.09)

        self.img_icon = PhotoImage(file="assets/Ellipse 4.png")
        self.button_icon = Button(self.frame_tempo, image=self.img_icon, relief="flat",
                                  command=funcoes_pomodoro.abrir_janela)
        self.button_icon.place(x=150, y=40)

        self.label_temporizador = Label(self.frame_tempo, text="xx : xx", font=fonts.fonte_temporizador_p,
                                        fg=colors.COR_BRANCA,
                                        bg=colors.COR_LARANJA_CLARO)
        self.label_temporizador.place(x=300, y=200)

        self.img_start = PhotoImage(file="assets/botao_start_pomodoro.png")
        self.button_start = Button(self.frame_tempo, image=self.img_start, relief="flat", command=...)
        self.button_start.place(x=365, y=350)

        self.img_intervalo = PhotoImage(file="assets/pomodoro_intervalos.png")
        self.label_intervalo = Label(self.frame_tempo, image=self.img_intervalo)
        self.label_intervalo.place(x=800, y=112)

        self.qntd_intervalos = Label(self.label_intervalo, textvariable=self.v_ciclos,
                                     font=fonts.fonte_h2_p,
                                     fg=colors.COR_LARANJA_ESCURO, bg=colors.COR_BRANCA, relief="flat")
        self.qntd_intervalos.place(x=355, y=33)

        msg = StringVar()
        msg.set("X")
        self.pC_botao = Button(self.janela, textvariable=msg, font=fonts.fonte_conteudo, fg=colors.COR_BRANCA,
                               bg=colors.COR_LARANJA_ESCURO,
                               relief="raised", command=...)
        self.pC_botao.place(x=1160, y=396)

        self.pM_botao = Button(self.janela, textvariable=msg, font=fonts.fonte_conteudo, fg=colors.COR_BRANCA,
                               bg=colors.COR_LARANJA_ESCURO,
                               relief="raised", command=...)
        self.pM_botao.place(x=1160, y=458)

        self.pL_botao = Button(self.janela, textvariable=msg, font=fonts.fonte_conteudo, fg=colors.COR_BRANCA,
                               bg=colors.COR_LARANJA_ESCURO,
                               relief="raised", command=...)
        self.pL_botao.place(x=1160, y=519)

        self.janela.mainloop()

