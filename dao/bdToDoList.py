import sqlite3
from tkinter import messagebox
import os

class ToDOStatus:
    def __init__(self):
        self.conn = sqlite3.connect('../dao/todolistStatus.db')
        self.cursor = self.conn.cursor()
        self.criarTabela()

    def criarTabela(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS todolistStatus(
                            idTask INTEGER PRIMARY KEY AUTOINCREMENT,
                            tarefa TEXT NOT NULL,
                            status TEXT NOT NULL,
                            descricao TEXT NOT NULL,
                            nivel_Importancia INTEGER NOT NULL)''')

    def registroDeTarefas(self, ListaTarefas):
        self.cursor.execute(
            'INSERT INTO todolistStatus(tarefa, status, descricao, nivel_Importancia) VALUES (?, ?, ?, ?)',
            ListaTarefas)

        self.conn.commit()
        messagebox.showinfo("SUCESSO", 'Tarefa adicionada com sucesso!')

    def visualizacaoTodasTarefas(self):
        self.cursor.execute('SELECT * FROM todolistStatus')
        informacao = self.cursor.fetchall()
        return informacao

    def procurarTarefa(self, idTask):
        self.cursor.execute('SELECT * FROM todolistStatus WHERE idTask=?', (idTask,))
        informacao = self.cursor.fetchone()
        if informacao == None:
            return messagebox.showinfo("ERRO!", f'Não foi possível encontrar a tarefa com o IdTask {idTask}')
        else:
            return informacao

    def atualizar_tarefa(self, listaAtualizada):
        query = 'UPDATE todolistStatus SET tarefa = ?, status = ?, descricao = ?, nivel_Importancia = ? WHERE idTask = ?'
        self.cursor.execute(query, listaAtualizada)
        self.conn.commit()
        messagebox.showinfo('SUCESSO!', f"Tarefa com idTask {listaAtualizada[4]} foi atualizada com sucesso.")

    def deletarTarefa(self, idTask):
        self.cursor.execute('DELETE FROM todolistStatus WHERE idTask=?', (idTask,))
        self.conn.commit()
        # Mostrando mensagem de sucesso
        messagebox.showinfo('SUCESSO!', f"Tarefa com o idTask {idTask} foi deletado com sucesso.")

    def deletarTodasAsTarefas(self):
        try:
            self.cursor.execute('DELETE FROM todolistStatus')
            self.conn.commit()
            messagebox.showinfo('SUCESSO!', 'Todas as tarefas foram excluídas do banco de dados.')
        except Exception as e:
            messagebox.showerror('ERRO!', 'Erro ao excluir todas as tarefas do banco de dados.')


ToDoList_banco = ToDOStatus()
