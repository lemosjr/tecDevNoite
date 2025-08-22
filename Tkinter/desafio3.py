# Atividade 3 – Identificador de números
# Situação: Um professor de matemática quer um programa que diga se um número é positivo,
# negativo ou igual a zero.
# Tarefa do aluno:
# - Crie um programa em Tkinter que permita ao usuário digitar um número.
# - Ao clicar no botão:
# • Se o número for maior que zero, mostre 'Número positivo'.
# • Se for menor que zero, mostre 'Número negativo'.
# • Se for zero, mostre 'Número igual a zero'.

import tkinter as tk
from tkinter import messagebox
def verificar_numero():
    try:
        numero = float(entry_numero.get())
        if numero > 0:
            messagebox.showinfo(title="Resultado", message="Número positivo")
        elif numero < 0:
            messagebox.showinfo(title="Resultado", message="Número negativo")
        else:
            messagebox.showinfo(title="Resultado", message="Número igual a zero")
    except ValueError:
        messagebox.showerror(title="Erro", message="Digite um valor numérico válido.")
app = tk.Tk()
app.title("Identificador de Números")
app.geometry("600x400")
tk.Label(app, text="Digite um número:").pack(pady=5)
entry_numero = tk.Entry(app)
entry_numero.pack(pady=5)
tk.Button(app, text="Verificar", command=verificar_numero).pack(pady=20)
app.mainloop()