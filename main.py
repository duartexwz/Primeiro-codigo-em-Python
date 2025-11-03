#//Criar um prgorama que receba uma informação, pergunte qual data você quer armazenar ela e mostre essa informação na tela quando você pedir//

#Pedir informação

info1 = input("Digite aqui a informação ou anotação que deseja guardar:   ") #Informação digitada pelo usuario

armazenadas = []
armazenadas.append({"texto": info1, "tipo": None, "data": None})

print("\nEssa mensagem é uma:")
print("1. Anotação.")               #Escolha de tipo de informação
print("2. Programação. ")

escolha = input("\nEscolha uma das opções acima ↑:") .strip() #Definindo o tipo de mensagem

if escolha  == "1":
    armazenadas[-1]["texto"] = "Anotação"
elif escolha  == "2":
    armazenadas[-1]["data"] = "Programação"
data = input("Para qual dia deseja fazer essa programação?: ")

while True:
    nova = input("\nDeseja guardar mais alguma informação (sim/nao)?: ").lower()

    if nova == "sim":
        print("\nEssa mensagem é uma:")
        print("1. Anotação.")
        print("2. Programação. ")

        escolha = input("\nEscolha uma das opções acima ↑: ")

        if escolha  == "1":
            armazenadas[-1]["tipo"] = "Anotação"

            data = input("Para qual dia deseja fazer essa programação?: ")

        
        elif escolha  == "2":
            armazenadas[-1]["data"] = data

     

    elif nova == "nao":
        encerrar = input("\nPosso encerrar o programa?") #Senao, encerrar o programa

        if encerrar == "sim":
            print("\nEncerrando...")
            break
        elif encerrar == "nao":
            print("\nReinicie o programa e armazene suas informações novamente.")

    

#mostrar a informação na tela de acordo com o que o usuario pedir 
ver_info = input("\nDeseja ver alguma das informações que você guardou?").strip() .lower()

if ver_info in["sim", "s"]:
    print("\n======INFORMAÇÕES GUARDADAS======\n")
    
    
    for i, item in enumerate(armazenadas, start=-1):
        print(f"{i}. {item['tipo']}: {item['texto']}")
        if item['data']:
            print(f"   📅Data: {item['data']}")
        
        print("-" * 40)        

        print("\nFim das nformações salvas.")
else:
    print("\nPrograma encerrado. Ate a proxima!")

