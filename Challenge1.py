#Input para receber a frase
frase = str(input('Digite uma frase: '))
#Transformando a frase em uma lista
reverso = frase.split()
#Invertendo a ordem dos vetores
reverso.sort(reverse=True)
#Variavel com espaçamento
espaco = " "
#Transformando lista de volta a frase
resultado = espaco.join(reverso)
#Apresentação do resultado
print(resultado)