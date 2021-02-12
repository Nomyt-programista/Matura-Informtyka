# 11:55 AM
import math
from os import kill

file = open("2016/Dane/punkty.txt","r")
items = []
pi = []

for item in file:
    item = item.split(" ")
    helplist = []
    for number in item:
        number = int(number)
        helplist.append(number)
    items.append(helplist)

    
def zad_41():
    counter = 0
    for item in items:
        x = item[0]
        y = item[1]
        r = math.sqrt((x-200)*(x-200)+(y-200)*(y-200))
        if r == 200:
            print(x,y)
        if r<200:
            counter += 1
    print(counter)

def zad_42():
    nk = 0
    for i in range(0,1000):
        x = items[i][0]
        y = items[i][1]
        r = math.sqrt((x-200)*(x-200)+(y-200)*(y-200))
        if r <= 200:
            nk += 1
   
    pi = (4*nk)/1000
    print(pi)
    nk = 0
    for i in range(0,5000):
        x = items[i][0]
        y = items[i][1]
        r = math.sqrt((x-200)*(x-200)+(y-200)*(y-200))
        if r <= 200:
            nk += 1

    pi = (4*nk)/5000
    print(pi)
    nk = 0
    for i in range(0,10000):
        x = items[i][0]
        y = items[i][1]
        r = math.sqrt((x-200)*(x-200)+(y-200)*(y-200))
        if r <= 200:
            nk += 1
    pi = (4*nk)/10000
    print(pi)

def zad_43():
    for i in range(1000,1701):
        nk = 0
        for i in range(0,i):
            x = items[i][0]
            y = items[i][1]
            r = math.sqrt((x-200)*(x-200)+(y-200)*(y-200))
            if r <= 200:
                nk += 1 
        pis = (4*nk)/(i+1)
        dpi = pis - math.pi
        pi.append(dpi)
    print(pi)
    
zad_41()
zad_42()
zad_43()

#12:35 
