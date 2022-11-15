
try:
    arquivo = open("emails.txt")

    print(arquivo.readlines())
    print(arquivo.read())
except FileNotFoundError:
    print("O arquivo não existe ou o nome está errado.")
except Exception as ex:
    print("Ocorreu um erro ao tentar abrir o arquivo:", ex )
finally:
    print("Finalizando programa..")
