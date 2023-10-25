class Cachorro:
    def __init__(self,raca,idade):
        self.raca = raca
        self.idade = idade
    
    def get_apresentacao_cachorro(self):
        print(f'Raça: {self.raca}, idade: {self.idade}')

cachorro1 = Cachorro('Pincher', 5)
cachorro1.get_apresentacao_cachorro()


