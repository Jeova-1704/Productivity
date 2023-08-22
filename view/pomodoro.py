# Código para ser seguido nos projetos

# Importação das bibliotecas e outras necessidades: ==========================================================================================================================================

from tkinter import *

# variveis globais: =====================================================================================================================================================

COR_BRANCA = "#F2F2F0"
COR_CINZA_CLARO = "#A5A6A4"
COR_CINZA_ESCURO = "#737373"
COR_LARANJA_CLARO = "#BF8450"
COR_LARANJA_ESCURO = "#BF4C0A"
fonte_titulo = ('mulish', 22, 'bold')
fonte_conteudo = ('monospace', 16)

# Inicalização da janela: ===============================================================================================================================================

janela = Tk()
janela.title("POMODRO")
janela.geometry('1280x700')
janela.config(background=COR_BRANCA)
janela.resizable()
janela.iconbitmap("assets/favicon.ico")

# Continuação do codigo: ================================================================================================================================================
# 1 segmento de tela:
navbar = Frame(janela, width=1280, height=174, bg=COR_CINZA_ESCURO)
navbar.pack()

# 2 segmento de tela:
inf_tempo = Canvas(janela, width=389, height=389)
inf_tempo.place(x=251, y=233.91)
inf_tempo.create_oval(1, 1, 389, 389, fill=COR_LARANJA_CLARO, outline='')

frase_foco = Label(inf_tempo, text="# Bora focar!", fg=COR_BRANCA, font="Space Mono 20")
frase_foco.pack()

label0 = Label(inf_tempo, text=src.temporizador(), fg=COR_BRANCA, font="Space Mono 20")
# icon
imagem_pomodoro = PhotoImage(file="assets/Ellipse 4.png")
# Criar uma imagem sobreposta ao círculo
x_icon = 10  # Coordenada x da imagem
y_icon = 10  # Coordenada y da imagem
inf_tempo.create_image(x_icon, y_icon, image=imagem_pomodoro, anchor=NW)

button_icon = Button(inf_tempo, image=imagem_pomodoro, command=lambda: src.click_icon())
button_icon.pack()

# botao


'''button_start = Button(inf_tempo, text="START", command=src.temporizador())
button_start.place(x=363.28, y=493)
button_icon.pack()'''



# 3 segmento de tela:

tabela_pausa = Frame(janela, width=480, height=331, bg=COR_LARANJA_CLARO)
tabela_pausa.place(x=800, y=293.89)

frase_pausa = Label(tabela_pausa, text="Partiu dar uma pausa!", bg=COR_LARANJA_CLARO, fg=COR_BRANCA, font="Space Mono 20")
frase_pausa.pack()

label1 = Label(tabela_pausa, text="Intervalos", fg=COR_BRANCA, font="Space Mono 35")
label1.pack()
'''importar a imagem do circulo branco para botar no fundo de uma váriavel t que contabilizará o total de intervalos'''

label2 = Label(tabela_pausa, text="Pausa curta", fg=COR_BRANCA, font="Space Mono 30", bd=4, relief="sunken")
label2.pack()
label3 = Label(tabela_pausa, text="Pausa média", fg=COR_BRANCA, font="Space Mono 30", bd=4, relief="sunken")
label3.pack()
label4 = Label(tabela_pausa, text="Pausa longa", fg=COR_BRANCA, font="Space Mono 30", bd=4, relief="sunken")
label4.pack()
# Ciclo da janela para ela ir atualizando: ==============================================================================================================================

janela.mainloop()
