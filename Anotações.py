
#Codigo ainda em construção, este é um modelo base ainda.

#//Criar um prgorama que receba uma informação, pergunte qual data você quer armazenar ela e mostre essa informação na tela quando você pedir//

#Pedir informação

info1 = input("Digite aqui a informação ou anotação que deseja guardar:   ").lower() #Informação digitada pelo usuario

print("\nEssa mensagem é uma:")
print("1. Anotação.")               #Escolha de tipo de informação
print("2. Programação. ")

escolha = input("\nEscolha uma das opções acima ↑:") #Definindo o tipo de mensagem

if escolha  == "1":# Confirmando a anotação
    print("\nAnotação feita com sucesso!")

elif escolha  == "2":
    data1 = input("\nPara qual dia deseja fazer essa programação?: ") #Definindo a data caso a escolha for Programação
    print("\nProgramação feita na data informada com sucesso! ")

elif escolha != "1" and escolha != "2":
    print("\nErro, digite 1 ou 2 !") #Se a escolha for diferente de 1 ou 2 o programa encerra
    exit()

info2 = input("\nDeseja guardar mais alguma informação? (sim/nao)").lower() #Pedindo mais alguma informação


if info2 == "sim":  #Se o usuario desejar anotar, executar o codigo abaixo
    info_2 = input("\nQual informação seria?: ").lower()
    print("\nEssa mensagem é uma:")
    print("1. Anotação.")
    print("2. Programação. ")

    escolha = input("\nEscolha uma das opções acima ↑: ")

    if escolha  == "1":
        print("\nAnotação feita com sucesso!")

    elif escolha  == "2":
        data2 = input("\nPara qual dia deseja fazer essa programação?: ")
        print("\nProgramação feita na data informada com sucesso!")

elif info2 == "nao":
        encerrar = input("\nPosso encerrar o programa?") #Senao, encerrar o programa

        if encerrar == "sim":
            print("\nEncerrando...")
            exit()

        elif encerrar == "nao":
            print("\nReinicie o programa e armazene suas informações novamente.")

    

#mostrar a informação na tela de acordo com o que o usuario pedir 
informacao = input("\nDeseja ver alguma das informações que você guardou?(sim/nao)  ").lower()

if informacao == "sim":#Se o usuario desejar ver a mensagem guardada, executar o codigo abaixo:
    print("\n1. Informação 1")
    print("2. Informação 2")
    print("3. Todas as Informações guardadas.")
   
    
    mostrar_info = input("\nQual informação deseja ver ↑?")


if mostrar_info == "1":
        print(f"  {info1}")
        if 'data1' in locals():
             print(f" Programada para {data1}")

elif mostrar_info == "2":
        print(f"  {info_2}")
        if 'data2' in locals():
             print(f" Programada para {data2}")

                                                    #O codigo mostra a informação que o usuario digitou, e se caso for uma programação, mostra a data que ela foi programada pelo usuario 

elif mostrar_info == "3":
    print(f" \n{info1}")
    if 'data1' in locals():
             print(f" Programada para {data1}")

    print(f" \n{info_2}")
    if 'data2' in locals():
             print(f" Programada para {data2}")




elif informacao == "nao": #Senao, encerrar o programa.
    print("Encerrando o programa...")
    


