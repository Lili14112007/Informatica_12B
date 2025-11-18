el1= ("Popescu","Ana","F",10,9,9),
el2= ("Ionescu", "Mihai", "M", 7, 6, 5),
el3= ("Marin", "Ioana", "F", 9, 9, 9),
el4= ("Dinu", "Paul", "M", 8, 7, 9),
el5= ("Radu", "Elena", "F", 10, 10, 8)

print('1) nota medie obtinuta la sesiune de fiecare elev')
print(el1[:2],'cu media la teza de',sum(el1[3:])/3)
print(el2[:2],'cu media la teza de',sum(el2[3:])/3)
print(el3[:2],'cu media la teza de',sum(el3[3:])/3)
print(el4[:2],'cu media la teza de',sum(el4[3:])/3)
print(el5[:2],'cu media la teza de',sum(el5[3:])/3)

print('2)numele, prenumele elevilor restantieri')
if ((el1[3]<5) or (el1[4]<5) or (el1[5]<5)):
    print(el1[:2])
if ((el2[3]<5) or (el2[4]<5) or (el2[5]<5)):
    print(el2[:2])
if ((el3[3]<5) or (el3[4]<5) or (el3[5]<5)):
    print(el3[:2])  
if ((el4[3]<5) or (el4[4]<5) or (el4[5]<5)):
    print(el4[:2]) 
if ((el5[3]<5) or (el5[4]<5) or (el5[5]<5)):
    print(el5[:2])

print('3)numele, prenumele elevilor eminenti')
if ((el1[3]>=9)and(el1[4]>=9)and (el1[5]>=9)):
    print(el1[:2])
if ((el2[3]>=9)and(el2[4]>=9)and (el2[5]>=9)):
    print(el2[:2])
if ((el3[3]>=9)and(el3[4]>=9)and (el3[5]>=9)):
    print(el3[:2])
if ((el4[3]>=9)and(el4[4]>=9)and (el4[5]>=9)):
    print(el4[:2])
if ((el5[3]>=9)and(el5[4]>=9)and (el5[5]>=9)):
    print(el5[:2])
