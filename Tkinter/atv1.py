# 1. Você está criando um programa em Python e precisa abrir a janela principal onde os botões e rótulos serão exibidos.
# 👉 Escreva o código necessário para criar a janela principal usando Tkinter.


import tkinter as tk

janela = tk.Tk()
janela.title("Primeira página") 
janela.geometry("500x500")

#rotulos

rotulo1 = tk.Label(janela, text="Login:")
rotulo1.pack(pady=5)
caixa1 = tk.Entry(janela, width=40)
caixa1.pack(pady=5)

rotulo2 = tk.Label(janela, text="Senha:")
rotulo2.pack(pady=5)
caixa2 = tk.Entry(janela, width=40)
caixa2.pack(pady=5)

botao = tk.Button(janela, text="Entrar", width=10)
botao.pack(pady=5)

botao1 = tk.Button(janela,text="Cancelar")
botao1.pack(pady=5)

janela.mainloop()