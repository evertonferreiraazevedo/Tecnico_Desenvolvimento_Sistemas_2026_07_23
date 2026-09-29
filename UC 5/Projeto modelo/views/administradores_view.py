import customtkinter as ctk


def tela_administradores(container):

    # ==================================================
    # TÍTULO
    # ==================================================

    titulo = ctk.CTkLabel(
        container,
        text="Administradores",
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
        text="Cadastro de administradores com nome, telefone e e-mail.",
        font=("Arial", 14),
        text_color="#52677F"
    )

    subtitulo.pack(
        anchor="w",
        padx=32
    )

    # ==================================================
    # CABEÇALHO
    # ==================================================

    cabecalho = ctk.CTkFrame(
        container,
        fg_color="transparent"
    )

    cabecalho.pack(
        fill="x",
        padx=32,
        pady=(25, 5)
    )

    colunas = [
        "Nome",
        "Telefone",
        "E-mail",
        "Endereço",
        "Ações"
    ]

    for coluna, texto in enumerate(colunas):

        ctk.CTkLabel(
            cabecalho,
            text=texto,
            font=("Arial", 13, "bold")
        ).grid(
            row=0,
            column=coluna,
            padx=10,
            pady=8,
            sticky="w"
        )

    # ==================================================
    # ÁREA DA TABELA
    # ==================================================

    tabela = ctk.CTkScrollableFrame(
        container,
        fg_color="transparent"
    )

    tabela.pack(
        fill="both",
        expand=True,
        padx=32,
        pady=5
    )

    linhas = []

    # ==================================================
    # FUNÇÃO PARA CORTAR TEXTO
    # ==================================================

    def cortar_texto(texto, tamanho):

        if len(texto) > tamanho:
            return texto[:tamanho] + "..."

        return texto

    # ==================================================
    # ADICIONAR ADMINISTRADOR
    # ==================================================

    def adicionar_administrador(administrador):

        linha = ctk.CTkFrame(
            tabela,
            fg_color="white",
            border_width=1,
            border_color="#E0E0E0"
        )

        linha.pack(
            fill="x",
            pady=3
        )

        nome = administrador.get(
            "Nome",
            ""
        )

        telefone = administrador.get(
            "Telefone",
            ""
        )

        email = administrador.get(
            "Email",
            ""
        )

        endereco = administrador.get(
            "Endereço",
            ""
        )

        ctk.CTkLabel(
            linha,
            text=cortar_texto(nome, 20),
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
            text=cortar_texto(telefone, 15),
            width=130,
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
            text=cortar_texto(email, 25),
            width=200,
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
            text=cortar_texto(endereco, 25),
            width=200,
            anchor="w"
        ).grid(
            row=0,
            column=3,
            padx=10,
            pady=8,
            sticky="w"
        )

        ctk.CTkButton(
            linha,
            text="Excluir",
            width=70
        ).grid(
            row=0,
            column=4,
            padx=10,
            pady=8
        )

        linhas.append(linha)

    # ==================================================
    # NOVO CADASTRO
    # ==================================================

    def novo_cadastro():

        cabecalho.pack_forget()
        tabela.pack_forget()
        botao_novo.pack_forget()

        formulario = ctk.CTkFrame(
            container,
            fg_color="white"
        )

        formulario.pack(
            fill="x",
            padx=32,
            pady=25
        )

        ctk.CTkLabel(
            formulario,
            text="Novo administrador",
            font=("Arial", 20, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            pady=(20, 15),
            sticky="w"
        )

        campos = [
            ("Nome:", "Nome"),
            ("Telefone:", "Telefone"),
            ("E-mail:", "Email"),
            ("Endereço:", "Endereço")
        ]

        entradas = {}

        for linha, (texto, chave) in enumerate(campos, start=1):

            ctk.CTkLabel(
                formulario,
                text=texto
            ).grid(
                row=linha,
                column=0,
                padx=20,
                pady=8,
                sticky="w"
            )

            entrada = ctk.CTkEntry(
                formulario,
                width=300
            )

            entrada.grid(
                row=linha,
                column=1,
                padx=20,
                pady=8
            )

            entradas[chave] = entrada

        # ==================================================
        # BOTÕES
        # ==================================================

        botoes = ctk.CTkFrame(
            formulario,
            fg_color="transparent"
        )

        botoes.grid(
            row=len(campos) + 1,
            column=0,
            columnspan=2,
            pady=(15, 20)
        )

        def cancelar_cadastro():

            formulario.destroy()

            cabecalho.pack(
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

        def cadastrar():

            # Por enquanto mantém o comportamento
            # original: fecha o formulário.

            formulario.destroy()

            cabecalho.pack(
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

        ctk.CTkButton(
            botoes,
            text="Cadastrar",
            command=cadastrar,
            fg_color="#262753"
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botoes,
            text="Cancelar",
            command=cancelar_cadastro,
            fg_color="#777777"
        ).pack(
            side="left",
            padx=5
        )

    # ==================================================
    # BOTÃO NOVO
    # ==================================================

    botao_novo = ctk.CTkButton(
        container,
        text="Novo",
        command=novo_cadastro,
        fg_color="#262753"
    )

    botao_novo.pack(
        anchor="e",
        padx=32,
        pady=10
    )