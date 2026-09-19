raio=float(input("Digite o valor do raio:" ))

area_da_circunferencia = 3.14159 * (raio**2)

if raio<0:
    print("O raio não pode ser numero negativo")
else:
    print(f"A area da circunferencia é {area_da_circunferencia:.2f}")
