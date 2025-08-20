# 7. Em uma aplicação de calculadora, você precisa adicionar dois botões, um chamado "Somar" e outro chamado "Subtrair".
# 👉 Crie uma janela com esses dois botões lado a lado.
import tkinter as tk
def somar():
    print("Botão Somar clicado")
def subtrair():
    print("Botão Subtrair clicado")
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x100")
botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.pack(side=tk.LEFT, padx=10, pady=20)
botao_subtrair = tk.Button(janela, text="Subtrair", command=subtrair)
botao_subtrair.pack(side=tk.LEFT, padx=10, pady=20)
janela.mainloop()
