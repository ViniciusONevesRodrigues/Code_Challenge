print("\n")
print('Coloque em maiúscula a primeira letra de cada frase na sting', )
print("\n")
#Input para receber a frase
frase = str(input("Digite a string: ")).capitalize()
#Transformando a frase em uma lista
lista = frase.split()
#Colocando maiúsculo em cada frase
for i in range(len(lista)):
    if lista[i][-1] in '!?.':
        lista[i+1] = lista[i+1].capitalize()
#Variavel com espaçamento
espaco = " "
#Transformando lista de volta a frase
resultado = espaco.join(lista)
#Apresentação do resultado
print("\n")
print(resultado)
print("\n")