def decToBin(n):
  binarna = ""
  if n == 0:
    binarna = "0"
    return binarna
  while n != 1:
    binarna = binarna + str(n%2)
    n = n//2
  binarna = binarna + "1"
  binarna = binarna[::-1]
  return binarna

def decimalToBinary(n):  
    if(n > 1):  
        decimalToBinary(n//2)  
    print(n%2, end=' ') 

def decimalToBinary2(n): 
    return bin(n).replace("0b","") 
