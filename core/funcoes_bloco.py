from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from view import Main_bloco_notas

arquivo_atual_janela = ""
texto_na_pagina = []
numero_paginas_salvas = 0


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
    global numero_paginas_salvas

    if arquivo_atual_janela:
        conteudo_janela = texto.get("1.0", "end-1c")
        with open(arquivo_atual_janela, "w") as salvar:
            salvar.write(conteudo_janela)


    else:
        conteudo_janela = texto.get("1.0", "end-1c")
        arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
        (("Arquivos de Texto", "*.txt"), ("Arquivos python", "*.py")))
        if arquivo:
            with open(arquivo, "w") as salvar:
                salvar.write(conteudo_janela)
                arquivo_atual_janela = arquivo
        numero_paginas_salvas += 1


def salvar_como_arquivo_janela(texto):
    global arquivo_atual_janela
    conteudo_janela = texto.get("1.0", "end-1c")
    arquivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=
    (("Arquivos de Texto", "*.txt"),))
    if arquivo:
        with open(arquivo, "w") as salvar:
            salvar.write(conteudo_janela)
            arquivo_atual_janela = arquivo


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
    if numero_paginas_salvas == 1:
        messagebox.showinfo("Contador", f"Até o momento você salvou {numero_paginas_salvas} nova anotação.")
    elif numero_paginas_salvas == 0:
        messagebox.showinfo("Contador", f"Até o momento você não possui anotações salvas")

    else:
        messagebox.showinfo("Contador", f"Até o momento você salvou{numero_paginas_salvas} novas anotações.")


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
    palavra_desmarcada = "96867763464#4$589&¨%$#490Edsgdg@gas"
    if palavra_desmarcada:
        texto_palavra = texto.get("1.0", "end")
        texto.tag_remove("destaque", "1.0", "end")
        texto_palavra.find(palavra_desmarcada)
        messagebox.showwarning("Aviso", "Todas as palavras foram desmarcadas")


def fechar_janela_destruir(texto):
    conteudo_janela = texto.get("1.0", "end-1c")
    if conteudo_janela != "":
        mensagem = messagebox.askyesno("pergunta", "Deseja salvar suas alterações?")
        if mensagem:
            salvar_arquivo_janela(texto)


def destruir(janela, texto):
    fechar_janela_destruir(texto)
    global arquivo_atual_janela
    arquivo_atual_janela = ""
    janela.destroy()
    Main_bloco_notas.Anotacoes()

def arquivo():
    global arquivo_atual_janela
    arquivo_atual_janela= ""
