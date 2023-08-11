# Importação das bibliotecas e outras necessidades:
from tkinter import *
from tkcalendar import Calendar
from tkinter import simpledialog
from bancoDeDadosEventos import *

# Variáveis globais:
COR_BRANCA = "#F2F2F0"
COR_CINZA_CLARO = "#A5A6A4"
COR_CINZA_ESCURO = "#737373"
COR_LARANJA_CLARO = "#BF8450"
COR_LARANJA_ESCURO = "#BF4C0A"
fonte_titulo = ("mulish", 22, "bold")
fonte_conteudo = ("monospace", 16)

# Inicialização da janela:
janela = Tk()
janela.title("Calendário")
janela.geometry("1280x700")
janela.config(background=COR_BRANCA)
janela.resizable(width="FALSE", height="FALSE")

# Criar três frames

frame_top = Frame(janela, width=1280, height=125, bg=COR_BRANCA, relief=SOLID)
frame_top.pack(padx=0, pady=0)

frame_detalhes = Frame(frame_top, width=1280, height=174, bg=COR_CINZA_ESCURO, relief=SOLID)
frame_detalhes.pack(padx=0, pady=0)

Texto_Productivity = "Productivity"
label = Label(frame_top, text=Texto_Productivity, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 40))
label.place(x=34, y=50)

Botao_Home = "Home"
label = Button(frame_top, text=Botao_Home, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
label.place(x=625, y=50)

Botao_Codigo = "Código"
label = Button(frame_top, text=Botao_Codigo, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
label.place(x=846, y=50)

Botao_Team = "Team"
label = Button(frame_top, text=Botao_Team, fg=COR_BRANCA, bg=COR_CINZA_ESCURO, font=('monospace', 32), relief=FLAT)
label.place(x=1068, y=50)

frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=COR_CINZA_CLARO, relief=SOLID)
frame_detalhes_borda.pack(padx=0, pady=0)

# Chamando o banco e widgets
sistema_de_registro = BancoDeEventos()
widgets_eventos = {}

# Calendario e botao
frame_calendario = Frame(janela, bg=COR_BRANCA)
frame_calendario.pack(side="left", fill="both", expand=True)

# Criando tabela para eventos salvos
frame_tabela = Frame(janela, width=200, height=100, bg=COR_CINZA_CLARO, relief=SOLID)
frame_tabela.pack(side="right", padx=5, pady=10, fill="both", expand=True)

# Calendário
cal = Calendar(
    frame_calendario,
    selectmode="day",
    year=2023,
    month=1,
    day=1,
    locale="pt_BR",
    date_pattern="dd/mm/yyyy"
)

cal.configure(
    background="#737373",
    foreground="#A5A6A4",
    selectbackground="#BF4C0A",
    selectforeground="#F2F2F0",
    font=("monospace", 14)
)

cal.pack(side="top", padx=10, pady=20, fill="both", expand=True)

# Funções do calendário
def selecionar_data():
    selected_date = cal.get_date()
    event = simpledialog.askstring(
        "Adicionar Evento", f"Digite o evento para {selected_date}:", parent=frame_calendario
    )
    if event:
        eventos = (selected_date, event)
        sistema_de_registro.insere_na_tabela(eventos)

def mostrar_eventos_para_data(data):
    event_label.config(text="Eventos para " + data)
    for widget in frame_tabela.winfo_children():
        widget.destroy()
    dados = sistema_de_registro.ver_todos_eventos()
    for evento_id, evento_data, evento_descricao in dados:
        if evento_data == data:
            evento_frame = Frame(frame_tabela)
            evento_label = Label(evento_frame, text=evento_descricao, font=fonte_conteudo)
            remover_button = Button(evento_frame, text="Remover", command=lambda ev=evento_descricao: remover_evento(data, ev, evento_id))
            evento_label.pack(side="left")
            remover_button.pack(side="right")
            evento_frame.pack(fill="x", padx=10, pady=5)
            widgets_eventos[evento_id] = evento_frame

def ao_selecionar_data(event):
    data_selecionada = cal.get_date()
    mostrar_eventos_para_data(data_selecionada)

def mostrar_evento(data, evento):
    event_label.config(text=f"Evento em {data}: {evento}")

event_label = Label(frame_calendario, text="", font=fonte_conteudo)
event_label.pack(pady=10)
cal.bind("<<CalendarSelected>>", ao_selecionar_data)

def remover_eventos_salvos():
    sistema_de_registro.delete_all_eventos()
    event_label.config(text="")

def remover_evento(data, evento, evento_id):
    dados_eventos = sistema_de_registro.ver_todos_eventos()
    for e_id, evento_data, evento_descricao in dados_eventos:
        if evento_data == data and evento_descricao == evento:
            sistema_de_registro.delete_evento(e_id)
            if e_id in widgets_eventos:
                widgets_eventos[e_id].destroy()
                del widgets_eventos[e_id]
            mostrar_eventos_para_data(data)
            break

# Botões de interação
Button(
    frame_calendario,
    text="Clique aqui para agendar seu evento",
    command=selecionar_data,
    font=fonte_conteudo
).pack(padx=5, pady=5)

# Loop para continuar em execução
janela.mainloop()
