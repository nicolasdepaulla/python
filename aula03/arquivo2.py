nome_arquivo = input("digite o nome do arquivo: ")
extensao_arquivo = input("digite a entensão do arquivo: ")
conteudo = input("digite o conteúdo do arquivo: ")

arq = open(nome_arquivo+"."+extensao_arquivo,"a")
arq.write(conteudo)
arq.close()