# Atividade 2 – Resultado escolar
# Situação: Uma escola quer automatizar o sistema de boletins. O programa deve dizer ao aluno se
# ele está aprovado, em recuperação ou reprovado, com base na nota final.
# Tarefa do aluno:
# - Crie um programa com Tkinter que peça a nota final do aluno (0 a 10).
# - Ao clicar no botão:
# • Se a nota for maior ou igual a 7, mostre 'Aprovado'.
# • Se for entre 5 e 6,9, mostre 'Recuperação'.
# • Se for menor que 5, mostre 'Reprovado'.

import tkinter as tk
from tkinter import messagebox

def checar_nota():
    try:
        nota = float(entry_nota.get())
        if nota >= 7:
            messagebox.showinfo(title="Aprovado", message="Você foi aprovado!!!")
        elif nota >= 5:
            messagebox.showinfo(title="Recuperação", message="Você está de recuperação")
        else:
            messagebox.showinfo(title="Reprovado", message="Você está reprovado")
    except ValueError:
        messagebox.showerror(title="Erro", message="Digite um valor numérico válido.")

app = tk.Tk()
app.title("Resultado escolar")
app.geometry("600x400")

tk.Label(app, text="Digite sua nota:").pack(pady=5)
entry_nota = tk.Entry(app)
entry_nota.pack(pady=5)
tk.Button(app, text="Verificar Resultado", command=checar_nota).pack(pady=20)
app.mainloop()