# pede um número e verifica se é par ou impar
numero = input("digite um número: ")
# é necessário realizar a conversão de texto para
# número,pois a função input sempre retorna o valor
# em formato texto. então,utilizamos a função 
# int para converter a variável numero em valor
# númericos inteiro e assim realizar os cálculos
# necessários
numero = int(numero)


if(numero % 2 == 0):
    print("o número digitado é par")
else:
        print("O número digitado é impar")