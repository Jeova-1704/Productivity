from tkinter import *
from tkinter.ttk import Treeview
from dao import bdToDoList, bdCalendario
from utils import colors, fonts
from core import funcoes_main


def center_window(janela, width, height):
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    janela.geometry(f"{width}x{height}+{x}+{y}")


class InterfaceDashboard:
    width = 1280
    height = 700

    def __init__(self):
        self.janela = Tk()
        self.janela.iconbitmap('assets/dashboard.ico')
        self.janela.title("DashBoard")
        center_window(self.janela, self.width, self.height)
        self.janela.config(background=colors.COR_BRANCA)
        self.janela.resizable(width=FALSE, height=FALSE)

        self.db = bdToDoList.ToDoList_banco
        self.create_task_tables()
        self.populate_tables()

        self.db = bdCalendario.BancoDeEventos()

        self.frame_top = Frame(self.janela, width=1280, height=125, bg=colors.COR_BRANCA, relief=SOLID)
        self.frame_top.pack(padx=0, pady=0)

        self.frame_detalhes = Frame(self.frame_top, width=1280, height=174, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
        self.frame_detalhes.pack(padx=0, pady=0)

        self.Texto_Productivity = "Productivity"
        self.label = Label(self.frame_detalhes, text=self.Texto_Productivity, fg=colors.COR_BRANCA,
                           bg=colors.COR_CINZA_ESCURO,
                           font=fonts.fonte_conteudo_logo)
        self.label.place(x=34, y=50)

        self.Botao_Home = "Home"
        self.label = Button(self.frame_detalhes, text=self.Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela)
                            )
        self.label.place(x=625, y=50)

        self.Botao_Codigo = "DashBoard"
        self.label = Button(self.frame_detalhes, text=self.Botao_Codigo, fg=colors.COR_BRANCA,
                            bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            relief=FLAT)
        self.label.place(x=800, y=50)

        self.Botao_Team = "Sobre"
        self.label = Button(self.frame_detalhes, text=self.Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                            font=fonts.fonte_conteudo_navBAr,
                            command=lambda: funcoes_main.renderizar_team(self.janela), relief=FLAT)
        self.label.place(x=1068, y=50)

        self.texto_anotacoes = Label(self.janela, text="Tarefas", font=fonts.fonte_conteudo, width=10,
                                     bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_BRANCA)
        self.texto_anotacoes.place(x=580, y=180)

        self.texto_anotacoes = Label(self.janela, text="Não iniciado", font=fonts.fonte_conteudo, width=10,
                                     bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_BRANCA)
        self.texto_anotacoes.place(x=400, y=230)

        self.texto_anotacoes = Label(self.janela, text="Andamento", font=fonts.fonte_conteudo, width=10,
                                     bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_BRANCA)
        self.texto_anotacoes.place(x=580, y=230)

        self.texto_anotacoes = Label(self.janela, text="Concluido", font=fonts.fonte_conteudo, width=10,
                                     bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_BRANCA)
        self.texto_anotacoes.place(x=770, y=230)

        self.calendario = Label(self.janela, text="Calendário", font=fonts.fonte_conteudo, width=10,
                                bg=colors.COR_LARANJA_ESCURO, fg=colors.COR_BRANCA)
        self.calendario.place(x=140, y=180)

        self.treeview_datas_eventos = Treeview(self.janela, columns=('Data',), show='headings')
        self.treeview_datas_eventos.heading('Data', text='Data')
        self.treeview_datas_eventos.column('Data', width=150, anchor='w')
        self.treeview_datas_eventos.place(x=100, y=265, width=150, height=400)

        self.treeview_eventos = Treeview(self.janela, columns=('Evento',), show='headings')
        self.treeview_eventos.heading('Evento', text='Evento', anchor='w')
        self.treeview_eventos.place(x=200, y=265, width=100, height=400)

        self.populate_datas_eventos()
        self.janela.mainloop()

    def create_task_tables(self):
        self.table_nao_iniciado = Treeview(self.janela, columns=('Tarefa',), show='headings')
        self.table_nao_iniciado.heading('Tarefa', text='Tarefa')
        self.table_nao_iniciado.place(x=375, y=265, width=180, height=400)

        self.table_andamento = Treeview(self.janela, columns=('Tarefa',), show='headings')
        self.table_andamento.heading('Tarefa', text='Tarefa')
        self.table_andamento.place(x=557, y=265, width=180, height=400)

        self.table_concluido = Treeview(self.janela, columns=('Tarefa',), show='headings')
        self.table_concluido.heading('Tarefa', text='Tarefa')
        self.table_concluido.place(x=738, y=265, width=180, height=400)

    def populate_tables(self):
        try:
            all_tasks = self.db.visualizacaoTodasTarefas()
            for task in all_tasks:
                self.add_task_to_table(task)
        except Exception as e:
            print("Erro ao acessar o banco de dados:", str(e))

    def add_task_to_table(self, task):
        status = task[2]
        if status == "Não iniciado":
            self.table_nao_iniciado.insert('', 'end', values=(task[1],))
        elif status == "Em andamento":
            self.table_andamento.insert('', 'end', values=(task[1],))
        elif status == "Concluido":
            self.table_concluido.insert('', 'end', values=(task[1],))

    def get_eventos_do_banco(self):
        try:
            eventos = self.db.ver_todos_eventos()
            return eventos
        except Exception as e:
            print("Erro ao acessar o banco de dados:", str(e))
            return []

    def populate_datas_eventos(self):
        try:
            eventos = self.get_eventos_do_banco()

            for evento in eventos:
                data = evento[1]
                descricao = evento[2]

                self.treeview_datas_eventos.insert('', 'end', values=(data,))
                self.treeview_eventos.insert('', 'end', values=(descricao,))

        except Exception as e:
            print("Erro ao acessar o banco de dados:", str(e))


if __name__ == '__main__':
    interfaceToDoList = InterfaceDashboard()
