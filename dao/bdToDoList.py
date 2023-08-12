# Importação das bibliotecas: ==========================================================================================================================================

import sqlite3
from tkinter import messagebox


# Criando classe do banco de dados:======================================================================================================================================

class ToDOStatus:
    # Incializando a classe do banco de dados com, criando um conector e crinando a tabela
    def __init__(self):
        self.conn = sqlite3.connect('todolistStatus.db')
        self.cursor = self.conn.cursor()
        self.criarTabela()

    # Criando a tabela e se já existir ela usa a já criada com o mesmo nome, junto com as colunas (idTask, tarefas, status, descricao, nivel_Importancia)
    def criarTabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS todolistStatus(
                            idTask INTEGER PRIMARY KEY AUTOINCREMENT,
                            tarefa TEXT NOT NULL,
                            status TEXT NOT NULL,
                            descricao TEXT NOT NULL,
                            nivel_Importancia INTEGER NOT NULL)''')

    # registrar os valores no banco de dados com uma lista passada como paramntro contando os valores (tarefa, status, descricao, nivel_Inportancia)
    def registroDeTarefas(self, ListaTarefas):
        self.cursor.execute(
            'INSERT INTO todolistStatus(tarefa, status, descricao, nivel_Importancia) VALUES (?, ?, ?, ?)',
            ListaTarefas)

        self.conn.commit()
        # Mostando a mensagem na tela de sucesso:
        messagebox.showinfo("SUCESSO", 'Tarefa adicionada com sucesso!')

    # Visualiza os valores do banco de dados 
    def visualizacaoTodasTarefas(self):
        self.cursor.execute('SELECT * FROM todolistStatus')
        informacao = self.cursor.fetchall()
        return informacao

    # Procura uma tarefa com um id pré definido e passado como paramento
    def procurarTarefa(self, idTask):
        self.cursor.execute('SELECT * FROM todolistStatus WHERE idTask=?', (idTask,))
        informacao = self.cursor.fetchone()
        if informacao == None:
            return messagebox.showinfo("ERRO!", f'Não foi possível encontrar a tarefa com o IdTask {idTask}')
        else:
            return informacao

    # Atualiza os valores do banco de dados com os novos valores passados como parametro na chamada do metodo
    def atualizar_tarefa(self, listaAtualizada):
        query = 'UPDATE todolistStatus SET tarefa = ?, status = ?, descricao = ?, nivel_Importancia = ? WHERE idTask = ?'
        self.cursor.execute(query, listaAtualizada)
        self.conn.commit()
        # Mostrando mensagem de sucesso
        messagebox.showinfo('SUCESSO!', f"Tarefa com idTask {listaAtualizada[4]} foi atualizada com sucesso.")

    # Deleta uma tarefa do banco de dados que é passada como paramento na chamada do metodo
    def deletarTarefa(self, idTask):
        self.cursor.execute('DELETE FROM todolistStatus WHERE idTask=?', (idTask,))
        self.conn.commit()
        # Mostrando mensagem de sucesso
        messagebox.showinfo('SUCESSO!', f"Tarefa com o idTask {idTask} foi deletado com sucesso.")


banco = ToDOStatus()
