n1 = input("Digite a primeira nota do aluno: ")
n2 = input("Digite a segunda nota do aluno: ")
n3 = input("Digite a terceira nota do aluno: ")
n4 = input("Digite a quarta nota do aluno: ")
rs = ( int(n1)+int(n2)+int(n3)+int(n4) ) /4
# Se o aluno tiver uma media acima ou igual a 7,
#então estara APROVADO, Senão se a média
# for abaixo ou igual a 4, então estará REPROVADO
# caso contrario, estará em RECUPERAÇÃO
print("A sua média é "+str(rs)+", então você está: ")
 
if( rs >= 7 ):
    print("Aprovado")
elif( rs <= 4 ):
    print("Reprovado")
else:
    print("Recupração")        