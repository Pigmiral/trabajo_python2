lista=[]
a=0
b=0
mayor=0
con=0
prome=0
while a<3:
 num=int(input("digite un numero:"))
 lista.append(num)
 prome+=num
 a+=1
 if num>mayor:
  mayor=num

 if num==5:
   con+=1  

while b<3:
 print(lista[b])
 b+=1

print("el mayor es:",mayor)
print("las veces que digito 5 fue ",con)
print("el proemdio fue:",prome/a)
