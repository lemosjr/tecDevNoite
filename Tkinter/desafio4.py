# Atividade 4 – Sistema de senha
# Situação: Um sistema de segurança precisa verificar se a senha digitada pelo usuário está correta.
# A senha correta é '1234'.
# Tarefa do aluno:
# - Crie um programa com Tkinter que tenha um campo para o usuário digitar a senha.
# - Ao clicar no botão:
# • Se a senha for '1234', mostre 'Acesso permitido'.
# • Caso contrário, mostre 'Acesso negado'.
# Dica: use Entry com show='*' para esconder a senha.

import tkinter as tk
from tkinter import messagebox
def verificar_senha():
    senha = entry_senha.get()
    if senha == '1234':
        messagebox.showinfo(title="Acesso", message="Acesso permitido")
    else:
        messagebox.showerror(title="Acesso", message="Acesso negado")
app = tk.Tk()
app.title("Sistema de Senha")
app.geometry("600x400")
tk.Label(app, text="Digite a senha:").pack(pady=5)
entry_senha = tk.Entry(app, show='*')
entry_senha.pack(pady=5)
tk.Button(app, text="Verificar Senha", command=verificar_senha).pack(pady=20)
app.mainloop()