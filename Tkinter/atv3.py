# 3. Você quer adicionar um botão chamado "Clique aqui" na tela principal do programa.
# 👉 Escreva o código necessário para criar e exibir esse botão na janela.
import tkinter as tk
janela = tk.Tk()
janela.title("Segunda página")
janela.geometry("500x500")
botao = tk.Button(janela, text="Clique aqui")
botao.pack()
janela.mainloop()
