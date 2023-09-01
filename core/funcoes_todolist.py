import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from utils import fonts, colors
from dao import bdToDoList
from view import ToDoList

status_task = ['Não iniciado', 'Em andamento', 'Concluido']
nivel_importancia_task = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def salvar_tarefa(Entrada_tarefa, Entrada_descricao, Entrada_status, Entrada_nivel, janela, janela_todo):
    try:
        tarefa = str(Entrada_tarefa.get())
        descricao = str(Entrada_descricao.get())
        status_task = str(Entrada_status.get())
        nivel = int(Entrada_nivel.get())
        lista_para_banco_dados = [tarefa, status_task, descricao, nivel]
        bdToDoList.ToDoList_banco.registroDeTarefas(lista_para_banco_dados)
        messagebox.showinfo("SUCESSO", 'Tarefa adicionada com sucesso!')
        janela.destroy()
    except:
        tkinter.messagebox.showinfo("ERRO!", 'Por favor forneça todos os campos de entrada')
    atualizar_janela(janela_todo)


def atualizar_tarefa(Entrada_tarefa, Entrada_descricao, Entrada_status, Entrada_nivel, id_task, janela, janela_todo):
    try:
        tarefa = str(Entrada_tarefa.get())
        descricao = str(Entrada_descricao.get())
        status_task = str(Entrada_status.get())
        nivel = int(Entrada_nivel.get())
        id = id_task
        lista_para_banco_dados = [tarefa, status_task, descricao, nivel, id]
        bdToDoList.ToDoList_banco.atualizar_tarefa(lista_para_banco_dados)
        messagebox.showinfo('SUCESSO!', f"A tarefa '{tarefa}' foi atualizada com sucesso.")
        janela.destroy()
    except:
        tkinter.messagebox.showinfo("ERRO!", 'Por favor forneça todos os campos de entrada')
    atualizar_janela(janela_todo)


def addTarefa(janela_todo):
    janela_dados = Toplevel()
    janela_dados.geometry('500x500')
    janela_dados.iconbitmap('../view/assets/todoList.ico')
    janela_dados.title("Cadastro de tarefas")
    janela_dados.resizable(height=FALSE, width=FALSE)
    janela_dados.config(background=colors.COR_BRANCA)

    frame_top = Frame(janela_dados, width=500, height=80, bg=colors.COR_LARANJA_CLARO, relief=SOLID)
    frame_top.pack()

    frame_meio = Frame(janela_dados, width=500, height=420, bg=colors.COR_BRANCA, relief=SOLID)
    frame_meio.pack()

    titulo = Label(frame_top, text="Cadastro de tarefas", font=fonts.fonte_titulo,
                   bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
    titulo.place(x=90, y=20)

    titulo_tarefa = Label(frame_meio, text='Tarefa:', anchor=NW, font=fonts.fonte_conteudo,
                          bg=colors.COR_BRANCA)
    titulo_tarefa.place(x=50, y=50)
    Entrada_tarefa = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=fonts.fonte_conteudo)
    Entrada_tarefa.place(x=165, y=50)

    titulo_descricao = Label(frame_meio, text='Descrição:', anchor=NW, font=fonts.fonte_conteudo,
                             bg=colors.COR_BRANCA)
    titulo_descricao.place(x=50, y=100)
    Entrada_descricao = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=fonts.fonte_conteudo)
    Entrada_descricao.place(x=165, y=100)

    titulo_status = Label(frame_meio, text='Status:', anchor=NW, font=fonts.fonte_conteudo,
                          bg=colors.COR_BRANCA)
    titulo_status.place(x=50, y=150)
    Entrada_status = ttk.Combobox(frame_meio, width=20, font=fonts.fonte_conteudo, justify=CENTER)
    Entrada_status['values'] = status_task
    Entrada_status.place(x=165, y=150)

    titulo_nivel = Label(frame_meio, text='Nível de importância:', anchor=NW, font=fonts.fonte_conteudo,
                         bg=colors.COR_BRANCA)
    titulo_nivel.place(x=50, y=200)
    Entrada_nivel = ttk.Combobox(frame_meio, width=5, font=fonts.fonte_conteudo, justify=CENTER)
    Entrada_nivel['values'] = nivel_importancia_task
    Entrada_nivel.place(x=270, y=200)

    linha_horizontal = Label(frame_meio, relief=GROOVE, width=400, height=0, anchor=NW, font='Ivy 1',
                             bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
    linha_horizontal.place(x=50, y=250)

    botao_salvar = Button(frame_meio, command=lambda: salvar_tarefa(Entrada_tarefa, Entrada_descricao, Entrada_status,
                                                                    Entrada_nivel, janela_dados, janela_todo),
                          relief=GROOVE,
                          text="Salvar", width=10,
                          compound=LEFT,
                          overrelief=RIDGE, font=fonts.fonte_conteudo,
                          bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
    botao_salvar.place(x=175, y=300)


def deletar_pesquisar_arvore(tv):
    itens_selecionados = tv.selection()
    if not itens_selecionados:
        messagebox.showerror("Atenção", 'Selecionar ao menos uma tarefa para poder deletar!')
        return

    confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar as tarefas selecionadas?")

    if confirmacao:
        for item_selecionado in itens_selecionados:
            id_tarefa = tv.item(item_selecionado, 'values')[0]
            tv.delete(item_selecionado)
            deletarTarefaEspecifica(id_tarefa)
        messagebox.showinfo("Sucesso!", "Todas as tarefas selecionadas foram deletadas com sucesso!")


def deletarTarefaEspecifica(id_tarefa):
    try:
        id_tarefa = int(id_tarefa)
        bdToDoList.ToDoList_banco.deletarTarefa(id_tarefa)
    except:
        messagebox.showerror("Erro!",
                             'Erro ao deletar a tarefa, por favor tente novamente, se o problema persistir atualizar '
                             'a tabela.')


def deletarTodasTasks(janela_todo):
    try:
        bdToDoList.ToDoList_banco.deletarTodasAsTarefas()
        messagebox.showinfo('SUCESSO!', 'Todas as tarefas foram excluídas com sucesso.')
    except:
        messagebox.showerror('ERRO!', 'Erro ao excluir todas as tarefas, por favor tente novamente e se o problema '
                                      'persistir tente atualizar a tabela e tente novamente.')
    atualizar_janela(janela_todo)


def atualizar_pesquisar_arvore(janela, tv):
    itens_selecionados = tv.selection()
    if len(itens_selecionados) == 1:
        try:
            item_selecionado = tv.selection()[0]
            id_tarefa = tv.item(item_selecionado, 'values')[0]
            atualizarTarefa(id_tarefa, janela)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um elemento para poder atualizar")
    else:
        messagebox.showerror("Erro!", "Por favor selecione apenas um item para poder atualizar.")


def atualizarTarefa(id_tarefa, janela_todo):
    try:
        todo_lista = bdToDoList.ToDoList_banco.procurarTarefa(id_tarefa)
        if len(todo_lista) != 0 or todo_lista == False:
            janela_dados = Tk()
            janela_dados.iconbitmap('../view/assets/todoList.ico')
            janela_dados.geometry('500x500')
            janela_dados.title("Atuaização de tarefas")
            janela_dados.resizable(height=FALSE, width=FALSE)
            janela_dados.config(background=colors.COR_BRANCA)

            frame_top = Frame(janela_dados, width=500, height=80, bg=colors.COR_LARANJA_CLARO, relief=SOLID)
            frame_top.pack()

            frame_meio = Frame(janela_dados, width=500, height=420, bg=colors.COR_BRANCA, relief=SOLID)
            frame_meio.pack()

            titulo = Label(frame_top, text="Cadastro de tarefas", font=fonts.fonte_titulo,
                           bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
            titulo.place(x=90, y=20)

            titulo_tarefa = Label(frame_meio, text='Tarefa:', anchor=NW, font=fonts.fonte_conteudo,
                                  bg=colors.COR_BRANCA)
            titulo_tarefa.place(x=50, y=50)
            Entrada_tarefa = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=fonts.fonte_conteudo)
            Entrada_tarefa.place(x=165, y=50)
            Entrada_tarefa.insert(0, todo_lista[1])

            titulo_descricao = Label(frame_meio, text='Descrição:', anchor=NW, font=fonts.fonte_conteudo,
                                     bg=colors.COR_BRANCA)
            titulo_descricao.place(x=50, y=100)
            Entrada_descricao = Entry(frame_meio, width=22, justify=LEFT, relief=SOLID, font=fonts.fonte_conteudo)
            Entrada_descricao.place(x=165, y=100)
            Entrada_descricao.insert(0, todo_lista[3])

            titulo_status = Label(frame_meio, text='Status:', anchor=NW, font=fonts.fonte_conteudo,
                                  bg=colors.COR_BRANCA)
            titulo_status.place(x=50, y=150)
            Entrada_status = ttk.Combobox(frame_meio, width=20, font=fonts.fonte_conteudo, justify=CENTER)
            Entrada_status['values'] = status_task
            Entrada_status.place(x=165, y=150)
            Entrada_status.insert(0, todo_lista[2])

            titulo_nivel = Label(frame_meio, text='Nivel de importancia:', anchor=NW, font=fonts.fonte_conteudo,
                                 bg=colors.COR_BRANCA)
            titulo_nivel.place(x=50, y=200)
            Entrada_nivel = ttk.Combobox(frame_meio, width=5, font=fonts.fonte_conteudo, justify=CENTER)
            Entrada_nivel['values'] = nivel_importancia_task
            Entrada_nivel.place(x=270, y=200)
            Entrada_nivel.insert(0, todo_lista[4])

            linha_horizontal = Label(frame_meio, relief=GROOVE, width=400, height=0, anchor=NW, font='Ivy 1',
                                     bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
            linha_horizontal.place(x=50, y=250)

            botao_salvar = Button(frame_meio,
                                  command=lambda: atualizar_tarefa(Entrada_tarefa, Entrada_descricao, Entrada_status,
                                                                   Entrada_nivel, id_tarefa, janela_dados, janela_todo),
                                  relief=GROOVE,
                                  text="Atualizar", width=10,
                                  compound=LEFT,
                                  overrelief=RIDGE, font=fonts.fonte_conteudo,
                                  bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
            botao_salvar.place(x=175, y=300)
    except:
        messagebox.showerror("ERRO!", f"Por favor forneça um ID valido para atualizar a atarefa")


def atualizar_janela(janela):
    janela.destroy()
    ToDoList.InterfaceToDoList()


def aplicar_filtro(tv, filtro_box):
    status_para_filtro = filtro_box.get()

    # Deleta todos os itens filhos da Treeview
    for item in tv.get_children():
        tv.delete(item)

    try:
        if status_para_filtro == "Todos":
            bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus")
        elif status_para_filtro == "Concluido":
            bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus WHERE status=?", ("Concluido",))
        elif status_para_filtro == "Em andamento":
            bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus WHERE status=?", ("Em andamento",))
        elif status_para_filtro == "Não iniciado":
            bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus WHERE status=?", ("Não iniciado",))
        else:
            bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus WHERE status=?",
                                                     (status_para_filtro,))

        for row in bdToDoList.ToDoList_banco.cursor.fetchall():
            tv.insert("", "end", values=row)

    except Exception as e:
        tv.insert("", "end", values=("Erro ao acessar o banco de dados:", str(e)))
