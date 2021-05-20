counter = 0
counter_max = -901290902910280739
word = ""
for i in range(0, 2):
    x = input()
    x = x.strip()
    letters= []
    for letter in x:
        if letters.count(letter) == 0: 
            letters.append(letter)
        else:
            pass
    counter = len(letters)
    if counter > counter_max:
        counter_max = counter
        word = x
print(word, counter_max)


