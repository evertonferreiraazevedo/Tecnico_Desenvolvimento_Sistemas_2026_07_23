import customtkinter as ctk


def criar_janela():

    janela = ctk.CTk()

    janela.title("Sistema de Cadastro")
    janela.geometry("1100x650")
    janela.resizable(False, False)

    sidebar = ctk.CTkFrame(
        janela,
        width=220,
        corner_radius=0,
        fg_color="#122B43"
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    ctk.CTkLabel(
        sidebar,
        text="Sistema de Cadastro",
        font=("Arial", 18, "bold"),
        text_color="white"
    ).pack(
        pady=(30, 35)
    )

    container = ctk.CTkFrame(
        janela,
        fg_color="#F5F9FC",
        corner_radius=0
    )

    container.pack(
        side="right",
        fill="both",
        expand=True
    )

    janela.sidebar = sidebar
    janela.container = container

    return janela