# 4 - Foi realizada uma pesquisa de algumas características físicas de 5 alunos de um curso, a qual 
#     coletou os seguintes dados referentes a cada pessoa para serem analisados:
# a ) Gênero (masculino e feminino);
# b ) Cor dos olhos (azuis, verdes ou castanhos);
# c ) Cor dos cabelos (louros, castanhos, pretos);
# d ) Idade.

#     Faça um algoritmo que determine e escreva:
# a ) A quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35;
# b ) A quantidade de pessoas que tenham olhos castanhos e cabelos pretos.

quantidade_feminino_18_35 = 0
quantidade_olhos_castanhos_cabelos_pretos = 0

for i in range (5) :
    genero = input(f"Digite o gênero da {i + 1}ª pessoa (masculino ou feminino): ")
    cor_dos_olhos = input(f"Digite a cor dos olhos da {i + 1}ª pessoa (azuis, verdes ou castanhos): ")
    cor_dos_cabelos = input(f"Digite a cor dos cabelos da {i + 1}ª pessoa (louros, castanhos, pretos): ")
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))

    if genero == "feminino" and idade >= 18 and idade <= 35 :
        quantidade_feminino_18_35 += 1
    
    if cor_dos_olhos == "castanhos" and cor_dos_cabelos == "pretos" :
        quantidade_olhos_castanhos_cabelos_pretos += 1


print()
print(f"A quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35: {quantidade_feminino_18_35}")
print(f"A quantidade de pessoas que tenham olhos castanhos e cabelos pretos: {quantidade_olhos_castanhos_cabelos_pretos}")


