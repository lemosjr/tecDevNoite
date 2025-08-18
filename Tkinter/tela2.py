import tkinter as tk
from tkinter import ttk

#Criar janela principal
janela = tk.Tk()
janela.title("Formulário de cadastro")
janela.geometry("800x600")
janela.configure(bg="#f0f0f0", width=40)

#definir tema
style = ttk.Style()
style.theme_use("clam")#tema moderno
style.configure("TLabel", font=("Arial", 10), background="#f0f0f0")
style.configure("TEntry", padding=5)
style.configure("TButton", font=("Arial", 11, "bold"), padding=6, foreground="#ffffff", background="#0078d7")
style.map("TButton", background=[("active", "#005bb5")])

#Titulo do formulário
titulo = tk.Label(
    janela,
    text="Cadastro de Usuário",
    font=("Arial", 16),
    bg="#f0f0f0",
    foreground="#333333"
)
titulo.grid(row=0, column=0, columnspan=4, pady=20) #centralizando

#Rótulos

#nome
ttk.Label(janela, text="Nome:", font="50px").grid(row=1, column=1, padx=15, pady=8, sticky="w")
caixa_nome = ttk.Entry(janela, width=40)
caixa_nome.grid(row=1, column=2, padx=15, pady=8, sticky="ew")

#sobrenome
ttk.Label(janela, text="Sobrenome:", font="50px").grid(row=2, column=1, padx=15, pady=8, sticky="w")
caixa_sobrenome = ttk.Entry(janela, width=40)
caixa_sobrenome.grid(row=2, column=2, padx=15, pady=8, sticky="ew")

#email
ttk.Label(janela, text="Email:", font="50px").grid(row=3, column=1, padx=15, pady=8, sticky="w")
caixa_email = ttk.Entry(janela, width=40)
caixa_email.grid(row=3, column=2, padx=15, pady=8, sticky="ew")

#telefone
ttk.Label(janela, text="Telefone:",font="50px").grid(row=4, column=1, padx=15, pady=8, sticky="w")
caixa_telefone = ttk.Entry(janela, width=40)
caixa_telefone.grid(row=4, column=2, padx=15, pady=8, sticky="ew")

#endereço
ttk.Label(janela, text="Endereço:",font="50px").grid(row=5, column=1, padx=15, pady=8, sticky="w")
caixa_endereco = ttk.Entry(janela, width=40)
caixa_endereco.grid(row=5, column=2, padx=15, pady=8, sticky="ew")

# botões 
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.grid(row=6, column=0, columnspan=4, pady=20)

botao_limpar = ttk.Button(frame_botoes, text="Limpar")
botao_limpar.pack(side="left", padx=10, pady=5)

botao_salvar = ttk.Button(frame_botoes, text="Salvar")
botao_salvar.pack(side="left", padx=10, pady=5)

botao_cancelar = ttk.Button(frame_botoes, text="Cancelar")
botao_cancelar.pack(side="left", padx=10, pady=5)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

janela.mainloop()