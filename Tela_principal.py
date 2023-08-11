# Código para ser seguido nos projetos 

# Importação das bibliotecas: ==========================================================================================================================================
from PIL import ImageTk, Image
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
    janela.geometry('1280x700')
    janela.config(background=CORBRANCA)
    janela.resizable(width=FALSE, height=FALSE)

    # Criar três frames

    frame_top = Frame(janela, width=1280, height=125, bg=CORBRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top,width=1280,height=174,bg=CORZINZAESCURO,relief=SOLID)
    frame_detalhes.pack(padx=0,pady=0)

    Texto_Productivity = "Productivity"
    label = tk.Label(frame_top, text=Texto_Productivity,fg=CORBRANCA,  bg=CORZINZAESCURO,font=('monospace', 40))
    label.place(x=34,y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home,fg=CORBRANCA,  bg=CORZINZAESCURO,font=('monospace', 32),relief=FLAT)
    label.place(x=625,y=50)

    Botao_Codigo = "Código"
    label = Button(frame_top, text=Botao_Codigo,fg=CORBRANCA,  bg=CORZINZAESCURO,font=('monospace', 32),relief=FLAT)
    label.place(x=846,y=50)

    Botao_Team = "Team"
    label = Button(frame_top, text=Botao_Team,fg=CORBRANCA,  bg=CORZINZAESCURO,font=('monospace', 32),relief=FLAT)
    label.place(x=1068,y=50)

    frame_detalhes_borda = Frame(frame_top,width=1280,height=4,bg=CORZINZACLARO,relief=SOLID)
    frame_detalhes_borda.pack(padx=0,pady=0)

 # iniciando frame do meio -----------------------------------------

    frame_meio = Frame(janela, width=1280, height=240, bg=CORBRANCA, relief=SOLID)
    frame_meio.pack(padx=0, pady=0,side='right')

    img_logo = PhotoImage(file='images/logo_productivity.png')
    label = Label(frame_meio,image=img_logo)
    label.pack(padx=90,pady=0,side='left')

    app_add = Image.open('images/Ellipse 1.png')
    app_add = app_add.resize((25, 25))
    app_add = ImageTk.PhotoImage(app_add)
    botao_add = Button(frame_meio, image=app_add, relief=GROOVE, text="Adicionar", width=100,
                       compound=LEFT,
                       overrelief=RIDGE, font='Ivy 7 bold',
                       bg=CORZINZAESCURO, fg=CORBRANCA)
    botao_add.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)

    frame_centro = Frame(frame_meio,width=900,height=240,bg=CORZINZAESCURO,relief=SOLID)
    frame_centro.pack(padx=0,pady=0,side='right')

    frame_centro_Borda = Frame(frame_meio,width=4,height=240,bg=CORZINZACLARO,relief=SOLID)
    frame_centro_Borda.pack(padx=0,pady=0)




    # Iniciar o loop de eventos da interface gráfica
    janela.mainloop()

# Chamar a função para criar a janela
criar_janela()
