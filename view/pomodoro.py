from tkinter import *
from utils import colors, fonts
from core import funcoes_pomodoro, funcoes_main


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


class InterfacePomodoro:
    width = 1280
    height = 700

    def __init__(self):
        self.janela = Tk()
        self.janela.title("POMODRO")
        self.width = 1280
        self.height = 700
        center_window(self.janela, self.width, self.height)
        self.janela.resizable(width=FALSE, height=FALSE)
        self.janela.config(background=colors.COR_BRANCA)
        self.janela.iconbitmap("assets/IconPomodoro.ico")

        self.numero_ciclos = funcoes_pomodoro.numero_ciclos
        self.t_pomodoro = 1
        self.t_pomodoro_int = funcoes_pomodoro.t_pomodoro_int
        self.t_pausa = 5
        self.tempo_pl = None
        self.tempo_pm = None
        self.duracao_pausaC = funcoes_pomodoro.duracao_pausaC
        self.duracao_pausaM = funcoes_pomodoro.duracao_pausaM
        self.duracao_pausaL = funcoes_pomodoro.duracao_pausaL
        self.segundos_int = 0
        self.minutos_int = 0
        self.qtd_intervalos_label = IntVar()
        self.qtd_intervalos_label.set(self.numero_ciclos)
        self.check_pc = StringVar()
        self.check_pc.set("X")
        self.check_pm = StringVar()
        self.check_pm.set("  ")
        self.check_pl = StringVar()
        self.check_pl.set("  ")

        self.navbar = Frame(self.janela, width=1280, height=174, bg=colors.COR_CINZA_ESCURO)
        self.navbar.pack()

        self.Texto_Productivity = "Productivity"
        self.label = Label(self.navbar, text=self.Texto_Productivity, fg=colors.COR_BRANCA,
                           bg=colors.COR_CINZA_ESCURO,
                           font=fonts.fonte_conteudo_logo)
        self.label.place(x=34, y=50)

        self.Botao_Home = "Home"
        self.label = Button(self.navbar, text=self.Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela)
                            )
        self.label.place(x=625, y=50)

        self.Botao_Codigo = "DashBoard"
        self.label = Button(self.navbar, text=self.Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            relief=FLAT,
                            command=lambda: funcoes_main.renderizar_dashboard(self.janela))
        self.label.place(x=800, y=50)

        self.Botao_Team = "Sobre"
        self.label = Button(self.navbar, text=self.Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            command=lambda: funcoes_main.renderizar_team(self.janela), relief=FLAT)
        self.label.place(x=1068, y=50)

        self.frame_tempo = Frame(self.janela, width=1280, height=532, bg=colors.COR_BRANCA)
        self.frame_tempo.pack()
        self.img_tempo = PhotoImage(file="assets/LabelPomodoroTime.png")
        self.label_tempo = Label(self.frame_tempo, image=self.img_tempo)
        self.label_tempo.place(x=235, y=64.09)

        self.img_icon = PhotoImage(file="assets/EllipsePomodoro.png")
        self.button_icon = Button(self.frame_tempo, image=self.img_icon, relief="flat",
                                  command=lambda: funcoes_pomodoro.abrir_janela(self.janela))
        self.button_icon.place(x=44, y=36)

        self.text_temporizador = '{:02d} : {:02d}'.format(self.minutos_int, self.segundos_int)
        self.label_temporizador = Label(self.frame_tempo, text=self.text_temporizador,
                                        font=fonts.fonte_temporizador_p,
                                        fg=colors.COR_BRANCA,
                                        bg=colors.COR_LARANJA_CLARO)
        self.label_temporizador.place(x=280, y=170)
        self.img_start = PhotoImage(file="assets/LabelPomodoroStart.png")
        self.button_start = Button(self.frame_tempo, image=self.img_start, relief="flat",
                                   command=lambda: funcoes_pomodoro.iniciarPomodoro(self.label_temporizador,
                                                                                    self.t_pomodoro_int, self.janela,
                                                                                    self.numero_ciclos,
                                                                                    self.qntd_intervalos,
                                                                                    self.tempo_pm, self.tempo_pl,
                                                                                    self.duracao_pausaC,
                                                                                    self.duracao_pausaM,
                                                                                    self.duracao_pausaL))
        self.button_start.place(x=350, y=330)

        self.img_info = PhotoImage(file="assets/LabelPadroesPomodoro.png")
        self.label_info = Label(self.janela, image=self.img_info)
        self.label_info.place(x=828, y=195)

        self.img_intervalo = PhotoImage(file="assets/LabelPomodoroInterval.png")
        self.label_intervalo = Label(self.frame_tempo, image=self.img_intervalo)
        self.label_intervalo.place(x=800, y=190)

        self.qntd_intervalos = Label(self.label_intervalo,
                                     text = self.numero_ciclos,
                                     font=fonts.fonte_h2_p,
                                     fg=colors.COR_LARANJA_ESCURO, bg=colors.COR_BRANCA, relief="flat")
        self.qntd_intervalos.place(x=355, y=33)



        self.pC_botao = Button(self.janela, textvariable=self.check_pc, font=fonts.fonte_conteudo,
                               fg=colors.COR_BRANCA,
                               bg=colors.COR_LARANJA_ESCURO,
                               relief="raised", command=lambda: self.selecaoDeTempo("pc"))
        self.pC_botao.place(x=1160, y=474)

        self.pM_botao = Button(self.janela, textvariable=self.check_pm, font=fonts.fonte_conteudo,
                               fg=colors.COR_BRANCA,
                               bg=colors.COR_LARANJA_ESCURO,
                               relief="raised", command=lambda: self.selecaoDeTempo("pm"))
        self.pM_botao.place(x=1160, y=535)

        self.pL_botao = Button(self.janela, textvariable=self.check_pl, font=fonts.fonte_conteudo,
                               fg=colors.COR_BRANCA,
                               bg=colors.COR_LARANJA_ESCURO,
                               relief="raised", command=lambda: self.selecaoDeTempo("pl"))
        self.pL_botao.place(x=1160, y=596)
        self.qntd_intervalos.config(text=self.numero_ciclos)

        self.janela.mainloop()

    def selecaoDeTempo(self, verificador):

        if verificador == "pc":
            self.check_pc.set("X")
            self.check_pm.set("  ")
            self.check_pl.set("  ")


        elif verificador == "pm":
            self.check_pc.set("  ")
            self.check_pm.set("X")
            self.check_pl.set("  ")
            self.tempo_pm = True

        elif verificador == "pl":
            self.check_pc.set("  ")
            self.check_pm.set("  ")
            self.check_pl.set("X")
            self.tempo_pl = True

        self.qntd_intervalos.config(text=self.numero_ciclos)

