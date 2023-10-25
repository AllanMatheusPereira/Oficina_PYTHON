class Pessoa:
    def set_nome (self,nome):
        self.nome = nome


    def set_sobrenome(self,sobrenome):   
        self.sobrenome = sobrenome


pessoa1 = Pessoa()
pessoa1.set_nome('Allan')
pessoa1.set_sobrenome('Pereira')

print(pessoa1.nome)
print(pessoa1.sobrenome)