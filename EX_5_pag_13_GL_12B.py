x,y,m,n=int(input('a=')), int(input('b=')),  int(input('c=')),  int(input('d='))
def suma_abcd(a,b,c,d): 
    return a+b+c+d

def media_abcd(a,b,c,d):    
    return (a+b+c+d)/4

def min_abcd(a,b,c,d):      
    return min(a,b,c,d)

def radacina_ab(a,b):
    return -b/a

def cmmdc_ab(a, b):   
    while b!= 0:
        a,b = b, a%b
    return a

def cmmmc_ab(a,b):    
    return abs(a * b) // cmmdc_ab(a, b)
print('a) Suma numerelor =', suma_abcd(x,y,m,n))
print('b) Media numerelor =', media_abcd(x,y,m,n))
print('c) Minimum numerelor =', min_abcd(x,y,m,n))
print('f) Rădăcina ecuației ax+b=0:' , radacina_ab(x,y))
print('h) Cel mai mare divizor comun =', cmmdc_ab(x,y))
print('i) Cel mai mic multiplu comun =', cmmmc_ab(x,y))




