# 2. Um colega criou a janela principal do Tkinter, mas quando executa o programa, ela fecha imediatamente.
# 👉 Escreva a linha de código que faz a janela permanecer aberta aguardando interações do usuário.

import tkinter as tk
janela = tk.Tk()
janela.title("Segunda página")
janela.geometry("500x500")
janela.mainloop()
