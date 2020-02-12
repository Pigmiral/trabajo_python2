import random
num =int(input("digite la cantidad de numeros que quiera tener en la lista"))
lista=[]
a=0
b=0
while a<num:
    lista.append(random.randint(0,50))
    a+=1

while b<num:
  print(lista[b])
  b+=1
  
