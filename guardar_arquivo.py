try:
    # w - abrir o arquivo e prepara para escrever,
    #     se o arquivo não existir, ele será criado
    # r - abrir o arquivo e prepara somente para leitura
    # a - abrir o arquivo e prepara para escrever na última linha
    # b - abrir o arquivo em formato binário

    arquivo = open("nomes.txt","a")
    arquivo.write("Elsa Antonio\n")
    
except:
    print("Ocorreu um erro ao tentar abrir arquivo")