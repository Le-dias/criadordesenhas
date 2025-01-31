

chave = input('Digite um senha: ')

senha = ''

for letra in chave:
    if letra in 'Aa': senha  = senha + '!'
    elif letra in 'Bb': senha = senha + '@'
    elif letra in 'Cc': senha = senha + '%'
    elif letra in 'Dd': senha = senha + '&'
    elif letra in 'Ee': senha = senha + '4'
    elif letra in 'Ff': senha = senha + '7'
    elif letra in 'Rr': senha = senha + '$'
    elif letra in 'Uu': senha = senha + '0'
    elif letra in 'Ii': senha = senha + '*'
    else: senha  = senha + letra
print(senha)

    