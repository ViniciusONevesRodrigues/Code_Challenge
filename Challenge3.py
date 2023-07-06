f = str(input('Digite uma palavra: ')).strip().upper()

maior_palindromo = ''

for i in range(len(f)):
    for k in range(i+1, len(f)+1):
        subpalavra = f[i:k]
        if subpalavra == subpalavra[::-1] and len(subpalavra) > len(maior_palindromo):
            maior_palindromo = subpalavra
            
if maior_palindromo:
    print("O maior palíndromo na palavra é:", maior_palindromo)
else:
    print("Não foi encontrado nenhum palíndromo na palavra.")