import random
n=int(input('Dati numarul de aruncari='))
c6=0
for x in range(n):
    nr=random.randint(1,6)
    if nr==6:
        c6+=1
    print (nr, end='')
print()
print('cifra 6 nimereste de ',c6,'ori')