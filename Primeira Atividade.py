nome=input("Digite seu nome:")
idade=int(input("Digite Sua Idade:"))
altura=float(input("DIgite sua ALtura:"))
peso=float(input("Digite Seu Peso:"))
nota_1=float(input("Digite Sua Nota:"))
nota_2=float(input("Digite sua Nota:"))
faltas=int(input("digite suas Faltas:"))

media_final=(nota_1 + nota_2) / 2
print("A media final do aluno(a), {} é {}".format(nome, media_final))

imc=peso/(altura * altura)
print("O imc do Aluno(a), {} é {}".format(nome, round(imc, 1)))
        
soma=(nota_1 + nota_2)
print("O somatorio do aluno(a), {} é {}".format(nome, soma))

idade+5
print("A idade do aluno(a) daqui a 5 anos  {} terá {}".format(nome,idade+5))

if media_final >= 7.0:
 print ("O aluno(a), {} está aprovada".format(nome))

else:
 print ("O aluno(a) {} está reprovado".format(nome))
 
if faltas >= 10:
  print ("O aluno(a) {} tem mais de 10 faltas".format(nome))
  
else:
  print ("O aluno(a) {} não tem mais de 10 faltas".format(nome))
