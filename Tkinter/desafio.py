
import tkinter as tk
from tkinter import messagebox

def verificar_idade():
    try:
        idade = int(entry_idade.get())
        if idade < 18 and idade >= 0:
            messagebox.showinfo(title="Menor de idade", message="Você é menor de idade")
        else:
            messagebox.showinfo(title="Maior de idade", message="Você é maior de idade")
    except ValueError:
        messagebox.showinfo(title="Entrada inválida", message="entrada inválida")            
root = tk.Tk()
root.title("Verificação de Idade")

tk.Label(root, text="Digite sua idade:").pack(pady=5)
entry_idade = tk.Entry(root)
entry_idade.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_idade).pack(pady=10)

root.mainloop()
