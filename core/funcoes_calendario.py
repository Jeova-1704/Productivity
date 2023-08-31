from tkinter import simpledialog
from tkinter import *
from dao.bdCalendario import BancoDeEventos
from tkinter import messagebox


class Funcoes:

    def __init__(self, frame_calendario, cal, frame_tabela, root):
        self.frame_calendario = frame_calendario
        self.cal = cal
        self.frame_tabela = frame_tabela
        self.root = root
        self.event_label = Label(self.frame_calendario, text="", font=("monospace", 16))
        self.event_label.pack(pady=10)
        self.cal.bind("<<CalendarSelected>>", self.ao_selecionar_data)

        self.sistema_de_registro = BancoDeEventos()
        self.widgets_eventos = {}

    def selecionar_data(self):
        selected_date = self.cal.get_date()

        event_input = simpledialog.askstring("Adicionar Evento", f"Digite o evento para {selected_date}:",
                                             parent=self.frame_calendario)

        if event_input is not None:
            time_input = simpledialog.askstring("Adicionar Evento", "Qual o horário do seu evento?:",
                                                parent=self.frame_calendario)

            event = (selected_date, event_input, time_input)
            self.sistema_de_registro.insere_na_tabela(event)
            self.mostrar_eventos_para_data(selected_date)

    def ao_selecionar_data(self, event):
        data_selecionada = self.cal.get_date()
        self.mostrar_eventos_para_data(data_selecionada)

    def mostrar_eventos_para_data(self, data):

        self.image = PhotoImage(file="assets/toDoList_delete.png")
        self.image_resized = self.image.subsample(3, 3)

        self.event_label.config(text="Eventos para " + data)

        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        dados = self.sistema_de_registro.ver_todos_eventos()
        for evento_id, evento_data, evento_descricao, evento_horario in dados:
            if evento_data == data:
                evento_frame = Frame(self.frame_tabela)
                evento_label = Label(evento_frame, text=evento_descricao, font=("monospace", 16))
                hora_label = Label(evento_frame, text=evento_horario, font=("monospace", 14))
                remover_button = Button(evento_frame, text="Remover", bg="#BF4C0A", image=self.image_resized,
                                        relief=GROOVE,
                                        command=lambda ev=evento_descricao: self.remover_evento(data, ev, evento_id))
                evento_label.pack(side="left")
                hora_label.pack(side="left")
                remover_button.pack(side="right")
                evento_frame.pack(fill="x", padx=10, pady=5)
                self.widgets_eventos[evento_id] = evento_frame

    def remover_evento(self, data, evento, evento_id):
        dados_eventos = self.sistema_de_registro.ver_todos_eventos()
        for e_id, evento_data, evento_descricao, evento_horario in dados_eventos:
            if evento_data == data and evento_descricao == evento:

                mensagem = f"O evento '{evento}' foi deletado com sucesso!"
                messagebox.showinfo("Evento Deletado", mensagem)

                self.sistema_de_registro.delete_evento(e_id)

                if e_id in self.widgets_eventos:
                    self.widgets_eventos[e_id].destroy()
                    del self.widgets_eventos[e_id]
                self.mostrar_eventos_para_data(data)

                break


if __name__ == "__main__":
    root = Tk()
    app = Funcoes(root, None)
    root.mainloop()
