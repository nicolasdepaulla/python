# criar uma função que escreve a tabuada para um
# determinado valor definido pelo usuário em 
# um arquivo de texto
def montar_tabuada(numero=0):
    print("O programa pede um número para fazer a tabuada")
    arq = open("tabuada.txt","a")
    for i in range(1,11):
        arq.write(str(numero) + " x " + str(i) + " = " + str(numero*i)+"\n")
    arq.close()

n = input("digite um número: ")
montar_tabuada(int(n))
        