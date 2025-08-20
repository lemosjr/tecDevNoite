# 10. Você quer fazer um botão que, ao ser clicado, fecha a janela principal.
# 👉 Crie o programa em Tkinter com um botão chamado "Sair", que encerra a aplicação.
import tkinter as tk
def fechar_janela():
    janela.quit()
janela = tk.Tk()
janela.title("Fechar Janela")
janela.geometry("300x100")
botao_sair = tk.Button(janela, text="Sair", command=fechar_janela)
botao_sair.pack(pady=20)
janela.mainloop()
