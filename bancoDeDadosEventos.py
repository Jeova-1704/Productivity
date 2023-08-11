import sqlite3
from tkinter import messagebox


class BancoDeEventos:
    def __init__(self):
        self.conn = sqlite3.connect('eventos.db')
        self.c = self.conn.cursor()
        self.cria_tabela()

    def cria_tabela(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS eventos(
                   id INTEGER PRIMARY KEY,
                   dias TEXT NOT NULL,
                   evento TEXT NOT NULL)
                   ''')

    def insere_na_tabela(self, eventos):
        self.c.execute("INSERT INTO eventos(dias, evento) VALUES(?, ?)", eventos)
        self.conn.commit()
        messagebox.showinfo('Sucesso', 'Registro com sucesso')

    def ver_todos_eventos(self):
        self.c.execute("SELECT id, dias, evento FROM eventos")
        dados = self.c.fetchall()
        return dados
    def delete_evento(self, id):
        self.c.execute("DELETE FROM eventos WHERE id=?", (id,))
        self.conn.commit()
        messagebox.showinfo('Sucesso', f'Evento com ID {id} foi deletado')


# Criando instancia do sistema de registro
sistema_de_registro = BancoDeEventos()
