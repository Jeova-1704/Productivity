# Código para ser seguido nos projetos

# Importação das bibliotecas e outras necessidades:
# ==========================================================================================================================================

from tkinter import *
from typing import Any

from utils import colors, fonts
from core import funcoes_pomodoro, funcoes_main


# Inicalização da janela:
# ===============================================================================================================================================


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry( f"{width}x{height}+{x}+{y}" )


class InterfacePomodoro():
    width = 1280
    height = 700

    def __init__(self):
        self.janela = Tk()
        self.janela.title( "POMODRO" )
        self.width = 1280
        self.height = 700
        center_window( self.janela, self.width, self.height )
        self.janela.config( background=colors.COR_BRANCA )
        self.janela.resizable( width=False, height=False )
        self.janela.iconbitmap( "assets/favicon.ico" )

        # variaveis do pomodoro:

        self._numero_ciclos = 0
        self._v_ciclos = 4
        self._t_pomodoro = 25
        self.t_pomodoro_int = 25
        self._t_pausa = 5
        self._t_pausaC = 5
        self._t_pausaM = 10
        self._t_pausaL = 15
        self.segundos_int = 0
        self.minutos_int = 0
        self._segundos = IntVar()
        self._minutos = IntVar()
        self.check_pc = StringVar()
        self.check_pc.set("  ")
        self.check_pm = StringVar()
        self.check_pm.set("  ")
        self.check_pl = StringVar()
        self.check_pl.set("  ")

        # Continuação do codigo:
        # ================================================================================================================================================ 1 segmento de tela:
        self.navbar = Frame( self.janela, width=1280, height=174, bg=colors.COR_CINZA_ESCURO )
        self.navbar.pack()

        self.Texto_Productivity = "Productivity"
        self.label = Label(self.navbar, text=self.Texto_Productivity, fg=colors.COR_BRANCA,
                           bg=colors.COR_CINZA_ESCURO,
                           font=fonts.fonte_conteudo_logo)
        self.label.place(x=34, y=50)

        self.Botao_Home = "Home"
        self.label = Button( self.navbar, text=self.Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                             font=fonts.fonte_h2,
                             relief=FLAT, command=lambda: funcoes_main.renderizar_home( self.janela )
                             )
        self.label.place( x=625, y=50 )

        self.Botao_Codigo = "DashBoard"
        self.label = Button( self.navbar, text=self.Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                             font=fonts.fonte_h2,
                             relief=FLAT )
        self.label.place( x=800, y=50 )

        self.Botao_Team = "Sobre"
        self.label = Button( self.navbar, text=self.Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                             font=fonts.fonte_h2,
                             command=..., relief=FLAT )
        self.label.place( x=1068, y=50 )

        # 2 segmento de tela:

        self.frame_tempo = Frame( self.janela, width=1280, height=532, bg=colors.COR_BRANCA )
        self.frame_tempo.pack()
        self.img_tempo = PhotoImage( file="assets/pomodoro_tempo.png" )
        self.label_tempo = Label( self.frame_tempo, image=self.img_tempo )
        self.label_tempo.place( x=235, y=64.09 )

        self.img_icon = PhotoImage( file="assets/pomodoro.png" )
        self.button_icon = Button( self.frame_tempo, image=self.img_icon, relief="flat",
                                   command=funcoes_pomodoro.abrir_janela )
        self.button_icon.place( x=125, y=46 )

        self.label_temporizador = Label( self.frame_tempo, text="00 : 00",
                                         font=fonts.fonte_temporizador_p,
                                         fg=colors.COR_BRANCA,
                                         bg=colors.COR_LARANJA_CLARO )
        self.label_temporizador.place( x=280, y=170 )

        self.img_start = PhotoImage( file="assets/botao_start_pomodoro.png" )
        self.button_start = Button( self.frame_tempo, image=self.img_start, relief="flat",command=lambda: funcoes_pomodoro.iniciarPomodoro(self.label_temporizador,self.t_pomodoro_int))
        self.button_start.place( x=350, y=330 )

        # 3 segmento de tela:

        self.img_info = PhotoImage( file="assets/info_pomodoro.png" )
        self.label_info = Label( self.janela, image=self.img_info )
        self.label_info.place( x=878, y=195 )

        # 4 segmento de tela:

        self.img_intervalo = PhotoImage( file="assets/pomodoro_intervalos.png" )
        self.label_intervalo = Label( self.frame_tempo, image=self.img_intervalo )
        self.label_intervalo.place( x=800, y=190 )

        self.qntd_intervalos = Label( self.label_intervalo, textvariable=self.v_ciclos,
                                      font=fonts.fonte_h2_p,
                                      fg=colors.COR_LARANJA_ESCURO, bg=colors.COR_BRANCA, relief="flat")
        self.qntd_intervalos.place( x=355, y=33 )

        self.pC_botao = Button( self.janela, textvariable=self.check_pc, font=fonts.fonte_conteudo,
                                fg=colors.COR_BRANCA,
                                bg=colors.COR_LARANJA_ESCURO,
                                relief="raised", command=lambda: self.selecaoDeTempo( "pc" ) )
        self.pC_botao.place( x=1160, y=474 )

        self.pM_botao = Button( self.janela, textvariable=self.check_pm, font=fonts.fonte_conteudo,
                                fg=colors.COR_BRANCA,
                                bg=colors.COR_LARANJA_ESCURO,
                                relief="raised", command=lambda: self.selecaoDeTempo( "pm" ) )
        self.pM_botao.place( x=1160, y=535 )

        self.pL_botao = Button( self.janela, textvariable=self.check_pl, font=fonts.fonte_conteudo,
                                fg=colors.COR_BRANCA,
                                bg=colors.COR_LARANJA_ESCURO,
                                relief="raised", command=lambda: self.selecaoDeTempo( "pl" ) )
        self.pL_botao.place( x=1160, y=596 )

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
        elif verificador == "pl":
            self.check_pc.set("  ")
            self.check_pm.set("  ")
            self.check_pl.set("X")

    # Métodos getter
    @property
    def numero_ciclos(self):
        return self._numero_ciclos

    @property
    def v_ciclos(self):
        return self._v_ciclos

    @property
    def t_pomodoro(self):
        return self._t_pomodoro

    @property
    def t_pausa(self):
        return self._t_pausa

    @property
    def t_pausaC(self):
        return self._t_pausaC

    @property
    def t_pausaM(self):
        return self._t_pausaM

    @property
    def t_pausaL(self):
        return self._t_pausaL

    @property
    def segundos(self):
        return self._segundos

    @property
    def minutos(self):
        return self._minutos

    # Métodos setter
    @numero_ciclos.setter
    def numero_ciclos(self, value):
        self._numero_ciclos = value

    @v_ciclos.setter
    def v_ciclos(self, value):
        self._v_ciclos = value

    @t_pomodoro.setter
    def t_pomodoro(self, value):
        self._t_pomodoro = value

    @t_pausa.setter
    def t_pausa(self, value):
        self._t_pausa = value

    @t_pausaC.setter
    def t_pausaC(self, value):
        self._t_pausaC = value

    @t_pausaM.setter
    def t_pausaM(self, value):
        self._t_pausaM = value

    @t_pausaL.setter
    def t_pausaL(self, value):
        self._t_pausaL = value

    @segundos.setter
    def segundos(self, value):
        self._segundos = value

    @minutos.setter
    def minutos(self, value):
        self._minutos = value




if __name__ == "__main__":
    pomodoro = InterfacePomodoro()
