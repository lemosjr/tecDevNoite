import tkinter as tk

def abrir_segunda_tela():
    segunda_tela = tk.Toplevel()
    segunda_tela.title("Segunda tela")
    segunda_tela.geometry("300x300")

    label2 = tk.Label(segunda_tela, text="Você esta aqui", font=("Arial", 12))
    label2.pack(pady=20)
    
    btn_voltar = tk.Button(segunda_tela, text="Fechar", command=segunda_tela.destroy)
    btn_voltar.pack()
    

#tela principal
root = tk.Tk()
root.title("Tela Principal")
root.geometry("300x300")
    
label = tk.Label(root, text="Bem-vindo", font=("Arial", 12))
label.pack(pady=20)
    
botao_ir = tk.Button(root, text="ir para a segunda tela", command=abrir_segunda_tela)
botao_ir.pack()    
root.mainloop()