import classe_calculadora

numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite o segundo número:'))

calculo1 = classe_calculadora.Calculadora(numero1,numero2)
calculo1.get_valor_soma()
calculo1.get_valor_divisao()


