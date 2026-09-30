import customtkinter as ctk
from tkinter import messagebox

from controllers.aluno_controller import (
    cadastrar_aluno,
    listar_alunos
)

def tela_alunos(container):

    titulo = ctk.CTkLabel(container, text="Cadastro de Alunos", font=("Arial", 28, "bold"))
    titulo.pack(anchor="w", padx=30, pady=(30, 20))
    # FORMULÁRIO

    frame_form = ctk.CTkFrame(container)
    frame_form.pack(padx=30, fill="x")
    
    ctk.CTkLabel(frame_form, text="Nome").pack(anchor="w", padx=20, pady=(20, 5))
    
    entrada_nome = ctk.CTkEntry(frame_form, placeholder_text="Digite o nome")
    entrada_nome.pack(padx=20, fill="x")
    
    ctk.CTkLabel(frame_form, text="Idade").pack(anchor="w", padx=20, pady=(15, 5))
    
    entrada_idade = ctk.CTkEntry(frame_form, placeholder_text="Digite a idade")
    entrada_idade.pack(padx=20, fill="x")
    
    ctk.CTkLabel(frame_form, text="Curso").pack(anchor="w", padx=20, pady=(15, 5))
    
    entrada_curso = ctk.CTkEntry(frame_form, placeholder_text="Digite o curso")
    entrada_curso.pack(padx=20, fill="x")

    # TABELA
    frame_lista = ctk.CTkFrame(container)
    frame_lista.pack(padx=30, pady=20, fill="both", expand=True)
    titulo_lista = ctk.CTkLabel(frame_lista, text="Alunos cadastrados", font=("Arial", 18, "bold"))
    titulo_lista.pack(anchor="w", padx=20, pady=15)
    lista = ctk.CTkTextbox(frame_lista)
    lista.pack(padx=20, pady=(0, 20), fill="both", expand=True)


    def atualizar_lista():
        lista.delete("1.0", "end")
        alunos = listar_alunos()
        if not alunos:
            lista.insert("end", "Nenhum aluno cadastrado.")
            return

        for aluno in alunos:
            texto = (
                f"Nome: {aluno['Nome']}\n"
                f"Idade: {aluno['Idade']}\n"
                f"Curso: {aluno['Curso']}\n"
                f"{'-' * 40}\n"
            )
            lista.insert("end", texto)

    def cadastrar():
        nome = entrada_nome.get().strip()
        idade = entrada_idade.get().strip()
        curso = entrada_curso.get().strip()
        sucesso, mensagem = cadastrar_aluno(nome, idade, curso)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            entrada_nome.delete(0, "end")
            entrada_idade.delete(0, "end")
            entrada_curso.delete(0, "end")
            atualizar_lista()
        else:
            messagebox.showerror("Erro", mensagem)
            
            
    botao_cadastrar = ctk.CTkButton(frame_form,text="Cadastrar",command=cadastrar )
    botao_cadastrar.pack(padx=20, pady=20)
    atualizar_lista()