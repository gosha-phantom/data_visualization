import matplotlib.pyplot as plt

x_val = list(range(1, 101))
y_val = [x**2 for x in x_val]

# присвоение цвета точкам: c=(0, 0, 0, 0.8)
# присвоение точкам цветовой карты: c=y_val, cmap=plt.cm.Blues
plt.scatter(x_val, y_val, edgecolor='none', s=20, c=y_val, cmap=plt.cm.Blues)

# заголовок и метки осей
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# размер шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

# диапазон для каждой оси
plt.axis([0, 111, 0, 1100000])

# отображаем диаграмму
plt.show()

# сохраняем диаграмму
# plt.savefig('scatter_squares.png', bbox_inches='tight')