from asyncio.windows_events import NULL
from http.client import SWITCHING_PROTOCOLS


AGENDA = {}
"""
# Estrutura dos dados
AGENDA["Ayrton"] = {
    "Telefone": "994578453",
    "Email":"ayrton@gmail.com",
    "Endereco":"Fubu"
}
AGENDA["Elsa"] = {
    "Telefone": "911578405",
    "Email":"elsa@gmail.com",
    "Endereco":"Fubu"
}
"""
def Mostrar_contactos():
    if AGENDA:
        for contacto in AGENDA:
            print("{nome:*^30}".format(nome=contacto))        
            Buscar_contacto(contacto)
              
            print("\n")
    else:
        print(">>>>> Agenda está vazia\n")

def Buscar_contacto(contacto):
    try:
        print("Nome:", contacto)
        print("Telefone:", AGENDA[contacto]["Telefone"])
        print("E-mail:", AGENDA[contacto]["Email"])
        print("Endereço:", AGENDA[contacto]["Endereco"])
    except KeyError:
        print("Contacto não existe!")
    except Exception as ex:
        print("Ocorreu um erro desconhecido!")
        print(ex)

def Inserir_Editar_contacto(nome,telefone,email,endereco):
    AGENDA[nome] = {
        "Telefone": telefone,
        "Email":email,
        "Endereco":endereco
    }
    Guardar()
    print("»»»» Contacto '{}' adicionado/editado com sucesso".format(nome))

def Excluir_contacto(contacto):
    try:
        AGENDA.pop(contacto)
        Guardar()
        print()
        print("»»»» Contacto '{}' excluído com sucesso".format(contacto))
    except KeyError:
        print("Contacto não existe!")
    except Exception as ex:
        print("Ocorreu um erro desconhecido!")
        print(ex)

def Imprimir_menu():
    print("==================================")
    print("===           MENU             ===")
    print("==================================")
    print("1 - Listar contactos")
    print("2 - buscar contacto")
    print("3 - Adicionar contacto")
    print("4 - Editar contacto")
    print("5 - Excluir contacto")
    print("6 - Exportar arquivo CSV")
    print("7 - Importar arquivo CSV")
    print("0 - Fechar agenda")
""""""
def Exportar_contactos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo,"w") as arquivo:
            
            for contacto in AGENDA:
                Telefone = AGENDA[contacto]["Telefone"]
                Email = AGENDA[contacto]["Email"]
                Endereco = AGENDA[contacto]["Endereco"]
                arquivo.write(f"{contacto},{Telefone},{Email},{Endereco}\n")
        print(">>>> Exportados com sucesso!")
    except:
        print(">>>> Ocurreu um erro ao tentar exportar.")

def Importar_contactos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo,"r") as arquivo:
            for linha in arquivo:
                detalhes_contacto = linha.strip().split(',')
                nome = detalhes_contacto[0]
                telefone = detalhes_contacto[1]
                email = detalhes_contacto[2]
                endereco = detalhes_contacto[3]
                Inserir_Editar_contacto(nome,telefone,email,endereco)
            print(">>>> Contactos importados com sucesso!")
    except FileNotFoundError:
        print(f"Arquivo {nome_do_arquivo} não foi encontrado!")
        print("Ocorreu um erro")

def Ler_detalhes_contacto():
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    return telefone, email, endereco

def Guardar():
    Exportar_contactos("database.csv")

def Carregar():
    try:
        with open("database.csv","r") as arquivo:
            for linha in arquivo:
                detalhes_contacto = linha.strip().split(',')
                nome = detalhes_contacto[0]
                telefone = detalhes_contacto[1]
                email = detalhes_contacto[2]
                endereco = detalhes_contacto[3]
                
                AGENDA[nome] = {
                    "Telefone": telefone,
                    "Email":email,
                    "Endereco":endereco
                }
                
        print(">>>> Database carregada com sucesso!")
    except FileNotFoundError:
        print(f"Database está sem registos")
    except Exception as ex:
        print("Ocorreu um erro")
        print(ex)

#Excluir_contacto("Ayrton")
#Mostrar_contactos()
#INICIO DA AGENDA
Carregar()

while True:
    Imprimir_menu()
    opcao = input("Escolha uma das opçoes: ")
    print("Opção escolhida", opcao)

    if opcao == "1": #Listar contactos
        Mostrar_contactos()
    elif opcao == "2":    #Buscar contacto
        contato = input("Digita o nome: ")
        Buscar_contacto(contato)
    elif opcao == "3":    #Adicionar contacto
        try:
            nome = input("Nome: ")
            AGENDA[nome]
            print(">>>> Já existe um contacto com esse nome")
        except KeyError:  
            telefone, email, endereco = Ler_detalhes_contacto()          
            Inserir_Editar_contacto(nome,telefone, email, endereco)
    elif opcao == "4":    #Editar contacto
        try:
            nome = input("Nome: ")
            AGENDA[nome] #Verificar se o contacto já existe
            telefone, email, endereco = Ler_detalhes_contacto()          
            Inserir_Editar_contacto(nome,telefone, email, endereco)
        except KeyError:
            print(">>>> Não existe nenhum contacto com esse nome.")
    elif opcao == "5":    #Excluir contacto
        nome = input("Nome:")
        Excluir_contacto(nome)
    elif opcao == "6":    #Exportar arquivo
        nome_do_arquivo = input("Digita o nome do arquivo: ")
        Exportar_contactos(nome_do_arquivo)
    elif opcao == "7":    #Exportar arquivo
        nome_do_arquivo = input("Digita o nome do arquivo: ")
        Importar_contactos(nome_do_arquivo)
    elif opcao == "0":    #Sair
        print("Fechando o programa...")
        break
    else:
        print("Opção inválida")


