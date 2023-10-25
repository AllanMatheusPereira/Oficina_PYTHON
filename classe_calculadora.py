class Calculadora:
    def __init__(self,numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def get_valor_soma(self):
        print(f'Soma = ', self.numero1+self.numero2)
    
    def get_valor_subtracao(self):
        print(f'Subitração = ', self.numero1-self.numero2)

    def get_valor_multiplicacao (self):
        print(f'Multiplicação = ', self.numero1*self.numero2 )

    def get_valor_divisao (self):
        print(f'Divisão = ', self.numero1/self.numero2)

