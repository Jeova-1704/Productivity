# Importação das bibliotecas e outras necessidades:=====================================================================

from tkinter import *
from PIL import ImageTk, Image

from funcoes import *

# variveis globais:=====================================================================================================

COR_BRANCA = "#F2F2F0"
COR_CINZA_CLARO = "#A5A6A4"
COR_CINZA_ESCURO = "#737373"
COR_LARANJA_CLARO = "#BF8450"
COR_LARANJA_ESCURO = "#BF4C0A"
fonte_titulo = ('mulish', 32, 'bold')
fonte_conteudo = ('monospace', 17)

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

# criando a Linha separadora
linha_vertical = Label(frame_meio, relief=GROOVE, width=0, height=255, anchor=NW, font='Ivy 1', bg=COR_LARANJA_ESCURO, fg=COR_CINZA_ESCURO)
linha_vertical.place(x=640, y=15)

linha_horizontal = Label(frame_meio, relief=GROOVE, width=350, height=0, anchor=NW, font='Ivy 1', bg=COR_LARANJA_ESCURO, fg=COR_CINZA_ESCURO)
linha_horizontal.place(x=152, y=190)

# Adicionar imagem
img_logo = Image.open('../images/logo.png')
img_logo = ImageTk.PhotoImage(img_logo)
imagem_logo = Label(frame_meio, image=img_logo, compound=LEFT, anchor=NW)
imagem_logo.place(x=165, y=10)

# Adicionar texto
texto_todolist = Label(frame_meio, text="To-Do List", font=fonte_titulo)
texto_todolist.place(x=255, y=25)

# Adicionando entradas da pesquisa
texto_entrada_idTask = Label(frame_meio, text='ID da tarefa:', anchor=NW, font=fonte_conteudo, bg=COR_BRANCA)
texto_entrada_idTask.place(x=180, y=225)
Entrada_idTask = Entry(frame_meio, width=7, justify='center', relief=SOLID, font=fonte_conteudo)
Entrada_idTask.place(x=320, y=225)



# Botões das funções
img_add = Image.open('../images/add.png')
img_add = img_add.resize((35, 35))
img_add = ImageTk.PhotoImage(img_add)
botao_add = Button(frame_meio, image=img_add, command=addTarefa, relief=GROOVE, text="Adicionar Tarefa", width=300, compound=LEFT,
                   overrelief=RIDGE, font=fonte_conteudo,
                   bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
botao_add.place(x=175, y=120)

img_pesquisa = Image.open('../images/pesquisar.png')
img_pesquisa = img_pesquisa.resize((35, 35))
img_pesquisa = ImageTk.PhotoImage(img_pesquisa)
botao_pesquisar = Button(frame_meio, image=img_pesquisa, command=..., relief=GROOVE, width=50, compound=RIGHT,
                         overrelief=RIDGE, font=fonte_conteudo,
                         bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
botao_pesquisar.place(x=425, y=219)

img_update = Image.open('../images/update.png')
img_update = img_update.resize((35, 35))
img_update = ImageTk.PhotoImage(img_update)
botao_add = Button(frame_meio, image=img_update, command=..., relief=GROOVE, text="Atualizar Tarefa", width=300, compound=LEFT,
                   overrelief=RIDGE, font=fonte_conteudo,
                   bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
botao_add.place(x=175, y=290)

img_delete = Image.open('../images/delete.png')
img_delete = img_delete.resize((35, 35))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button(frame_meio, command=..., image=img_delete, relief=GROOVE, text="Deletar Tarefa", width=300, compound=LEFT,
                      overrelief=RIDGE, font=fonte_conteudo,
                      bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
botao_delete.place(x=175, y=370)

img_all_delete = Image.open('../images/danger.png')
img_all_delete = img_all_delete.resize((35, 35))
img_all_delete = ImageTk.PhotoImage(img_all_delete)
botao_all_delete = Button(frame_meio, command=..., image=img_all_delete, relief=GROOVE, text="Deletar todas as tarefas", width=300, compound=LEFT,
                      overrelief=RIDGE, font=fonte_conteudo,
                      bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
botao_all_delete.place(x=175, y=450)



# Ciclo da janela para ela ir atualizando:=============================================================================

janela.mainloop()
