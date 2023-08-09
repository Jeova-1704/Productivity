# Código para ser seguido nos projetos 

# Importação das bibliotecas: ==========================================================================================================================================

from tkinter import *
import tkinter as tk
# variveis globais: =====================================================================================================================================================
CORBRANCA = "#F2F2F0"
CORZINZACLARO = "#A5A6A4"
CORZINZAESCURO = "#737373"
CORLARANJACLARO = "#BF8450"
CORLARANJAESCURO = "#BF4C0A"
# Continuação do codigo: ================================================================================================================================================

# Ciclo da janela para ela ir atualizando: ==============================================================================================================================
def criar_janela():
    # Criar uma instância da classe Tk
    janela = tk.Tk()
    janela.title("Janela Principal")
    janela.geometry('1366x768')
    janela.config(background=CORBRANCA)
    janela.resizable(width=FALSE, height=FALSE)

    # Criar três frames
    
    frame_top = Frame(janela, width=1366, height=100, bg=CORBRANCA, relief=SOLID)
    frame_top.grid(row=0, column=0, padx=0, pady=30)

    frame_logo = Frame(frame_top,width=140,height=140,bg=CORZINZACLARO,relief=SOLID)
    frame_logo.grid(row=0,column=0,padx=40,pady=0)

    frame_detalhes = Frame(frame_top,width=1180,height=150,bg=CORZINZAESCURO,relief=SOLID)
    frame_detalhes.grid(row=0,column=1,padx=0,pady=0)

    frame_botoes = Frame(janela, width=1000, height=300, bg=CORLARANJAESCURO, relief=RAISED)
    frame_botoes.grid(row=3, column=0, padx=0, pady=50,sticky="w")

    frame_tabela = Frame(janela, width=1366, height=80, bg=CORLARANJACLARO, relief=SOLID)
    frame_tabela.grid(row=5, column=0, padx=0, pady=60, sticky=NSEW, columnspan=5)

    # Iniciar o loop de eventos da interface gráfica
    janela.mainloop()

# Chamar a função para criar a janela
criar_janela()
