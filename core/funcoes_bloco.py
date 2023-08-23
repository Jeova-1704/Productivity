from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from utils import colors, fonts
from core import funcoes_main
arquivo_atual_janela = ""
texto_na_pagina = []
numero_paginas_abertas = 0


class Anotacoes:

    def __init__(self):
        global numero_paginas_abertas
        self.janela = Tk()
        self.janela.title("Calendário")
        self.janela.geometry("1280x700")
        self.janela.config(background='#F2F2F0')
        self.janela.resizable(width=FALSE, height=FALSE)

        numero_paginas_abertas += 1

        frame_top = Frame(self.janela, width=1280, height=125, bg=colors.COR_BRANCA, relief=SOLID)
        frame_top.pack(padx=0, pady=0)

        frame_detalhes = Frame(frame_top, width=1280, height=174, bg=colors.COR_CINZA_ESCURO, relief=SOLID)
        frame_detalhes.pack(padx=0, pady=0)

        Texto_Productivity = "Productivity"
        label = Label(frame_top, text=Texto_Productivity, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                      font=('monospace', 40))
        label.place(x=34, y=50)

        Botao_Home = "Home"
        label = Button(frame_top, text=Botao_Home, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), relief=FLAT, command=lambda: funcoes_main.renderizar_home(self.janela)
                       )
        label.place(x=625, y=50)

        Botao_Codigo = "DashBoard"
        label = Button(frame_top, text=Botao_Codigo, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32),
                       relief=FLAT)
        label.place(x=800, y=50)

        Botao_Team = "Sobre"
        label = Button(frame_top, text=Botao_Team, fg=colors.COR_BRANCA, bg=colors.COR_CINZA_ESCURO,
                       font=('monospace', 32), relief=FLAT, command=lambda: funcoes_main.renderizar_team(self.janela))
        label.place(x=1068, y=50)

        frame_detalhes_borda = Frame(frame_top, width=1280, height=4, bg=colors.COR_CINZA_CLARO, relief=SOLID)
        frame_detalhes_borda.pack(padx=0, pady=0)

        self.texto = Text(self.janela,wrap="word",height=25,width=200,font=fonts.fonte_conteudo)
        self.texto.pack()

        menu_janela = Menu(self.janela)
        file_menu_janela_bloco_notas = Menu(menu_janela, tearoff=0)
        menu_janela.add_cascade(label="Arquivo", menu=file_menu_janela_bloco_notas)
        file_menu_janela_bloco_notas.add_command(label="Nova página", command=Anotacoes)
        file_menu_janela_bloco_notas.add_command(label="Abrir...", command=lambda: self.abrir_arquivo_janela(self.texto))
        file_menu_janela_bloco_notas.add_command(label="Salvar", command=lambda: self.salvar_arquivo_janela(self.texto))
        file_menu_janela_bloco_notas.add_command(label="Salvar como...", command=lambda: self.salvar_como_arquivo_janela(self.texto))
        file_menu_janela_bloco_notas.add_separator()
        file_menu_janela_bloco_notas.add_command(label="Sair", command=lambda: self.fechar_janela(self.texto, self.janela))
        menu_janela.add_command(label="Procurar", command=lambda: self.pesquisar_palavra(self.texto))
        menu_janela.add_command(label="Desmarcar texto", command=lambda: self.desmarcar_palavra(self.texto))
        menu_janela.add_command(label="Contador", command=self.contador)
        self.janela.config(menu=menu_janela)
        self.janela.protocol("WM_DELETE_WINDOW", lambda: self.fechar_janela(self.texto, self.janela))
        self.janela.mainloop()



    def abrir_arquivo_janela(self,texto):
        global arquivo_atual_janela
        arquivo_janela = filedialog.askopenfilename(filetypes=(("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
        if arquivo_janela:
            arquivo_atual_janela = arquivo_janela
            with open(arquivo_janela, "r") as file_janela:
                conteudo = file_janela.read()
                texto.delete("1.0", "end")
                texto.insert("1.0", conteudo)


    def salvar_arquivo_janela(self,texto):
        global arquivo_atual_janela
        if arquivo_atual_janela:
            conteudo_janela = texto.get("1.0", "end-1c")
            with open(arquivo_atual_janela, "w") as salvar:
                salvar.write(conteudo_janela)





    def salvar_como_arquivo_janela(texto):
        conteudo_janela = texto.get("1.0", "end-1c")
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
        (("Arquivos de Texto", "*.txt"),))
        if arquivo:
            with open(arquivo, "w") as salvar:
                salvar.write(conteudo_janela)


    def fechar_janela(self,texto, janela):
        conteudo_janela = texto.get("1.0", "end-1c")
        if conteudo_janela != "":
            mensagem = messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
            if mensagem:
                self.salvar_arquivo_janela(texto)
                janela.destroy()
            else:
                janela.destroy()
        else:
            janela.destroy()


    def contador(self):
        if numero_paginas_abertas == 1:
            messagebox.showinfo("Contador", f"Até o momento você criou {numero_paginas_abertas} nova anotação.")
        else:
            messagebox.showinfo("Contador", f"Até o momento você criou {numero_paginas_abertas} novas anotações.")


    def pesquisar_palavra(texto):
        palavra_pesquisada = simpledialog.askstring("Pesquisar", "Digite a palavra a ser pesquisada:")
        if palavra_pesquisada:
            texto_palavra = texto.get("1.0", "end")
            texto.tag_remove("destaque", "1.0", "end")
            posicao = texto_palavra.find(palavra_pesquisada)
            if palavra_pesquisada not in texto_palavra:
                messagebox.showwarning("Aviso", f"A palavra: {palavra_pesquisada} não foi encontrada")
            else:
                messagebox.showwarning("Aviso", f"Todas as plavras com: *{palavra_pesquisada}* foram destacadas")

            while posicao != -1:
                inicio = f"1.0+{posicao}c"
                fim = f"1.0+{posicao + len(palavra_pesquisada)}c"
                texto.tag_add("destaque", inicio, fim)
                posicao = texto_palavra.find(palavra_pesquisada, posicao + 1)
            texto.tag_config("destaque", background="green")


    def desmarcar_palavra(texto):
        palavra_desmarcada = "96867763464#4$589490Edsgdg@gas"
        if palavra_desmarcada:
            texto_palavra = texto.get("1.0", "end")
            texto.tag_remove("destaque", "1.0", "end")
            texto_palavra.find(palavra_desmarcada)
            messagebox.showwarning("Aviso", "Todas as palavras foram desmarcadas")