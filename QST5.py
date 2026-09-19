n1 = int(input("Digite seu primeiro valor inteiro: "))
n2 = int(input("Digite seu segundo valor inteiro: "))
n3 = int(input("Digite seu terceiro valor inteiro: "))

if n1 > n2:
    n1,n2 = n2,n1

if n1 > n3:
    n1,n3 = n3, n1

if n2 > n3:
    n2, n3 = n3, n2

print(f"A ordem crescente dos numéros é {n1}, {n2}, {n3}")

    
    

