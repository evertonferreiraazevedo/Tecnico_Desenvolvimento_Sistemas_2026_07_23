import customtkinter as ctk
from tkinter import messagebox

from controllers.cliente_controller import (
    cadastrar_cliente,
    excluir_cliente
)

from models.cliente_model import carregar_clientes


cor_fundo = "#E9E9E9"
cor_frame = "#FFFFFF"
sub_titulo = "#52677F"
borda_frame = "#e0e0e0"
cor_botao = "#262753"


def tela_clientes(container):

    frame_conteudo = ctk.CTkFrame(
        container,
        fg_color="transparent"
    )

    frame_conteudo.pack(
        fill="both",
        expand=True
    )

    # ==================================================
    # TÍTULO
    # ==================================================

    titulo = ctk.CTkLabel(
        frame_conteudo,
        text="Clientes",
        font=("Arial", 28, "bold"),
        text_color="#122B43"
    )

    titulo.pack(
        anchor="w",
        padx=32,
        pady=(30, 5)
    )

    subtitulo = ctk.CTkLabel(
        frame_conteudo,
        text="Cadastro de clientes com nome, CPF, telefone, e-mail e endereço.",
        font=("Arial", 14),
        text_color=sub_titulo
    )

    subtitulo.pack(
        anchor="w",
        padx=32
    )

    # ==================================================
    # CABEÇALHO DA TABELA
    # ==================================================

    frame_cabecalho = ctk.CTkFrame(
        frame_conteudo,
        fg_color="transparent"
    )

    frame_cabecalho.pack(
        fill="x",
        padx=32,
        pady=(25, 5)
    )

    ctk.CTkLabel(
        frame_cabecalho,
        text="Nome",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=8,
        sticky="w"
    )

    ctk.CTkLabel(
        frame_cabecalho,
        text="Telefone",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=1,
        padx=10,
        pady=8,
        sticky="w"
    )

    ctk.CTkLabel(
        frame_cabecalho,
        text="Endereço",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=2,
        padx=10,
        pady=8,
        sticky="w"
    )

    ctk.CTkLabel(
        frame_cabecalho,
        text="E-mail",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=3,
        padx=10,
        pady=8,
        sticky="w"
    )

    ctk.CTkLabel(
        frame_cabecalho,
        text="Ações",
        font=("Arial", 13, "bold")
    ).grid(
        row=0,
        column=4,
        padx=10,
        pady=8
    )

    # ==================================================
    # TABELA
    # ==================================================

    tabela = ctk.CTkScrollableFrame(
        frame_conteudo,
        fg_color="transparent"
    )

    tabela.pack(
        fill="both",
        expand=True,
        padx=32,
        pady=5
    )

    componentes_das_linhas_da_tabela = []

    # ==================================================
    # ATUALIZAR TABELA
    # ==================================================

    def atualizar_tabela_visual():

        for componente in componentes_das_linhas_da_tabela:
            componente.destroy()

        componentes_das_linhas_da_tabela.clear()

        clientes = carregar_clientes()

        if not clientes:

            mensagem = ctk.CTkLabel(
                tabela,
                text="Nenhum cliente cadastrado.",
                font=("Arial", 14),
                text_color=sub_titulo
            )

            mensagem.pack(
                pady=30
            )

            componentes_das_linhas_da_tabela.append(
                mensagem
            )

            return

        for cliente in clientes:

            linha = ctk.CTkFrame(
                tabela,
                fg_color=cor_frame,
                border_width=1,
                border_color=borda_frame
            )

            linha.pack(
                fill="x",
                pady=3
            )

            nome = (
                cliente.get("Nome", "")
                + " "
                + cliente.get("Sobrenome", "")
            ).strip()

            telefone = cliente.get(
                "Telefone",
                ""
            )

            endereco = cliente.get(
                "Endereço",
                "Não informado"
            )

            email = cliente.get(
                "Email",
                "Não informado"
            )

            ctk.CTkLabel(
                linha,
                text=nome,
                width=180,
                anchor="w"
            ).grid(
                row=0,
                column=0,
                padx=10,
                pady=8,
                sticky="w"
            )

            ctk.CTkLabel(
                linha,
                text=telefone,
                width=120,
                anchor="w"
            ).grid(
                row=0,
                column=1,
                padx=10,
                pady=8,
                sticky="w"
            )

            ctk.CTkLabel(
                linha,
                text=endereco,
                width=180,
                anchor="w"
            ).grid(
                row=0,
                column=2,
                padx=10,
                pady=8,
                sticky="w"
            )

            ctk.CTkLabel(
                linha,
                text=email,
                width=180,
                anchor="w"
            ).grid(
                row=0,
                column=3,
                padx=10,
                pady=8,
                sticky="w"
            )

            botao_excluir = ctk.CTkButton(
                linha,
                text="Excluir",
                width=70,
                fg_color="#B33A3A",
                hover_color="#8F2D2D",
                command=lambda c=cliente: deletar_cliente(c)
            )

            botao_excluir.grid(
                row=0,
                column=4,
                padx=10,
                pady=8
            )

            componentes_das_linhas_da_tabela.append(
                linha
            )

    # ==================================================
    # EXCLUIR CLIENTE
    # ==================================================

    def deletar_cliente(cliente):

        resposta = messagebox.askyesno(
            "Excluir cliente",
            "Deseja realmente excluir este cliente?"
        )

        if not resposta:
            return

        excluir_cliente(cliente)

        atualizar_tabela_visual()

    # ==================================================
    # NOVO CADASTRO
    # ==================================================

    def novo_cadastro():

        frame_cabecalho.pack_forget()
        tabela.pack_forget()
        botao_novo.pack_forget()

        frame_formulario = ctk.CTkFrame(
            frame_conteudo,
            fg_color=cor_frame
        )

        frame_formulario.pack(
            fill="x",
            padx=32,
            pady=25
        )

        ctk.CTkLabel(
            frame_formulario,
            text="Novo cliente",
            font=("Arial", 20, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            pady=(20, 15),
            sticky="w"
        )

        # Nome

        ctk.CTkLabel(
            frame_formulario,
            text="Nome:"
        ).grid(
            row=1,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        entrada_nome = ctk.CTkEntry(
            frame_formulario,
            width=300
        )

        entrada_nome.grid(
            row=1,
            column=1,
            padx=20,
            pady=8
        )

        # Sobrenome

        ctk.CTkLabel(
            frame_formulario,
            text="Sobrenome:"
        ).grid(
            row=2,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        entrada_sobrenome = ctk.CTkEntry(
            frame_formulario,
            width=300
        )

        entrada_sobrenome.grid(
            row=2,
            column=1,
            padx=20,
            pady=8
        )

        # Telefone

        ctk.CTkLabel(
            frame_formulario,
            text="Telefone:"
        ).grid(
            row=3,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        entrada_telefone = ctk.CTkEntry(
            frame_formulario,
            width=300
        )

        entrada_telefone.grid(
            row=3,
            column=1,
            padx=20,
            pady=8
        )

        # Endereço

        ctk.CTkLabel(
            frame_formulario,
            text="Endereço:"
        ).grid(
            row=4,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        entrada_endereco = ctk.CTkEntry(
            frame_formulario,
            width=300
        )

        entrada_endereco.grid(
            row=4,
            column=1,
            padx=20,
            pady=8
        )

        # E-mail

        ctk.CTkLabel(
            frame_formulario,
            text="E-mail:"
        ).grid(
            row=5,
            column=0,
            padx=20,
            pady=8,
            sticky="w"
        )

        entrada_email = ctk.CTkEntry(
            frame_formulario,
            width=300
        )

        entrada_email.grid(
            row=5,
            column=1,
            padx=20,
            pady=8
        )

        # ==================================================
        # CADASTRAR
        # ==================================================

        def executar_cadastro():

            sucesso, mensagem = cadastrar_cliente(
                entrada_nome.get().strip(),
                entrada_sobrenome.get().strip(),
                entrada_telefone.get().strip(),
                entrada_endereco.get().strip(),
                entrada_email.get().strip()
            )

            if not sucesso:

                messagebox.showwarning(
                    "Atenção",
                    mensagem
                )

                return

            messagebox.showinfo(
                "Sucesso",
                mensagem
            )

            frame_formulario.destroy()

            frame_cabecalho.pack(
                fill="x",
                padx=32,
                pady=(25, 5)
            )

            tabela.pack(
                fill="both",
                expand=True,
                padx=32,
                pady=5
            )

            botao_novo.pack(
                anchor="e",
                padx=32,
                pady=10
            )

            atualizar_tabela_visual()

        # ==================================================
        # CANCELAR
        # ==================================================

        def cancelar():

            frame_formulario.destroy()

            frame_cabecalho.pack(
                fill="x",
                padx=32,
                pady=(25, 5)
            )

            tabela.pack(
                fill="both",
                expand=True,
                padx=32,
                pady=5
            )

            botao_novo.pack(
                anchor="e",
                padx=32,
                pady=10
            )

        # ==================================================
        # BOTÕES
        # ==================================================

        frame_botoes = ctk.CTkFrame(
            frame_formulario,
            fg_color="transparent"
        )

        frame_botoes.grid(
            row=6,
            column=0,
            columnspan=2,
            pady=(15, 20)
        )

        ctk.CTkButton(
            frame_botoes,
            text="Cadastrar",
            command=executar_cadastro,
            fg_color=cor_botao
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            frame_botoes,
            text="Cancelar",
            command=cancelar,
            fg_color="#777777",
            hover_color="#555555"
        ).pack(
            side="left",
            padx=5
        )

    # ==================================================
    # BOTÃO NOVO
    # ==================================================

    botao_novo = ctk.CTkButton(
        frame_conteudo,
        text="Novo",
        command=novo_cadastro,
        fg_color=cor_botao
    )

    botao_novo.pack(
        anchor="e",
        padx=32,
        pady=10
    )

    # ==================================================
    # PRIMEIRA ATUALIZAÇÃO
    # ==================================================

    atualizar_tabela_visual()