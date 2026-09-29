import customtkinter as ctk

from views.dashboard_view import tela_dashboard
from views.administradores_view import tela_administradores
from views.clientes_view import tela_clientes
from views.servicos_view import tela_servicos


def limpar_container(container):

    for widget in container.winfo_children():
        widget.destroy()


def abrir_tela(container, tela):

    limpar_container(container)

    tela(container)


def iniciar_aplicacao(janela):

    sidebar = janela.sidebar
    container = janela.container

    ctk.CTkButton(
        sidebar,
        text="Dashboard",
        fg_color="#294967",
        hover_color="#355C7D",
        command=lambda: abrir_tela(
            container,
            tela_dashboard
        )
    ).pack(
        padx=15,
        pady=5,
        fill="x"
    )

    ctk.CTkButton(
        sidebar,
        text="Administradores",
        fg_color="transparent",
        hover_color="#294967",
        command=lambda: abrir_tela(
            container,
            tela_administradores
        )
    ).pack(
        padx=15,
        pady=5,
        fill="x"
    )

    ctk.CTkButton(
        sidebar,
        text="Clientes",
        fg_color="transparent",
        hover_color="#294967",
        command=lambda: abrir_tela(
            container,
            tela_clientes
        )
    ).pack(
        padx=15,
        pady=5,
        fill="x"
    )

    ctk.CTkButton(
        sidebar,
        text="Serviços",
        fg_color="transparent",
        hover_color="#294967",
        command=lambda: abrir_tela(
            container,
            tela_servicos
        )
    ).pack(
        padx=15,
        pady=5,
        fill="x"
    )

    abrir_tela(
        container,
        tela_dashboard
    )