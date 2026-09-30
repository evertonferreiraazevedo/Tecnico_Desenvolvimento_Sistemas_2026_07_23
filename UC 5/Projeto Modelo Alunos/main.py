import customtkinter as ctk
from views.aluno_view import tela_alunos


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
janela = ctk.CTk()
janela.title("Cadastro de Alunos")
janela.geometry("700x600")
# janela.resizable(False, False)
container = ctk.CTkFrame(janela)
container.pack(fill="both", expand=False)

tela_alunos(container)
janela.mainloop()