def incrementar_meu_numero(numero):
    numero = numero + 1
    return numero

numero_incrementado = incrementar_meu_numero(int(input('Digite um número:')))

# numero = int(input('Digite um numero:'))
# incrementar_meu_numero(numero)
print('Número fora da funcao:', numero_incrementado)