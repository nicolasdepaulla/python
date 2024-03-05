print("este programa analisa os valores digitado de 0 a 6 e diz o dia da semana")
digito = input("entre com um número de 0 a 6")


match digito:
    case '0':
      print("domingo")
    case '1':
     print("segunda-feira")
    case '2':
      print("terça")
    case '3':
     print("quarta")
    case '4':
      print("quinta")
    case '5':
     print("sexta")
    case '6':
      print("sabádo")
    case _:
      print("valor incorreto. Tente outra vez")
    