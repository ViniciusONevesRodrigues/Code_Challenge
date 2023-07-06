#Input para receber a frase
frase = str(input('Digite uma frase: '))
#Criando uma lista
palavrasU = []
#Transformando a frase em uma lista
lista = frase.split()
#Fazendo a filtração de palavras repetidas
for c in range(0, len(frase)):
    if frase[c] not in palavrasU:
        palavrasU.append(frase[c]) 
#Variavel com espaçamento
espaco = ""
#Transformando lista de volta a frase
resultado = espaco.join(palavrasU)
#Apresentação do resultado
print(resultado)