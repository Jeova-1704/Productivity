# Código para ser seguido nos projetos

# Importação das bibliotecas e outras necessidades: ==========================================================================================================================================

from tkinter import *
from utils import colors, fonts
from core import funcoes_pomodoro

# Inicalização da janela: ===============================================================================================================================================

janela = Tk()
janela.title( "POMODRO" )
janela.geometry( '1280x700' )
janela.config( background=colors.COR_BRANCA )
janela.resizable( width=False, height=False )
janela.iconbitmap( "assets/favicon.ico" )

# Continuação do codigo: ================================================================================================================================================
# 1 segmento de tela:
navbar = Frame( janela, width=1280, height=174, bg=colors.COR_CINZA_ESCURO )
navbar.pack()
Botao_Home = "Home"
label = Button( navbar, text=Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                font=fonts.fonte_h2,
                relief=FLAT, command=...
                )
label.place( x=625, y=50 )

Botao_Codigo = "DashBoard"
label = Button( navbar, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                font=fonts.fonte_h2,
                relief=FLAT )
label.place( x=800, y=50 )

Botao_Team = "Sobre"
label = Button( navbar, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                font=fonts.fonte_h2,
                command=..., relief=FLAT )
label.place( x=1068, y=50 )

# 2 segmento de tela:

frame_tempo = Frame( janela, width=1280, height=532, bg=colors.COR_BRANCA )
frame_tempo.pack()
img_tempo = PhotoImage( file="assets/pomodoro_tempo.png" )
label_tempo = Label( frame_tempo, image=img_tempo )
label_tempo.place( x=251, y=77.09 )

img_icon = PhotoImage( file="assets/Ellipse 4.png" )
button_icon = Button( frame_tempo, image=img_icon, relief="flat", command=funcoes_pomodoro.abrir_janela )
button_icon.place( x=150, y=40 )

label_temporizador = Label( frame_tempo, text="xx : xx", font=fonts.fonte_temporizador_p, fg=colors.COR_BRANCA,
                            bg=colors.COR_LARANJA_CLARO )
label_temporizador.place( x=300, y=200 )

img_start = PhotoImage( file="assets/botao_start_pomodoro.png" )
button_start = Button( frame_tempo, image=img_start, relief="flat", command=... )
button_start.place( x=365, y=350 )

# botao


'''button_start = Button(inf_tempo, text="START", command=src.temporizador())
button_start.place(x=363.28, y=493)
button_icon.pack()'''

# 3 segmento de tela:

img_intervalo = PhotoImage( file="assets/pomodoro_intervalos.png" )
label_intervalo = Label( frame_tempo, image=img_intervalo )
label_intervalo.place( x=800, y=112 )

qntd_intervalos = Label( label_intervalo, text=str( funcoes_pomodoro.v_intervalos ), font=fonts.fonte_h2_p,
                         fg=colors.COR_LARANJA_ESCURO, bg=colors.COR_BRANCA, relief="flat" )
qntd_intervalos.place( x=355, y=33 )

##############################


pC_botao = Button( janela, textvariable=msg, font=fonts.fonte_conteudo, fg=colors.COR_BRANCA, bg=colors.COR_LARANJA_ESCURO,
                   relief="raised", command=lambda: funcoes_pomodoro.botao_pausa_click( "pc_click" ) )
pC_botao.place( x=1160, y=396 )

pM_botao = Button( janela, textvariable=msg, font=fonts.fonte_conteudo, fg=colors.COR_BRANCA, bg=colors.COR_LARANJA_ESCURO,
                   relief="raised", command=lambda: funcoes_pomodoro.botao_pausa_click( "pm_click" ) )
pM_botao.place( x=1160, y=458 )

pL_botao = Button( janela, textvariable=msg, font=fonts.fonte_conteudo, fg=colors.COR_BRANCA, bg=colors.COR_LARANJA_ESCURO,
                   relief="raised", command=lambda: funcoes_pomodoro.botao_pausa_click( "pl_click" ) )
pL_botao.place( x=1160, y=519 )

def text_button():

    msg = StringVar()
    msg.set("X")

    if
        msg = "X"

# Ciclo da janela para ela ir atualizando: ==============================================================================================================================
print( funcoes_pomodoro.v_pomodoro )
janela.mainloop()
