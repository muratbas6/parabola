import matplotlib.pyplot as plt

data2 = eval(input("A'yi gir: "))
data = eval(input("B'yi gir: "))
data1 = eval(input("C'yi gir: "))
a=[]
b=[]
# y=0
# x=-50

for x in range(-50,50,1):
    y=data2*x**2+data*x-data1
    a.append(x)
    b.append(y)
    #x= x+1

fig= plt.figure()
axes=fig.add_subplot(111)
axes.plot(a,b)
r = data/-2
k = data2*r**2+data*r+(data1)
plt.plot([r],[k],"ro")
print(r,k)
plt.show()

