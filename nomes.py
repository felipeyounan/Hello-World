entrada = input("Digite seu nome completo: ")
palavras = entrada.split()

variaveis = {}
num_palavras = len(palavras)

for i in range(len(palavras)):
    variaveis["var" + str(i+1)]=palavras[i]



#primeiro_nome = palavras[0]
#segundo_nome = palavras[1]
#terceiro_nome = palavras[2]


print(num_palavras)
