# 4. Você adicionou um rótulo (Label) e um botão, mas eles não aparecem corretamente organizados na tela.
# 👉 Mostre como usar o método correto (pack) para posicionar esses widgets dentro da janela principal.
import tkinter as tk
janela = tk.Tk()
janela.title("Segunda página")
janela.geometry("500x500")
rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.pack()
botao = tk.Button(janela, text="Clique aqui")
botao.pack()
janela.mainloop()
