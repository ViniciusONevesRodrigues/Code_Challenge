print("\n")
print('Encontre a substing palindroma mais longa na string abaixo')
print("\n")
#Input para receber a palavra
palavra = str(input('Digite a string: ')).strip()
#Variavel do maior palindroma
maior_palindroma = ''
#Procurando as palindromas e definindo o maior
for i in range(len(palavra)):
    for j in range(i+1, len(palavra)+1):
        subpalavra = palavra[i:j]
        if subpalavra == subpalavra[::-1] and len(subpalavra) > len(maior_palindroma):
            maior_palindroma = subpalavra
#Exibição de resultados    
print("\n")       
if maior_palindroma:
    print("O maior palíndromo na palavra é:", maior_palindroma)
else:
    print("Não foi encontrado nenhum palíndromo na palavra.")
print("\n")