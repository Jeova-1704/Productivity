import sqlite3


class BdToDoList:
    def __init__(self):
        self.conn = sqlite3.connect('../dao/BdToDoList.db')
        self.cursor = self.conn.cursor()
        self.criarTabela()

    def criarTabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS BdToDoList(
                            idTask INTEGER PRIMARY KEY AUTOINCREMENT,
                            tarefa TEXT NOT NULL,
                            status TEXT NOT NULL,
                            descricao TEXT NOT NULL,
                            nivel_Importancia INTEGER NOT NULL)''')

    def registroDeTarefas(self, ListaTarefas):
        self.cursor.execute(
            'INSERT INTO BdToDoList(tarefa, status, descricao, nivel_Importancia) VALUES (?, ?, ?, ?)',
            ListaTarefas)
        self.conn.commit()

    def visualizacaoTodasTarefas(self):
        self.cursor.execute('SELECT * FROM BdToDoList')
        informacao = self.cursor.fetchall()
        return informacao

    def procurarTarefa(self, idTask):
        self.cursor.execute('SELECT * FROM BdToDoList WHERE idTask=?', (idTask,))
        informacao = self.cursor.fetchone()
        if informacao == None:
            return False
        else:
            return informacao

    def atualizar_tarefa(self, listaAtualizada):
        query = 'UPDATE BdToDoList SET tarefa = ?, status = ?, descricao = ?, nivel_Importancia = ? WHERE idTask = ?'
        self.cursor.execute(query, listaAtualizada)
        self.conn.commit()

    def deletarTarefa(self, idTask):
        self.cursor.execute('DELETE FROM BdToDoList WHERE idTask=?', (idTask,))
        self.conn.commit()

    def deletarTodasAsTarefas(self):
        self.cursor.execute('DELETE FROM BdToDoList')
        self.conn.commit()

ToDoList_banco = BdToDoList()
