#Grafico pastel

import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
sizes = [25, 30, 15, 30]

plt.pie(sizes, labels=categories, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue', 'lightgreen', 'lightskyblue'])
plt.title('Gráfico de Pastel de Proporciones')
plt.show()
