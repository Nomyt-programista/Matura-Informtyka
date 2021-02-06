def palindrom(n):
    i = 0
    n = str(n)
    while i<len(n)/2:
        if n[i] == n[(i+1)*-1]:
            pass
        else:
            return False
        i +=1
    return True
