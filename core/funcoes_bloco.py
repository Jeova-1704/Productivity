from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from utils import colors, fonts
arquivo_atual_janela = ""
texto_na_pagina = []
numero_paginas_abertas = 0




def janela_principal():

    janela = Tk()
    global numero_paginas_abertas
    numero_paginas_abertas += 1
    janela.title("Bloco de Notas")

    texto = Text(janela, wrap="word", height=40, width=100, font=fonts.fonte_conteudo)
    texto.pack()

    # dimensoes
    largura_total_janela = janela.winfo_screenwidth()
    altura_total_janela = janela.winfo_screenheight()
    largura_janela = 1280
    altura_janela = 700
    posicao_eixo_x = largura_total_janela/2 - largura_janela/2
    posicao_eixo_y = altura_total_janela/2 - altura_janela/2
    janela.geometry("%dx%d+%d+%d" % (largura_janela, altura_janela, posicao_eixo_x, posicao_eixo_y))
    janela.resizable(FALSE, FALSE)
    # Menu
    menu_janela = Menu(janela)
    file_menu_janela_bloco_notas = Menu(menu_janela, tearoff=0)
    menu_janela.add_cascade(label="Arquivo", menu=file_menu_janela_bloco_notas)
    file_menu_janela_bloco_notas.add_command(label="Nova página", command=janela_principal)
    file_menu_janela_bloco_notas.add_command(label="Abrir...", command=lambda: abrir_arquivo_janela(texto))
    file_menu_janela_bloco_notas.add_command(label="Salvar", command=lambda: salvar_arquivo_janela(texto))
    file_menu_janela_bloco_notas.add_command(label="Salvar como...", command=lambda: salvar_como_arquivo_janela(texto))
    file_menu_janela_bloco_notas.add_separator()
    file_menu_janela_bloco_notas.add_command(label="Sair", command=lambda: fechar_janela(texto, janela))
    menu_janela.add_command(label="Procurar", command=lambda: pesquisar_palavra(texto))
    menu_janela.add_command(label="Desmarcar texto", command=lambda: desmarcar_palavra(texto))
    menu_janela.add_command(label="Contador", command=contador)
    janela.config(menu=menu_janela)
    janela.protocol("WM_DELETE_WINDOW", lambda: fechar_janela(texto, janela))
    janela.mainloop()



def abrir_arquivo_janela(texto):
    global arquivo_atual_janela
    arquivo_janela = filedialog.askopenfilename(filetypes=(("Arquivos de Texto", "*.txt"), ("Arquivos Python", "*.py")))
    if arquivo_janela:
        arquivo_atual_janela = arquivo_janela
        with open(arquivo_janela, "r") as file_janela:
            conteudo = file_janela.read()
            texto.delete("1.0", "end")
            texto.insert("1.0", conteudo)


def salvar_arquivo_janela(texto):
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


def fechar_janela(texto, janela):
    conteudo_janela = texto.get("1.0", "end-1c")
    if conteudo_janela != "":
        mensagem = messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            salvar_arquivo_janela(texto)
            janela.destroy()
        else:
            janela.destroy()
    else:
        janela.destroy()


def contador():
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