# 6. Você está criando um formulário simples para coletar o nome do usuário.
# 👉 Faça um programa em Tkinter com uma janela contendo um rótulo (Label) escrito "Digite seu nome:" e uma caixa de texto (Entry) logo abaixo.

import tkinter as tk
def enviar_nome():
    nome = entrada_nome.get()
    print(f"Nome digitado: {nome}")
janela = tk.Tk()
janela.title("Formulário de Nome")
janela.geometry("300x150")
rotulo = tk.Label(janela, text="Digite seu nome:")
rotulo.pack(pady=10)
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=5)
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_nome)
botao_enviar.pack(pady=10)
janela.mainloop()