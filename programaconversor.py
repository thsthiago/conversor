import sys
import os
import conversor

# FUNÇÃO DIGITA
def digita(c):
    print("--------------------------------")
    print("-------------Opções-------------")
    print("--------------------------------")
    print("[5] Voltar para o menu principal")
    print("[6] Converter novamente")
    print("[7] Sair do programa")
    print("--------------------------------")
    print(" ")

    d = input("Digite a opção desejada: ")
    print("-------------------------------")

    if d == '5':
        os.system('cls')
        return menu()

# Executa a função novamente
    elif d == '6':
        if c == '1':
            os.system('cls')
            print("-------------------------------")
            print("---------Pés em Metros---------")
            print("-------------------------------")
            numero = float(input("DIgite os Pés: "))
            print(conversor.pe2metro(numero))
            c == '1'
            return digita(c)
        
        elif c == '2':
            os.system('cls')
            print("-------------------------------")
            print("----Polegada em Centímetros----")
            print("-------------------------------")
            numero = float(input("Digite as Polegadas: "))
            print(conversor.pol2cent(numero))
            c = '2'
            return digita(c)

        elif c == '3':
            os.system('cls')
            print("-------------------------------")
            print("-------Jardas em Metros--------")
            print("-------------------------------")
            numero = float(input("Digite as Jardas: "))
            print(conversor.jarda2metro(numero))
            c = '3'    
            return digita(c)


        elif c == '4':
            os.system('cls')
            print("-------------------------------")
            print("-----Milhas em Quilômetros-----")
            print("-------------------------------")
            numero = float(input("Digite as Milhas: "))
            print(conversor.milhas2km(numero))
            c = '4'
            return digita(c)

# Fecha o programa 
    elif d == '7':
        sys.exit()
    
# Executado quando a função não existe
    else:
        os.system('cls')
        print(" ")
        print("-------------------------------")
        print("Essa opção não existe, digite novamente")
        return digita(c)

os.system('cls')

# FUNÇÃO MENU
def menu():
    
    print("-------------------------------")
    print("------------Conversor----------")
    print("-------------------------------")
    print(" ")
    print("--------------Menu-------------")
    print(" ")
    print("[1] Para Pés em Metro")
    print("[2] Para Polegada em Centímetro")
    print("[3] Para Jarda em Metro")
    print("[4] Para Milhas em Quilômetro")
    print("[5] Para sair")
    print(" ")


    c = input("DIgite a opção desejada: ")
    print(" ")
    print("-------------------------------")

# Pés em Metros 
    if c == '1':
        os.system('cls')
        print("-------------------------------")
        print("---------Pés em Metros---------")
        print("-------------------------------")
        numero = float(input("DIgite o Pés: "))
        print(conversor.pe2metro(numero))
        c = '1'
        return digita(c)

# Polegadas em Centímetros 
    elif c == '2':
        os.system('cls')
        print("-------------------------------")
        print("----Polegada em Centímetros----")
        print("-------------------------------")
        numero = float(input("Digite as Polegadas: "))
        print(conversor.pol2cent(numero))
        c = '2'
        return digita(c)

# Jardas em Metros 
    elif c == '3':
        os.system('cls')
        print("-------------------------------")
        print("-------Jardas em Metros--------")
        print("-------------------------------")
        numero = float(input("DIgite as Jardas: "))
        print(conversor.jarda2metro(numero))
        c = '3'    
        return digita(c)

# Milhas em Quilômetro 
    elif c == '4':
        os.system('cls')
        print("-------------------------------")
        print("-----Milhas em Quilômetros-----")
        print("-------------------------------")
        numero = float(input("Digite as Milhas: "))
        print(conversor.milhas2km(numero))
        c = '4'
        return digita(c)

# Fecha o programa 
    elif c == '5':
        sys.exit()
        
# Executado quando a opção não existe    
    else:
        os.system('cls')
        print("Essa opção não existe, digite novamente") 
        return menu()    
        
        
    menu()
menu()