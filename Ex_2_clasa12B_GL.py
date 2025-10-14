a,b,c=float(input('a=')), float (input('b=')), float (input('c='))
import math
if ((a+b>c) and (a+c>b) and (b+c>a)) :
    def mediana_a():
        return 0.5*math.sqrt((2*(b**2))+(2*(c**2))-a**2)
    def mediana_b():
        return 0.5*math.sqrt ( (2*(a**2)) +(2*(c**2))-b**2)
    def mediana_c():
        return 0.5*math.sqrt((2*(a**2)) +(2*(b**2))-c**2)

print ('Mediana de a=',mediana_a())
print ('Mediana de b=', mediana_b())
print ('Mediana de c=', mediana_c())