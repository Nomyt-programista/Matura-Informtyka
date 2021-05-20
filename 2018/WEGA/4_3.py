
counter = 0 
lista = []

for i in range(0, 1000):
    x= input()
    x = x.strip()
    counter = 0
    for z in range(0, len(x)):
        if z+1== len(x):
            break
        letter_first = ord(x[z]) - 96
        letter_second = ord(x[z+1]) -96
        if max(letter_first, letter_second) - min(letter_first, letter_second) <= 10:
            counter += 1
        else:
            break
    if counter +1 == len(x):
        lista.append(x)

print(lista)


# wszystkie kurwa litery cwelu pierdolony szmato kurwoi 