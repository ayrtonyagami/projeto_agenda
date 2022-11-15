list_de_cores = ["Azul","Verde","Branco","Castanho","Preto"]


print(list_de_cores)

print("++++++++++++ Listar item com o for ++++++++++")
for cor in list_de_cores:
    print(cor)

print("++++++++++++ Primeiro ++++++++++")
print(list_de_cores[0]) #pegar o primeiro item


print("++++++++++++ Ultimo ++++++++++")
print(list_de_cores[-1]) #pegar o último item

print("++++++++++++ Listar o 1º e 2º item ++++++++++")
print(list_de_cores[0:2])


print("++++++++++++ Listar intervalo de item ++++++++++")
print(list_de_cores[1:3])

print("++++++++++++ Listar do 2º até o ultimo ++++++++++")
print(list_de_cores[1:])