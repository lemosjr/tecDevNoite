import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.geometry("820x500")
janela.title("Cadastro cliente")

#Frames
frame_dados_clientes = tk.LabelFrame(text="Dados do cliente", bg="#0A9999")
frame_dados_clientes.grid()

frame_clientes_cadastrados = tk.LabelFrame(text="Clientes cadastrados", bg="#0A9999")
frame_clientes_cadastrados.grid()

botao_excluir_varios = tk.Button(frame_clientes_cadastrados,\
text="remover selecionado", command=0)
botao_excluir_varios.grid(row=1, column=0, padx=10, pady=10, sticky='e')
tree = ttk.Treeview(frame_clientes_cadastrados, columns=('Id', 'Nome', 'Email', 'Telefone'), show="headings")
tree.heading('Id', text='Id')
tree.heading('Nome', text='Nome')
tree.heading('Email', text='Email')
tree.heading('Telefone', text='Telefone')
tree.grid(row=0, column=0)


#nome
label_nome = tk.Label(frame_dados_clientes, text="Nome:",bg="#0A9999")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entry_nome = tk.Entry(frame_dados_clientes)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

#email
label_email = tk.Label(frame_dados_clientes, text="Email:", bg="#0A9999")
label_email.grid(row=1, column=0, padx=5, pady=5)

entry_email = tk.Entry(frame_dados_clientes)
entry_email.grid(row=1, column=1, padx=5, pady=5)

#telfone
label_telefone = tk.Label(frame_dados_clientes, text="Email:", bg="#0A9999")
label_telefone.grid(row=2, column=0, padx=5, pady=5)

entry_telefone = tk.Entry(frame_dados_clientes)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

#pesquisar
label_pesquisar = tk.Button(frame_dados_clientes, text="Pesquisar:", bg="#0A9999", padx=40)
label_pesquisar.grid(row=0, column=4, padx=5, pady=5)

entry_pesquisar = tk.Entry(frame_dados_clientes, width=25)
entry_pesquisar.grid(row=0, column=3, padx=5, pady=5)

#Botões

#cadastrar
botao_cadastrar = tk.Button(frame_dados_clientes, text="Cadastrar", width=20)
botao_cadastrar.grid(row=3, column=0, padx=5, pady=5)

#limpar
botao_limpar = tk.Button(frame_dados_clientes, text="Limpar", width=20)
botao_limpar.grid(row=3, column=1, padx=5, pady=5)

#excluir
botao_excluir = tk.Button(frame_dados_clientes, text="Excluir", width=20)
botao_excluir.grid(row=3, column=2, padx=5, pady=5)

#desfazer
botao_desfazer = tk.Button(frame_dados_clientes, text="Desfazer", width=20)
botao_desfazer.grid(row=3, column=3, padx=5, pady=5)

#salvar
botao_salvar = tk.Button(frame_dados_clientes, text="Salvar", width=20)
botao_salvar.grid(row=3, column=4, padx=5, pady=5)

janela.mainloop() 