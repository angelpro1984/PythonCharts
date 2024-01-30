import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values  = [250,410, 100, 200]
colores=['red','skyblue','green','black']
plt.bar(categories, values,color=colores)

plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Ventas en dólares ($)')
plt.show()

