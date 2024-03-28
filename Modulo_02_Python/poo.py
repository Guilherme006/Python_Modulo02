# POO

# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos!"


# Objetos
pessoa_01 = Pessoa("Guilherme", 25)
mensagem = pessoa_01.saudacao()
print(mensagem)

pessoa_02 = Pessoa(nome='João', idade=30)
mensagem = pessoa_02.saudacao()
print(mensagem)
