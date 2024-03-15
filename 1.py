# 1 - Desenvolva um programa para ler a quantidade de pessoas de um grupo. Para cada integrante informe 
#     o peso. O algoritmo deve exibir a média dos pesos e quantos estão acima de 80kg. 

soma_dos_pesos = 0
pessoa_acima_80 = 0

quantidade_de_pessoas_do_grupo = int(input("Digite a quantidade de pessoass do grupo: "))

for  i in range(quantidade_de_pessoas_do_grupo) :
    peso = float(input(f"Digite o peso da {i + 1}ª pessoa: "))
    while peso < 0 :
        print("Peso inválido")
        peso = float(input(f"Digite novamente o peso da {i + 1}ª pessoa: "))
    
    soma_dos_pesos += peso
    if peso > 80 :
        pessoa_acima_80 += 1

media_dos_pesos = soma_dos_pesos / quantidade_de_pessoas_do_grupo

print(F"Média dos pesos: {media_dos_pesos} kg")
print(f"Quantidade de pessoas acima de 80 kg: {pessoa_acima_80}")
    
    