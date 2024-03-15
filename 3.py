# 3 - Faça um algoritmo que receba idades de 6 pessoas. Por fim, o algoritmo deve informar:
# a ) Quantas idades foram lidas;
# b ) Maior idade;
# c ) Menor idade;
# d ) Média das idades.

menor_idade = 0
maior_idade = 0
soma_das_idades = 0

for i in range (6) :
    idade = int(input(f"Dgigite a idade da {i + 1}ª pessoa: "))
    while idade < 0 :
        print("idade inválida")
        idade = int(input(f"Digite novamente a idade da {i + 1}ª pessoa:"))

    soma_das_idades += idade

    if i == 0 :
        menor_idade = idade
    else :
        if menor_idade > idade :
            menor_idade = idade
    
    if maior_idade < idade :
        maior_idade = idade

media_idades = soma_das_idades / 6

print()
print("Foram lidas 6 idades")
print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
print(f"Média das idades: {media_idades}")