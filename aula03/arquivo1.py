# open é uma função que permite abrir um arquivo
# ler ou escrever neste arquivo
arq = open("dados.txt","a")
# a função write, permite escrever em um arquivo
arq.write("olá\n")
# a função close fecha o arquivo retirando-o da memória
arq.close()
