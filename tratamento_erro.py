
def divisao():
    try:
        a = float(input("Digita 1º numero: "))
        b = float(input("Digita 2º numero: "))
        print(a/b)
    except ValueError as ex:
        print("Por favor digite apenas números")
    except ZeroDivisionError as ex:
        print("Não é possivel dividir um zero")
    except Exception as ex:
        print("Ocorreu um erro.")
        print(ex)

divisao()