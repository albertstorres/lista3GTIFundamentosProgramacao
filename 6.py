# 6 - Desenvolva um programa utilizando o FOR que faça a tabuada de um número inteiro que será digitado
#     pelo usuário. Mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial
#     e final devem ser informados pelo usuário.
#     Segue um exemplo: Montar a tabuada do: 5
#     Começar por: 4
#     Terminar em: 7

#     Saída de dados:
#     5 x 4 = 20
#     5 x 5 = 25
#     5 x 6 = 30
#     5 x 7 = 35

tabuada = int(input("Montar tabuada do: "))
comecar = int(input("Começar por: "))
terminar = int(input("Terminar em: ")) + 1

for i in range (comecar, terminar) :
    print(f"{tabuada} x {i} = {tabuada * i}")