from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

from dao.bdToDoList import ToDOStatus

# Variaveis gerais
COR_BRANCA = "#F2F2F0"
COR_CINZA_CLARO = "#A5A6A4"
COR_CINZA_ESCURO = "#737373"
COR_LARANJA_CLARO = "#BF8450"
COR_LARANJA_ESCURO = "#BF4C0A"
fonte_titulo = ('mulish', 25, 'bold')
fonte_conteudo = ('monospace', 17)
status = ['Não iniciada', 'Em andamento', 'Concluida']
nivel_importancia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bancoDeDadosTodoList = ToDOStatus()


def salvarTarefa():
    ...


def addTarefa():
    janela_dados = Toplevel()
    janela_dados.geometry('500x500')
    janela_dados.title("Cadastro de tarefas")
    janela_dados.resizable(height=FALSE, width=FALSE)
    janela_dados.config(background=COR_BRANCA)

    # Frames
    frame_top = Frame(janela_dados, width=500, height=80, bg=COR_LARANJA_CLARO, relief=SOLID)
    frame_top.pack()

    frame_meio = Frame(janela_dados, width=500, height=420, bg=COR_BRANCA, relief=SOLID)
    frame_meio.pack()

    # Texto da janela
    titulo = Label(frame_top, text="Cadastro de tarefas", font=fonte_titulo, bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
    titulo.place(x=90, y=20)

    # entry dos valores (idTask, tarefa, status, descrição, nivel_de_importancia)
    titulo_tarefa = Label(frame_meio, text='Tarefa:', anchor=NW, font=fonte_conteudo, bg=COR_BRANCA)
    titulo_tarefa.place(x=50, y=50)
    Entrada_tarefa = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=fonte_conteudo)
    Entrada_tarefa.place(x=165, y=50)

    titulo_descricao = Label(frame_meio, text='Descrição:', anchor=NW, font=fonte_conteudo, bg=COR_BRANCA)
    titulo_descricao.place(x=50, y=100)
    Entrada_descricao = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=fonte_conteudo)
    Entrada_descricao.place(x=165, y=100)

    titulo_status = Label(frame_meio, text='Status:', anchor=NW, font=fonte_conteudo, bg=COR_BRANCA)
    titulo_status.place(x=50, y=150)
    Entrada_status = ttk.Combobox(frame_meio, width=20, font=fonte_conteudo, justify=CENTER)
    Entrada_status['values'] = status
    Entrada_status.place(x=165, y=150)

    titulo_nivel = Label(frame_meio, text='Nivel de importancia:', anchor=NW, font=fonte_conteudo, bg=COR_BRANCA)
    titulo_nivel.place(x=50, y=200)
    Entrada_nivel = ttk.Combobox(frame_meio, width=5, font=fonte_conteudo, justify=CENTER)
    Entrada_nivel['values'] = nivel_importancia
    Entrada_nivel.place(x=270, y=200)

    # Linha de divisão para
    linha_horizontal = Label(frame_meio, relief=GROOVE, width=400, height=0, anchor=NW, font='Ivy 1',
                             bg=COR_LARANJA_ESCURO, fg=COR_CINZA_ESCURO)
    linha_horizontal.place(x=50, y=250)

    #Botao de salvar
    img_salvar = Image.open('../view/assets/toDoList_save.png')
    img_salvar = img_salvar.resize((35, 35))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    botao_salvar = Button(frame_meio, command=..., image=img_salvar, relief=GROOVE, text="Salvar", width=300,
                          compound=LEFT,
                          overrelief=RIDGE, font=fonte_conteudo,
                          bg=COR_LARANJA_CLARO, fg=COR_BRANCA)
    botao_salvar.place(x=100, y=300)

    janela_dados.mainloop()
