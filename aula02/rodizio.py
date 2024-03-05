#se o final da placa for 1,2 você não pode rodar na segunda
# se o final da placa for 3,4 você não pode rodar na terça
#se o final da placa for 5,6 você não pode rodar na quarta
#se o final da placa for 7,8 você não pode rodar na quinta
#se o final da placa for 9 você não pode rodar na sexta

print("digite um número de 1 a 9 e diz se o carro pode rodar ou não")
digito = input("entre com um número de 1 a 9\n")

match digito:
    case '1' | '2':
      print("você não pode rodar na segunda\n")
    case '3' | '4':
     print("você não pode rodar na terça\n")
    case '5' | '6':
      print("você não pode rodar na quarta\n")
    case '7' | '8':
     print("você não pode rodar na quinta\n")
    case '9':
      print("você não pode rodar na sexta\n")
    case _:
      print("valor incorreto. Tente outra vez\n")