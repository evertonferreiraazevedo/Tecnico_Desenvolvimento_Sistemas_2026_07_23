class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.notasReputacao = []
    
    def __str__(self):
        return f"O Livro {self.titulo} foi escrito por {self.autor}"
    
    def reputacao(self, nota):
        self.notasReputacao.append(nota)
        mediaReputacao = sum(self.notasReputacao) / len(self.notasReputacao)
        if mediaReputacao >= 4.5:
            return f"Excelente (Altamente Recomendado) - {mediaReputacao:.2f}"
        elif mediaReputacao >= 3.5:
            return f"Boa (Recomendado) - {mediaReputacao:.2f}"
        else:
            return f"Regular  - {mediaReputacao:.2f}"
        
livro = Livro("A morte de Ivan Ilitch", "Liev Tolstói")
print (livro)

print(livro.reputacao(3))
print(livro.reputacao(2))
print(livro.reputacao(4))
print(livro.reputacao(5))

    