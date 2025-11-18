X={13,15,31,26, 73}
Y={16,14,42,26,87}
Z={26,54,8,9,23,31}
p_s=not(X|Y|Z)
p_d=(not(X)) and (not(Y)) and (not(Z))
if p_s==p_d:
 print ('legea 1 este adevarata')
else:
 print('legea 1 este gresita')

p_s_b=not (X&Y&Z)
p_d_b=(not(X)) | (not(Y)) | (not(Z))
if p_s_b==p_d_b:
 print("legea 2 este corecta")
else:
 print ("legea 2 este gresita")