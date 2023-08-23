from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from core import funcoes_todolist
from utils import colors, fonts
from dao import bdToDoList
from core import funcoes_main
from utils.ToolTip import Tooltip


class InterfaceToDoList:
    Botao_Codigo: str
    status = ['Todos', 'Concluido', 'Em andamento', 'Não iniado']

    def __init__(self):

        self.janela = Tk()
        self.janela.iconbitmap('assets/todoList.ico')
        self.janela.title("To-Do List")
        self.janela.geometry('1280x700')
        self.janela.config(background=colors.COR_BRANCA)
        self.janela.resizable(width=FALSE, height=FALSE)

        self.frame_top = Frame(self.janela, width=1280, height=125, bg=colors.COR_BRANCA, relief=SOLID)
        self.frame_top.pack(padx=0, pady=0)

        self.frame_detalhes = Frame(self.frame_top, width=1280, height=174, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
        self.frame_detalhes.pack(padx=0, pady=0)

        self.Texto_Productivity = "Productivity"
        self.label = Label(self.frame_top, text=self.Texto_Productivity, fg=colors.COR_BRANCA,
                           bg=colors.COR_CINZA_ESCURO,
                           font=fonts.fonte_conteudo_logo)
        self.label.place(x=34, y=50)

        self.Botao_Home = "Home"
        self.label = Button(self.frame_top, text=self.Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela)
                            )
        self.label.place(x=625, y=50)

        self.Botao_Codigo = "DashBoard"
        self.label = Button(self.frame_top, text=self.Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            relief=FLAT)
        self.label.place(x=800, y=50)

        self.Botao_Team = "Sobre"
        self.label = Button(self.frame_top, text=self.Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            command=lambda: funcoes_main.renderizar_team(self.janela), relief=FLAT)
        self.label.place(x=1068, y=50)

        self.frame_detalhes_borda = Frame(self.frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
        self.frame_detalhes_borda.pack(padx=0, pady=0)

        self.frame_meio = Frame(self.janela, width=1280, height=550, bg=colors.COR_BRANCA, relief=SOLID)
        self.frame_meio.pack()

        self.tv = ttk.Treeview(self.frame_meio, columns=('id', 'tarefa', 'status', 'descricao', 'nivel'), height=20)
        self.tv.column('id', minwidth=30, width=30, anchor='w', stretch=NO)
        self.tv.column('tarefa', minwidth=50, width=100, anchor='w')
        self.tv.column('status', minwidth=50, width=100, anchor='center')
        self.tv.column('descricao', minwidth=80, width=100, anchor='w')
        self.tv.column('nivel', minwidth=30, width=50, anchor='center')
        self.tv.heading('id', text='ID', anchor='w')
        self.tv.heading('tarefa', text='TAREFA')
        self.tv.heading('status', text='STATUS')
        self.tv.heading('descricao', text='DESCRICAO')
        self.tv.heading('nivel', text='NIVEL')
        self.tv.place(x=670, y=20)

        try:
            bdToDoList.ToDoList_banco.cursor.execute("SELECT * FROM todolistStatus")
            for row in bdToDoList.ToDoList_banco.cursor.fetchall():
                self.tv.insert("", "end", values=row)
        except Exception as e:
            self.tv.insert("", "end", values=("Erro ao acessar o banco de dados:", str(e)))

        linha_vertical = Label(self.frame_meio, relief=GROOVE, width=0, height=255, anchor=NW, font='Ivy 1',
                               bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
        linha_vertical.place(x=640, y=15)

        linha_horizontal = Label(self.frame_meio, relief=GROOVE, width=1280, height=0, anchor=NW, font='Ivy 1',
                                 bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_CINZA_ESCURO)
        linha_horizontal.place(x=0, y=523)

        self.img_logo = Image.open('assets/toDoList_logo.png')
        self.img_logo = ImageTk.PhotoImage(self.img_logo)
        self.imagem_logo = Label(self.frame_meio, image=self.img_logo, compound=LEFT, anchor=NW)
        self.imagem_logo.place(x=165, y=10)

        self.texto_todolist = Label(self.frame_meio, text="To-Do List", font=fonts.fonte_titulo)
        self.texto_todolist.place(x=255, y=25)

        self.img_add = Image.open('assets/toDoList_add.png')
        self.img_add = self.img_add.resize((35, 35))
        self.img_add = ImageTk.PhotoImage(self.img_add)
        self.botao_add = Button(self.frame_meio, image=self.img_add,
                                command=lambda: funcoes_todolist.addTarefa(self.janela),
                                relief=GROOVE,
                                text="Adicionar Tarefa", width=300,
                                compound=LEFT, overrelief=RIDGE, font=fonts.fonte_conteudo,
                                bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
        self.botao_add.place(x=175, y=120)

        self.img_update = Image.open('assets/toDoList_update.png')
        self.img_update = self.img_update.resize((35, 35))
        self.img_update = ImageTk.PhotoImage(self.img_update)
        self.botao_update = Button(self.frame_meio, image=self.img_update,
                                   command=lambda: funcoes_todolist.atualizar_pesquisar_arvore(self.janela, self.tv),
                                   relief=GROOVE, text="Atualizar Tarefa", width=300,
                                   compound=LEFT, overrelief=RIDGE, font=fonts.fonte_conteudo,
                                   bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
        self.botao_update.place(x=175, y=200)

        self.botao_atualizar_table = Button(self.frame_meio, image=self.img_update,
                                            command=lambda: funcoes_todolist.atualizar_janela(self.janela),
                                            relief=GROOVE, width=40, compound=LEFT, overrelief=RIDGE,
                                            font=fonts.fonte_conteudo, bg=colors.COR_LARANJA_CLARO,
                                            fg=colors.COR_BRANCA)
        self.botao_atualizar_table.place(x=1205, y=450)
        self.tooltip = Tooltip(self.botao_atualizar_table, "Atualizar tabela")

        self.img_delete = Image.open('assets/toDoList_delete.png')
        self.img_delete = self.img_delete.resize((35, 35))
        self.img_delete = ImageTk.PhotoImage(self.img_delete)
        self.botao_delete = Button(self.frame_meio,
                                   command=lambda: funcoes_todolist.deletar_pesquisar_arvore(self.tv),
                                   image=self.img_delete, relief=GROOVE, text="Deletar Tarefa", width=300,
                                   compound=LEFT,
                                   overrelief=RIDGE, font=fonts.fonte_conteudo,
                                   bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
        self.botao_delete.place(x=175, y=280)

        self.img_all_delete = Image.open('assets/toDoList_danger.png')
        self.img_all_delete = self.img_all_delete.resize((35, 35))
        self.img_all_delete = ImageTk.PhotoImage(self.img_all_delete)
        self.botao_all_delete = Button(self.frame_meio, command=lambda: funcoes_todolist.deletarTodasTasks(self.janela),
                                       image=self.img_all_delete,
                                       relief=GROOVE,
                                       text="Deletar todas as tarefas",
                                       width=300, compound=LEFT, overrelief=RIDGE, font=fonts.fonte_conteudo,
                                       bg=colors.COR_LARANJA_CLARO, fg=colors.COR_BRANCA)
        self.botao_all_delete.place(x=175, y=360)

        self.status_filter_combobox = ttk.Combobox(self.frame_meio, width=12, justify=CENTER, font=fonts.fonte_conteudo)
        self.status_filter_combobox['values'] = self.status
        self.status_filter_combobox.place(x=320, y=425)

        self.img_filter = Image.open('assets/toDoList_filtro.png')
        self.img_filter = self.img_filter.resize((35, 35))
        self.img_filter = ImageTk.PhotoImage(self.img_filter)
        self.filtrar_tabela = Button(self.frame_meio, command=lambda: funcoes_todolist.aplicar_filtro(self.tv, self.status_filter_combobox),
                                     image=self.img_filter,
                                     relief=GROOVE, anchor='w',
                                     text="Filtrar por:", compound="left",
                                     font=fonts.fonte_conteudo,
                                     bg=colors.COR_LARANJA_CLARO,
                                     fg=colors.COR_BRANCA)
        self.filtrar_tabela.place(x=174, y=425)

        self.janela.mainloop()


if __name__ == '__main__':
    interfaceToDoList = InterfaceToDoList()
