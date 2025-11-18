import random
X = {random.randint(0,199)for i in range(20)}
Y = {random.randint(0,199)for i in range(20)}
print(('a'), X|Y)
print(('b'), X&Y)
print(('c'), X-Y)
print(('d'), (X-Y)|(Y-X))
print(('e'), (X-Y) & (Y-X))