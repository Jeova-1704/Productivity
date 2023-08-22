# Código para ser seguido nos projetos

# Importação das bibliotecas e outras necessidades: ==========================================================================================================================================

from tkinter import *
from utils import colors, fonts

# Inicalização da janela: ===============================================================================================================================================

janela = Tk()
janela.title("POMODRO")
janela.geometry('1280x700')
janela.config(background=colors.COR_BRANCA)
janela.resizable(width=False, height=False)
janela.iconbitmap("assets/favicon.ico")



# Continuação do codigo: ================================================================================================================================================
# 1 segmento de tela:
navbar = Frame(janela, width=1280, height=174, bg=colors.COR_CINZA_ESCURO)
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

frame_tempo = Frame(janela,  width=1280, height=532, bg=colors.COR_BRANCA)
frame_tempo.pack()
img_tempo = PhotoImage(file="assets/pomodoro_tempo.png")
label_tempo = Label(frame_tempo,image=img_tempo)
label_tempo.place(x=251, y=77.09)

img_icon = PhotoImage(file="assets/Ellipse 4.png")
button_icon = Button(frame_tempo, image=img_icon, relief=FLAT)
button_icon.place(x=265.73, y=70)


# botao


'''button_start = Button(inf_tempo, text="START", command=src.temporizador())
button_start.place(x=363.28, y=493)
button_icon.pack()'''



# 3 segmento de tela:

img_intervalo = PhotoImage(file="assets/pomodoro_intervalos.png")
label_intervalo = Label(frame_tempo,image=img_intervalo)
label_intervalo.place(x=800, y=112)

# Ciclo da janela para ela ir atualizando: ==============================================================================================================================

janela.mainloop()
