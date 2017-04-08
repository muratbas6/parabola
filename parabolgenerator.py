import matplotlib.pyplot as plt

a1 = eval(input("A'yi gir: "))
b1 = eval(input("B'yi gir: "))
c1 = eval(input("C'yi gir: "))
a=[]
b=[]


for x in range(-100,100,1):
    y=a1*x**2+b1*x-c1
    a.append(x)
    b.append(y)
    #x= x+1

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
r = -1*(b1/2*a1)
k = (a1*(r**2))+(b1*r)+(c1)
plt.plot([r],[k],"ro")
print(r,k)
plt.show()

