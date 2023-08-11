# Importação das bibliotecas e outras necessidades:=====================================================================

from tkinter import *
from PIL import ImageTk, Image

# variveis globais:=====================================================================================================

COR_BRANCA = "#F2F2F0"
COR_CINZA_CLARO = "#A5A6A4"
COR_CINZA_ESCURO = "#737373"
COR_LARANJA_CLARO = "#BF8450"
COR_LARANJA_ESCURO = "#BF4C0A"
fonte_titulo = ('mulish', 32, 'bold')
fonte_conteudo = ('monospace', 16)

# Inicalização da janela:===============================================================================================

janela = Tk()
janela.title("To-Do List")
janela.geometry('1280x700')
janela.config(background=COR_CINZA_ESCURO)
janela.resizable(width=FALSE, height=FALSE)

# Desenvolvimento da janela:============================================================================================

# Frames
frame_topo = Frame(janela, width=1280, height=150, bg=COR_CINZA_ESCURO, relief=SOLID)
frame_topo.pack()

frame_meio = Frame(janela, width=1280, height=550, bg=COR_BRANCA, relief=SOLID)
frame_meio.pack()

frame_input_detalhes = ...

frame_visualizar_tarefas =...

# criando a Linha separadora
l_linha = Label(frame_meio, relief=GROOVE, width=0, height=255, anchor=NW, font='Ivy 1', bg=COR_LARANJA_ESCURO, fg=COR_CINZA_ESCURO)
l_linha.place(x=640, y=15)


# Adicionar imagem
img_logo = Image.open('images/logo.png')
img_logo = ImageTk.PhotoImage(img_logo)
imagem_logo = Label(frame_meio, image=img_logo, compound=LEFT, anchor=NW)
imagem_logo.place(x=5, y=10)







# Ciclo da janela para ela ir atualizando:=============================================================================

janela.mainloop()
