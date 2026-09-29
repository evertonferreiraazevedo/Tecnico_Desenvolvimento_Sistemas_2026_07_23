# import tkinter as tk

# janela = tk.Tk()# Criação da janela principal
# janela.title("Olá, Tkinter!")
# janela.geometry("300x300")
# janela.resizable(False, False)


# # Rótulo simples
# label = tk.Label(janela, text="Bem-vindo ao Tkinter!", color="blue")
# label.pack()

# # Início do loop principal
# janela.mainloop()

# import tkinter as tk

# def abrir_nova_janela():
#     nova_janela = tk.Toplevel()
#     nova_janela.title("Nova Janela")
#     label = tk.Label(nova_janela, text="Esta é uma nova janela")
#     label.pack(pady=20)

# root = tk.Tk()
# root.title("Janela Principal")

# botao = tk.Button(root, text="Abrir Nova Janela", command=abrir_nova_janela)
# botao.pack(pady=20)
# root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Interface com Frame")

# frame = tk.Frame(root, borderwidth=2, relief="sunken")
# frame.pack(padx=10, pady=10)

# label = tk.Label(frame, text="Este é um frame!")
# label.pack(padx=5, pady=5)

# button = tk.Button(frame, text="Clique aqui")
# button.pack(padx=5, pady=5)

# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.title("Janela Principal")

# def sair():
#     root.destroy()

# def mostrar_mensagem():
#     tk.messagebox.showinfo("Mensagem", "Você clicou no botão!")

# botao_sair = tk.Button(root, text="Sair", command=sair)
# botao_sair.pack(pady=10)

# botao_mensagem = tk.Button(root, text="Mostrar Mensagem", command=mostrar_mensagem)
# botao_mensagem.pack(pady=10)
# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.title("Interface com Frame")

frame = tk.Frame(root, borderwidth=2, relief="sunken")
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Este é um frame!")
label.pack(padx=5, pady=5)

button = tk.Button(frame, text="Clique aqui")
button.pack(padx=5, pady=5)





canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack()

# Desenho de uma linha
canvas.create_line(0, 0, 200, 200, fill="black")

# Desenho de um retângulo
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Desenho de um texto
canvas.create_text(100, 100, text="Olá, Canvas!", font=("Arial", 16))

root.mainloop()
