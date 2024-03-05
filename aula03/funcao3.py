def criaArquivo(nome="",ext="",cont="")->str:
    """A função cria arquivo, recebe o nome do arquivo,
    a extensão e por fim algo para inserir no arquivo,
    e cria este arquivo no diretório local"""
    f = open(nome+"."+ext,"a")
    f.write(cont)
    f.close()
    return "Arquivo criado com sucesso"

print(criaArquivo("porta","csv","texto;mensagem;ola"))