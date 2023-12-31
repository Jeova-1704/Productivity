import sqlite3
import os


class BancoDeEventos:
    def __init__(self):
        db_path = os.path.join(os.path.dirname(__file__), '..', 'dao', 'eventos.db')
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.cria_tabela()

    def cria_tabela(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS eventos(
                   id INTEGER PRIMARY KEY,
                   dias TEXT NOT NULL,
                   evento TEXT NOT NULL,
                   horario TEXT NOT NULL)
                   ''')

    def insere_na_tabela(self, eventos):
        self.c.execute("INSERT INTO eventos(dias, evento, horario) VALUES(?, ?, ?)", eventos)
        self.conn.commit()

    def ver_todos_eventos(self):
        self.c.execute("SELECT id, dias, evento, horario FROM eventos")
        dados = self.c.fetchall()
        return dados

    def delete_evento(self, id):
        self.c.execute("DELETE FROM eventos WHERE id=?", (id,))
        self.conn.commit()


sistema_de_registro = BancoDeEventos()
