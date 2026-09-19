ano_atual = int(input("Digite o ano atual que você está: "))
idade = int(input("Digite sua idade atual: "))

ano_nascimento = ano_atual - idade 

if idade<=0 or ano_atual<=0 :
    print("não foi possivel calcular o ano do seu nascimento")
else:
    print(f"Seu ano de nascimento é {ano_nascimento}")
