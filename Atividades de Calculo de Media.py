nota_1=float(input("Digite Sua Nota:"))
nota_2=float(input("DIgite Sua Nota:"))
nota_3=float(input("Digite Sua Nota:"))

media_final= (nota_1 + nota_2 + nota_3)/3

print("Olá Estudante Sua Nota é {}".format(round(media_final, 1)))

if media_final >=7.0:
    print("O aluno Está Aprovado")
else:
    print("Aluno Está Reprovado")
    
