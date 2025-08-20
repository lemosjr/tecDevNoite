# 8. Imagine que você está desenvolvendo um programa de aviso.
# 👉 Crie uma janela com um rótulo (Label) escrito "Atenção!" em fonte grande e em vermelho.
import tkinter as tk
def criar_janela_avisos():
    janela_avisos = tk.Tk()
    janela_avisos.title("Aviso")
    janela_avisos.geometry("300x200")
    rotulo_avisos = tk.Label(janela_avisos, text="Atenção!", font=("Arial", 24), fg="red")
    rotulo_avisos.pack(expand=True)
    janela_avisos.mainloop()
criar_janela_avisos()