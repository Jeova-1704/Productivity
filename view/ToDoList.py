from tkinter import *
from PIL import ImageTk, Image

from core import funcoes_todolist
from utils import PadraoProjeto

janela = Tk()
janela.title("To-Do List")
janela.geometry('1280x700')
janela.config(background=PadraoProjeto.COR_CINZA_ESCURO)
janela.resizable(width=FALSE, height=FALSE)

frame_topo = Frame(janela, width=1280, height=150, bg=PadraoProjeto.COR_CINZA_ESCURO, relief=SOLID)
frame_topo.pack()

frame_meio = Frame(janela, width=1280, height=550, bg=PadraoProjeto.COR_BRANCA, relief=SOLID)
frame_meio.pack()

frame_tarefas = Frame(frame_meio, width=600, height=500, bg=PadraoProjeto.COR_LARANJA_CLARO)
frame_tarefas.place(x=660, y=25)

linha_vertical = Label(frame_meio, relief=GROOVE, width=0, height=255, anchor=NW, font='Ivy 1',
                       bg=PadraoProjeto.COR_LARANJA_ESCURO, fg=PadraoProjeto.COR_CINZA_ESCURO)
linha_vertical.place(x=640, y=15)

linha_horizontal = Label(frame_meio, relief=GROOVE, width=350, height=0, anchor=NW, font='Ivy 1',
                         bg=PadraoProjeto.COR_LARANJA_ESCURO, fg=PadraoProjeto.COR_CINZA_ESCURO)
linha_horizontal.place(x=152, y=190)

img_logo = Image.open('assets/toDoList_logo.png')
img_logo = ImageTk.PhotoImage(img_logo)
imagem_logo = Label(frame_meio, image=img_logo, compound=LEFT, anchor=NW)
imagem_logo.place(x=165, y=10)

texto_todolist = Label(frame_meio, text="To-Do List", font=PadraoProjeto.fonte_titulo)
texto_todolist.place(x=255, y=25)

texto_entrada_idTask = Label(frame_meio, text='ID da tarefa:', anchor=NW, font=PadraoProjeto.fonte_conteudo,
                             bg=PadraoProjeto.COR_BRANCA)
texto_entrada_idTask.place(x=200, y=225)
Entrada_idTask = Entry(frame_meio, width=7, justify='center', relief=SOLID, font=PadraoProjeto.fonte_conteudo)
Entrada_idTask.place(x=340, y=225)

img_add = Image.open('assets/toDoList_add.png')
img_add = img_add.resize((35, 35))
img_add = ImageTk.PhotoImage(img_add)
botao_add = Button(frame_meio, image=img_add, command=funcoes_todolist.addTarefa, relief=GROOVE, text="Adicionar Tarefa", width=300,
                   compound=LEFT, overrelief=RIDGE, font=PadraoProjeto.fonte_conteudo,
                   bg=PadraoProjeto.COR_LARANJA_CLARO, fg=PadraoProjeto.COR_BRANCA)
botao_add.place(x=175, y=120)

img_update = Image.open('assets/toDoList_update.png')
img_update = img_update.resize((35, 35))
img_update = ImageTk.PhotoImage(img_update)
botao_add = Button(frame_meio, image=img_update, command=..., relief=GROOVE, text="Atualizar Tarefa", width=300,
                   compound=LEFT, overrelief=RIDGE, font=PadraoProjeto.fonte_conteudo,
                   bg=PadraoProjeto.COR_LARANJA_CLARO, fg=PadraoProjeto.COR_BRANCA)
botao_add.place(x=175, y=290)

img_delete = Image.open('assets/toDoList_delete.png')
img_delete = img_delete.resize((35, 35))
img_delete = ImageTk.PhotoImage(img_delete)
botao_delete = Button(frame_meio, command=..., image=img_delete, relief=GROOVE, text="Deletar Tarefa", width=300, compound=LEFT,
                      overrelief=RIDGE, font=PadraoProjeto.fonte_conteudo,
                      bg=PadraoProjeto.COR_LARANJA_CLARO, fg=PadraoProjeto.COR_BRANCA)
botao_delete.place(x=175, y=370)

img_all_delete = Image.open('assets/toDoList_danger.png')
img_all_delete = img_all_delete.resize((35, 35))
img_all_delete = ImageTk.PhotoImage(img_all_delete)
botao_all_delete = Button(frame_meio, command=..., image=img_all_delete, relief=GROOVE, text="Deletar todas as tarefas",
                          width=300, compound=LEFT, overrelief=RIDGE, font=PadraoProjeto.fonte_conteudo,
                          bg=PadraoProjeto.COR_LARANJA_CLARO, fg=PadraoProjeto.COR_BRANCA)
botao_all_delete.place(x=175, y=450)

janela.mainloop()
