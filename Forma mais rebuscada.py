preço=float(input("Digite o Valor do Produto: "))
Desconto=float(input("Digite o Valor do Desconto"))

Desconto= preço*Desconto/100

Preço_Final=preço - Desconto

print("O valor do desconto recebido, foi {}".format(round(Preço_Final, 1)))

if Preço_Final == Preço_Final:
    print("Valor do Desconto Está correto")
else:
    print("O Valor do Desconto Está errado")
