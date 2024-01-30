import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y1=[10, 12,25,30,35]
y2=[5,10,20,25,35]

plt.fill_between(x, y1, y2, color='blue', alpha=0.2)
plt.title('Area Chart')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()

