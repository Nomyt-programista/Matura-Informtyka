# 7:46 

file = open("2015/Dane/liczby.txt", "r")
items = []

for item in file:
    item = int(item) 
    items.append(item)

def decToBin(binary):   
    # binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def zad_41():
    master_counter = 0
    for item in items:
        counter = 0
        for number in str(item):
            if number == "0":
                counter +=1 
        if counter > len(str(item))/2:
            master_counter += 1
    print(master_counter)

def zad_42():
    p2 = 0 
    p8 = 0
    for item in items:
        bina = int(decToBin(item))
        if bina %2 == 0:
            p2 +=1 
        if bina %8 == 0:
            p8 +=1
    print(f"podzielne przez 8: {p8}, podzielne przez 2: {p2}")

def zad_43():
    maxi = 0
    mini = 1605828497222164613922119051741599036763721501353852720943011
    lmaxi = 0
    lmini = 0
    i = 0
    for item in items:
        i +=1
        bina  = int(decToBin(item))
        if bina > maxi:
            maxi = bina
            lmaxi = i
        elif bina < mini:
            mini = bina
            lmini = i 
    print(f"max: {maxi} linia: {lmaxi}, mini: {mini} linia: {lmini}")


zad_41()
zad_42()
zad_43()


