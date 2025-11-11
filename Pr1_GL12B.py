import random
n=int(input('dati numarul de numere generate='))
Spoz=0
Sneg=0
for x in range(n):
    nr=random.randint(-50,50)
    if nr>0:
        Spoz+=nr
    else:
        Sneg+=nr
    print(nr, end='')
print()
print('suma numerelor pozitive =',Spoz)
print('suma numerelor negative =',Sneg)