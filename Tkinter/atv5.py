#  5. Em uma aplicação, ao clicar em um botão, você quer abrir uma nova janela chamada "Segunda Tela".
# 👉 Escreva o código em Tkinter que cria essa nova janela a partir da tela principal.
import tkinter as tk
def abrir_segunda_tela():
    segunda_tela = tk.Toplevel()
    segunda_tela.title("Segunda Tela")
    segunda_tela.geometry("400x400")
    rotulo = tk.Label(segunda_tela, text="Bem-vindo à Segunda Tela!")
    rotulo.pack()
janela = tk.Tk()
janela.title("Tela Principal")
janela.geometry("500x500")
botao = tk.Button(janela, text="Abrir Segunda Tela", command=abrir_segunda_tela)
botao.pack()
janela.mainloop()
