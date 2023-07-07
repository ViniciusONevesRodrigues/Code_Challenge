print("\n")
print('Reverta a ordem das palavras nas frases, mantendo a ordem das palavras')
print("\n")
#Input para receber a frase
frase = str(input('Digite a frase: '))
#Transformando a frase em uma lista
lista = frase.split()
#Invertendo a ordem dos vetores
invertido = lista[::-1]
#Variavel com espaçamento
espaco = " "
#Transformando lista de volta a frase
resultado = espaco.join(invertido)
#Apresentação do resultado
print("\n")
print(resultado)
print("\n")