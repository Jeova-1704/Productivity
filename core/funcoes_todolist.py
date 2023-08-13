import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from utils import PadraoProjeto
from dao import bdToDoList



def salvar_tarefa(Entrada_tarefa, Entrada_descricao, Entrada_status, Entrada_nivel, janela):
    try:
        tarefa = str(Entrada_tarefa.get())
        descricao = str(Entrada_descricao.get())
        status = str(Entrada_status.get())
        nivel = int(Entrada_nivel.get())
        lista_para_banco_dados = [tarefa, status, descricao, nivel]
        bdToDoList.ToDoList_banco.registroDeTarefas(lista_para_banco_dados)
        janela.destroy()
    except:
        tkinter.messagebox.showinfo("ERRO!", 'Por favor forneça todos os campos de entrada')




status = ['Não iniado', 'Em andamento', 'Concluido']
nivel_importancia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def addTarefa():
    janela_dados = Tk()
    janela_dados.geometry('500x500')
    janela_dados.title("Cadastro de tarefas")
    janela_dados.resizable(height=FALSE, width=FALSE)
    janela_dados.config(background=PadraoProjeto.COR_BRANCA)

    frame_top = Frame(janela_dados, width=500, height=80, bg=PadraoProjeto.COR_LARANJA_CLARO, relief=SOLID)
    frame_top.pack()

    frame_meio = Frame(janela_dados, width=500, height=420, bg=PadraoProjeto.COR_BRANCA, relief=SOLID)
    frame_meio.pack()

    titulo = Label(frame_top, text="Cadastro de tarefas", font=PadraoProjeto.fonte_titulo,
                   bg=PadraoProjeto.COR_LARANJA_CLARO, fg=PadraoProjeto.COR_BRANCA)
    titulo.place(x=90, y=20)

    titulo_tarefa = Label(frame_meio, text='Tarefa:', anchor=NW, font=PadraoProjeto.fonte_conteudo,
                          bg=PadraoProjeto.COR_BRANCA)
    titulo_tarefa.place(x=50, y=50)
    Entrada_tarefa = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=PadraoProjeto.fonte_conteudo)
    Entrada_tarefa.place(x=165, y=50)

    titulo_descricao = Label(frame_meio, text='Descrição:', anchor=NW, font=PadraoProjeto.fonte_conteudo,
                             bg=PadraoProjeto.COR_BRANCA)
    titulo_descricao.place(x=50, y=100)
    Entrada_descricao = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=PadraoProjeto.fonte_conteudo)
    Entrada_descricao.place(x=165, y=100)

    titulo_status = Label(frame_meio, text='Status:', anchor=NW, font=PadraoProjeto.fonte_conteudo,
                          bg=PadraoProjeto.COR_BRANCA)
    titulo_status.place(x=50, y=150)
    Entrada_status = ttk.Combobox(frame_meio, width=20, font=PadraoProjeto.fonte_conteudo, justify=CENTER)
    Entrada_status['values'] = status
    Entrada_status.place(x=165, y=150)

    titulo_nivel = Label(frame_meio, text='Nivel de importancia:', anchor=NW, font=PadraoProjeto.fonte_conteudo,
                         bg=PadraoProjeto.COR_BRANCA)
    titulo_nivel.place(x=50, y=200)
    Entrada_nivel = ttk.Combobox(frame_meio, width=5, font=PadraoProjeto.fonte_conteudo, justify=CENTER)
    Entrada_nivel['values'] = nivel_importancia
    Entrada_nivel.place(x=270, y=200)

    linha_horizontal = Label(frame_meio, relief=GROOVE, width=400, height=0, anchor=NW, font='Ivy 1',
                             bg=PadraoProjeto.COR_LARANJA_ESCURO, fg=PadraoProjeto.COR_CINZA_ESCURO)
    linha_horizontal.place(x=50, y=250)

    botao_salvar = Button(frame_meio, command=lambda: salvar_tarefa(Entrada_tarefa, Entrada_descricao, Entrada_status, Entrada_nivel, janela_dados), relief=GROOVE, text="Salvar", width=10,
                          compound=LEFT,
                          overrelief=RIDGE, font=PadraoProjeto.fonte_conteudo,
                          bg=PadraoProjeto.COR_LARANJA_CLARO, fg=PadraoProjeto.COR_BRANCA)
    botao_salvar.place(x=175, y=300)


"""def deletarTarefaEspecifica(id):
    tarefa = id.get()
    """



