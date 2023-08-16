from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from core import funcoes_todolist
from utils import colors, fonts
from dao import bdToDoList
from core import Funcoes_main
from utils.ToolTip import Tooltip
def atualizar_janela(janela):
    # Destrua a janela atual
    janela.destroy()
    criar_janela_todo_list()


def criar_janela_todo_list():
    janela = Tk()
    janela.title("To-Do List")
    janela.geometry('1280x700')
    janela.config(background=colors.COR_BRANCA)
    janela.resizable(width=FALSE, height=FALSE)

    frame_top = Frame(janela, width=1280, height=125, bg=colors.COR_BRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top, width=1280, height=174, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
    frame_detalhes.pack(padx=0, pady=0)

    Texto_Productivity = "Productivity"
    label = Label(frame_top, text=Texto_Productivity, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO, font=('monospace', 40))
    label.place(x=34, y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT, command=lambda: Funcoes_main.renderizar_home(janela)
                   )
    label.place(x=625, y=50)

    Botao_Codigo = "DashBoard"
    label = Button(frame_top, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO, font=('monospace', 32),
                   relief=FLAT)
    label.place(x=800, y=50)

    Botao_Team = "Sobre"
    label = Button(frame_top, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
    label.place(x=1068, y=50)

    frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
    frame_detalhes_borda.pack(padx=0, pady=0)

    frame_meio = Frame(janela, width=1280, height=550, bg=colors.COR_BRANCA, relief=SOLID)
    frame_meio.pack()

    tv = ttk.Treeview(frame_meio, columns=('id', 'tarefa', 'status', 'descricao', 'nivel'), height=20)
    tv.column('id', minwidth=30, width=30, anchor='w', stretch=NO)
    tv.column('tarefa', minwidth=50, width=100, anchor='w')
    tv.column('status', minwidth=50, width=100, anchor='center')
    tv.column('descricao', minwidth=80, width=100, anchor='w')
    tv.column('nivel', minwidth=30, width=50, anchor='center')
    tv.heading('id', text='ID', anchor='w')
    tv.heading('tarefa', text='TAREFA')
    tv.heading('status', text='STATUS')
    tv.heading('descricao', text='DESCRICAO')
    tv.heading('nivel', text='NIVEL')
    tv.place(x=670, y=20)

    try:
        bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus")
        for row in bdToDoList.ToDoList_banco.cursor.fetchall():
            tv.insert("", "end", values=row)
    except Exception as e:
        tv.insert("", "end", values=("Erro ao acessar o banco de dados:", str(e)))

    linha_vertical = Label(frame_meio, relief=GROOVE, width=0, height=255, anchor=NW, font='Ivy 1',
                           bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
    linha_vertical.place(x=640, y=15)

    linha_horizontal = Label(frame_meio, relief=GROOVE, width=350, height=0, anchor=NW, font='Ivy 1',
                             bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
    linha_horizontal.place(x=152, y=190)

    linha_horizontal = Label(frame_meio, relief=GROOVE, width=1280, height=0, anchor=NW, font='Ivy 1',
                             bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
    linha_horizontal.place(x=0, y=523)

    img_logo = Image.open('assets/toDoList_logo.png')
    img_logo = ImageTk.PhotoImage(img_logo)
    imagem_logo = Label(frame_meio, image=img_logo, compound=LEFT, anchor=NW)
    imagem_logo.place(x=165, y=10)

    texto_todolist = Label(frame_meio, text="To-Do List", font=fonts.fonte_titulo)
    texto_todolist.place(x=255, y=25)

    texto_entrada_idTask = Label(frame_meio, text='ID da tarefa:', anchor=NW, font=fonts.fonte_conteudo,
                                 bg=colors.COR_BRANCA)
    texto_entrada_idTask.place(x=200, y=225)
    Entrada_idTask = Entry(frame_meio, width=7, justify='center', relief=SOLID, font=fonts.fonte_conteudo)
    Entrada_idTask.place(x=340, y=225)

    img_add = Image.open('assets/toDoList_add.png')
    img_add = img_add.resize((35, 35))
    img_add = ImageTk.PhotoImage(img_add)
    botao_add = Button(frame_meio, image=img_add, command=funcoes_todolist.addTarefa, relief=GROOVE,
                       text="Adicionar Tarefa", width=300,
                       compound=LEFT, overrelief=RIDGE, font=fonts.fonte_conteudo,
                       bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
    botao_add.place(x=175, y=120)

    img_update = Image.open('assets/toDoList_update.png')
    img_update = img_update.resize((35, 35))
    img_update = ImageTk.PhotoImage(img_update)
    botao_add = Button(frame_meio, image=img_update, command=lambda: funcoes_todolist.atualizarTarefa(Entrada_idTask), relief=GROOVE, text="Atualizar Tarefa", width=300,
                       compound=LEFT, overrelief=RIDGE, font=fonts.fonte_conteudo,
                       bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
    botao_add.place(x=175, y=290)




    botao_atualizar_table = Button(frame_meio, image=img_update, command=lambda: atualizar_janela(janela),
                                   relief=GROOVE, width=40, compound=LEFT, overrelief=RIDGE,
                                   font=fonts.fonte_conteudo, bg=colors.COR_LARANJA_CLARO,
                                   fg=colors.COR_BRANCA)
    botao_atualizar_table.place(x=1205, y=450)
    tooltip = Tooltip(botao_atualizar_table, "Atualizar tabela")






    img_delete = Image.open('assets/toDoList_delete.png')
    img_delete = img_delete.resize((35, 35))
    img_delete = ImageTk.PhotoImage(img_delete)
    botao_delete = Button(frame_meio, command=lambda: funcoes_todolist.deletarTarefaEspecifica(Entrada_idTask), image=img_delete, relief=GROOVE, text="Deletar Tarefa", width=300,
                          compound=LEFT,
                          overrelief=RIDGE, font=fonts.fonte_conteudo,
                          bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
    botao_delete.place(x=175, y=370)

    img_all_delete = Image.open('assets/toDoList_danger.png')
    img_all_delete = img_all_delete.resize((35, 35))
    img_all_delete = ImageTk.PhotoImage(img_all_delete)
    botao_all_delete = Button(frame_meio, command=funcoes_todolist.deletarTodasTasks, image=img_all_delete, relief=GROOVE,
                              text="Deletar todas as tarefas",
                              width=300, compound=LEFT, overrelief=RIDGE, font=fonts.fonte_conteudo,
                              bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
    botao_all_delete.place(x=175, y=450)

    janela.mainloop()

if __name__ == '__main__':
    criar_janela_todo_list()

