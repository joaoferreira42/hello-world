from time import sleep
p = input('Coloque alguma frase aqui -> ')
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i = 0
lim = len(p)
palavra = ''

while i < lim:
    l1 = p[i]
    for letra in abc:
        if letra != l1:
            print(palavra + letra)
            sleep(0.05)
        else:
            print(palavra + letra)
            break
    palavra += l1
    i += 1
