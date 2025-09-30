x,y=int(input('a=')), int(input('b='))
def suma_ab(a,b): 
    return a+b

def produs_ab(a,b): 
    return a*b

def media_ab(a,b):    
    return (a+b)/2

def min_ab(a,b):      
    return min(a,b)

def maxim_ab(a,b):    
    return max(a,b) 

def radacina_ab(a,b):
    return -b/a

def cmmdc_ab(a, b):   
    while b!= 0:
        a,b = b, a%b
    return a

def cmmmc_ab(a,b):    
    return abs(a * b) // cmmdc_ab(a, b)

print('a) Suma numerelor =', suma_ab(x,y))
print('b) Produsul numerelor = ', produs_ab(x, y))
print('c) Media numerelor = ', media_ab(x,y))
print('d) Minimul numerelor = ', min_ab(x, y))
print('e) Maximul numerelor=', maxim_ab(x,y))
print('f) ',x,'+',y,'=', suma_ab(x,y))
print('g) ',x,'*',y,'=', produs_ab(x,y))
print('h) (',x,'*',y,')/2=', media_ab(x,y))
print('i) Rădăcina ecuației ax+b=0:' , radacina_ab(x,y))
print('j) Cel mai mare divizor comun =', cmmdc_ab(x,y))
print('k) Cel mai mic multiplu comun =', cmmmc_ab(x,y))