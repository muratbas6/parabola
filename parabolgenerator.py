import matplotlib.pyplot as plt
from math import sqrt

#ax**2+bx+c

a1 = eval(input("A'yi gir: "))
b1 = eval(input("B'yi gir: "))
c1 = eval(input("C'yi gir: "))
a=[]
b=[]



for x in range(-7,7,1):
    y=(a1*(x**2))+(b1*x)+(c1)
    a.append(x)
    b.append(y)
    
fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)

r = -1*(b1/2*a1)

k = (a1*(r**2))+(b1*r)+(c1)

y1 = a1*(0**2)+(b1*0)+c1

c = (b1**2)-4*(a1*c1)
d = abs(c)
print("Delta",d)

if b1 == 0:
    x1 =0
    x2 =0
    
else:
    x1 = (-b1+sqrt(d))/2*a1
    x2 = (-b1-sqrt(d))/2*a1

plt.plot([r],[k],"ro")
plt.plot([0],[y1],"yo")
plt.plot([x1],[0],"ko")
plt.plot([x2],[0],"ko")
print("Tepe noktası: ",r,k)
print("Y'yi kestigi nokta",y1)
print("X'i kestigi noktalar",x1,x2)
plt.show()
