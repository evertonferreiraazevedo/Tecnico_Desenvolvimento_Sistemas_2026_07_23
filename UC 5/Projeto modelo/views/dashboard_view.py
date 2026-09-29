import customtkinter as ctk


def tela_dashboard(container):

    titulo = ctk.CTkLabel(
        container,
        text="Dashboard",
        font=("Arial", 28, "bold"),
        text_color="#122B43"
    )

    titulo.pack(
        anchor="w",
        padx=32,
        pady=(30, 5)
    )

    subtitulo = ctk.CTkLabel(
        container,
        text="Visão geral dos cadastros do sistema.",
        font=("Arial", 14),
        text_color="#52677D"
    )

    subtitulo.pack(
        anchor="w",
        padx=32
    )

    frame_cards = ctk.CTkFrame(
        container,
        fg_color="transparent"
    )

    frame_cards.pack(
        fill="x",
        padx=32,
        pady=30
    )

    criar_card(
        frame_cards,
        "Administradores",
        "0"
    )

    criar_card(
        frame_cards,
        "Clientes",
        "0"
    )

    criar_card(
        frame_cards,
        "Serviços",
        "0"
    )


def criar_card(container, titulo, valor):

    card = ctk.CTkFrame(
        container,
        height=120,
        fg_color="white",
        corner_radius=10
    )

    card.pack(
        side="left",
        fill="both",
        expand=True,
        padx=8
    )

    ctk.CTkLabel(
        card,
        text=titulo,
        font=("Arial", 14),
        text_color="#52677D"
    ).pack(
        anchor="w",
        padx=20,
        pady=(20, 5)
    )

    ctk.CTkLabel(
        card,
        text=valor,
        font=("Arial", 30, "bold"),
        text_color="#122B43"
    ).pack(
        anchor="w",
        padx=20
    )