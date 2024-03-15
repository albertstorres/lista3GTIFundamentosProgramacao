# 5 - Uma empresa irá realizar uma queima de estoque com os produtos que tiveram poucas unidades 
#     disponíveis. Os descontos aplicados seguem aos seguintes critérios:
# 40% de desconto - até 2 unidades;
# 30% de desconto - entre 3 e 5 unidades;
# 20% de desconto - entre 6 e 9 unidades;
# 10% de desconto - 10 unidades ou mais

#     Faça um programa que receba o código do produto (número inteiro positivo), o valor unitário
#     e o total em estoque. Para cada produto informado o sistema deverá apresentar qual desconto 
#     foi concedido e o novo valor unitário. O sistema irá finalizar quando forem digitados 6 
#     códigos do produto.

for i in range (6) :
    print()
    codigo_produto = int(input(f"Digite o código do produto {i + 1}: "))
    valor_unitario = float(input(f"Digite o preço do produto {i + 1}: "))
    while valor_unitario < 0 :
        print("Preço inválido")
        valor_unitario = float(input(f"Digite novamente o preço do produto {i + 1}: "))
    total_estoque = int(input(f"Digite o total em estoque do produto {i + 1}: "))
    while total_estoque < 0 :  
        print("Quantidade de estoque inválida.")
        total_estoque = int(input(f"Digite novamente o total em estoque do produto {i + 1}: "))


    if total_estoque <= 2 :
        desconto = valor_unitario * 0.6
        print()
        print("Concedido desconto de 40%")
        print(f"Novo valor unitário: R$ {desconto}")
    elif total_estoque > 2 and total_estoque <= 5 :
        desconto = valor_unitario * 0.7
        print()
        print("Concedido desconto de 30%")
        print(f"Novo valor unitário: R$ {desconto}")
    elif total_estoque > 5 and total_estoque <= 9 :
        desconto = valor_unitario * 0.8
        print() 
        print("Concedido desconto de 20%")
        print(f"Novo valor unitário: R$ {desconto}")
    else :
        desconto = valor_unitario * 0.9
        print() 
        print("Concedido desconto de 10%")
        print(f"Novo valor unitário: R$ {desconto}")

    if i == 5 :
        print()
        print("Finalizando...")
        break