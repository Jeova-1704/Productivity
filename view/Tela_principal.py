# Código para ser seguido nos projetos 

# Importação das bibliotecas: ==========================================================================================================================================

from core.FuncoesTelaPrincipal import *

# variveis globais: =====================================================================================================================================================
CORBRANCA = "#F2F2F0"
CORCINZACLARO = "#A5A6A4"
CORCINZAESCURO = "#737373"
CORLARANJACLARO = "#BF8450"
CORLARANJAESCURO = "#BF4C0A"

# Criar uma instância da classe Tk
janela = tk.Tk()
janela.title("Janela Principal")
janela.geometry('1280x700')
janela.config(background=CORBRANCA)
janela.resizable(width=FALSE, height=FALSE)


# Continuação do codigo: ================================================================================================================================================
def voltar_home():
    nova_janela = Tk()
    nova_janela.title("Nova Janela")
    janela.destroy()


# Frame da parte superior da janela ----------------------------

def criar_Frame_Top():
    frame_top = Frame(janela, width=1280, height=125, bg=CORBRANCA, relief=SOLID)
    frame_top.pack(padx=0, pady=0)

    frame_detalhes = Frame(frame_top,width=1280,height=174,bg=CORCINZAESCURO,relief=SOLID)
    frame_detalhes.pack(padx=0,pady=0)

    Texto_Productivity = "Productivity"
    label = tk.Label(frame_top, text=Texto_Productivity,fg=CORBRANCA,  bg=CORCINZAESCURO,font=('monospace', 40))
    label.place(x=34,y=50)

    Botao_Home = "Home"
    label = Button(frame_top, text=Botao_Home,fg=CORBRANCA,  bg=CORCINZAESCURO,font=('monospace', 32),relief=FLAT,command=voltar_home)
    label.place(x=625,y=50)

    Botao_Codigo = "Código"
    label = Button(frame_top, text=Botao_Codigo,fg=CORBRANCA,  bg=CORCINZAESCURO,font=('monospace', 32), relief=FLAT,command= abrir_navegador)
    label.place(x=846,y=50)

    Botao_Team = "Team"
    label = Button(frame_top, text=Botao_Team,fg=CORBRANCA,  bg=CORCINZAESCURO,font=('monospace', 32),relief=FLAT)
    label.place(x=1068,y=50)

    frame_detalhes_borda = Frame(frame_top,width=1280,height=4,bg=CORCINZACLARO,relief=SOLID)
    frame_detalhes_borda.pack(padx=0,pady=0)

criar_Frame_Top()

# iniciando frame do meio ====================================================================

frame_meio = Frame(janela, width=1280, height=220, bg=CORBRANCA, relief=SOLID)
frame_meio.pack(padx=0, pady=0, side='right')

img_logo = PhotoImage(file='assets/logo_productivity.png')
label = Label(frame_meio,image=img_logo)
label.pack(padx=90,pady=0,side='left')

frame_centro_Borda = Label(frame_meio,width=1,height=240,bg=CORCINZACLARO,relief=FLAT)
frame_centro_Borda.place(x=380,y=0)

frame_centro = Frame(frame_meio,width=900,height=240,bg=CORCINZAESCURO,relief=SOLID)
frame_centro.pack(padx=0,pady=0,side='right')

img_ToDoList = PhotoImage(file='assets/Ellipse 1.png')
label_ToDoList = Button(frame_meio,image=img_ToDoList,relief=FLAT,bg=CORCINZAESCURO)
label_ToDoList.place(x=385,y=23)

img_Anotacoes = PhotoImage(file='assets/Ellipse 2.png')
label_Anotacoes = Button(frame_meio,image=img_Anotacoes,relief=FLAT,bg=CORCINZAESCURO)
label_Anotacoes.place(x=602,y=23)

img_Calendario = PhotoImage(file='assets/Ellipse 3.png')
label_Calendario = Button(frame_meio,image=img_Calendario,relief=FLAT,bg=CORCINZAESCURO)
label_Calendario.place(x=821,y=23)

img_Pomodoro = PhotoImage(file='assets/Ellipse 4.png')
label_Pomodoro = Button(frame_meio,image=img_Pomodoro,relief=FLAT,bg=CORCINZAESCURO)
label_Pomodoro.place(x=1040,y=23)


# Iniciar o loop de eventos da interface gráfica ==============================================


janela.mainloop()



