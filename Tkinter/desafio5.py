# Atividade 5 – Cardápio interativo
# Situação: Um restaurante quer um sistema simples para mostrar os preços dos produtos do
# cardápio. O cliente escolhe digitando um número.
# Cardápio:
# 1■■ Pizza – R$ 30,00
# 2■■ Hambúrguer – R$ 20,00
# 3■■ Refrigerante – R$ 5,00
# Tarefa do aluno:
# - Crie um programa com Tkinter que mostre o cardápio e permita o cliente digitar uma opção (1, 2 ou 3).
# - Ao clicar no botão:
# • Se o cliente digitar 1, mostre 'Pizza – R$ 30,00'.
# • Se digitar 2, mostre 'Hambúrguer – R$ 20,00'.
# • Se digitar 3, mostre 'Refrigerante – R$ 5,00'.
# • Se digitar qualquer outra coisa, mostre 'Opção inválida'.

import tkinter as tk
from tkinter import messagebox
def mostrar_preco():
    opcao = entry_opcao.get()
    if opcao == '1':
        messagebox.showinfo(title="Cardápio", message="Pizza – R$ 30,00")
    elif opcao == '2':
        messagebox.showinfo(title="Cardápio", message="Hambúrguer – R$ 20,00")
    elif opcao == '3':
        messagebox.showinfo(title="Cardápio", message="Refrigerante – R$ 5,00")
    else:
        messagebox.showerror(title="Erro", message="Opção inválida")
app = tk.Tk()
app.title("Cardápio Interativo")
app.geometry("600x400")
tk.Label(app, text="Escolha uma opção do cardápio:").pack(pady=5)
tk.Label(app, text="1. Pizza – R$ 30,00").pack()
tk.Label(app, text="2. Hambúrguer – R$ 20,00").pack()
tk.Label(app, text="3. Refrigerante – R$ 5,00").pack(pady=5)
entry_opcao = tk.Entry(app)
entry_opcao.pack(pady=5)
tk.Button(app, text="Ver Preço", command=mostrar_preco).pack(pady=20)
app.mainloop()