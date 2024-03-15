# 2 - A funerária Sua Hora Chegou possui vários caixões. O algoritmo deverá cadastrar o código dos caixões 
#     até o usuário digitar -1 (quando digitar -1 ele encerra) e sair do cadastro. Por fim, o algoritmo 
#     mostrará o número de caixões cadastrados. Utilize o WHILE. 

codigo_caixao = 0
quantidade_de_caixoes_cadastrados = 0

print("-1 Finalizar")
print()

while codigo_caixao != -1 :
    codigo_caixao = int(input("Digite o código do caixão: "))

    if codigo_caixao == -1:
        print()
        print("Finalizando...")
        break
    else :
        quantidade_de_caixoes_cadastrados += 1

print(f"Quantidade de caixões cadastrados: {quantidade_de_caixoes_cadastrados}")