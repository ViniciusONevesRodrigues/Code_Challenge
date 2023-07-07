print("\n")
print('Verifique se a string é um anagrama de um palíndromo')
print("\n")
#Input para receber a frase
frase = str(input('Digite uma palavra: ')).strip().upper()
#Transformando em lista
lista = frase.split()
#Juntando tudo
j = ''.join(lista)
#Variavel para colocar o inverso
inverso = ''
#Invertendo tudo
for letra in range(len(j)-1, -1, -1):
    inverso += j[letra]
#Apresentação do resultado
print("\n")
print(inverso == j)
print("\n")
