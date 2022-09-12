import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
input_values = [1, 2, 3, 4, 5]

plt.plot(input_values, squares, linewidth=3)

# точки на диаграмме
plt.scatter(input_values, squares, s=200)


# заголовок и метки осей
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# размер шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

# отображаем диаграмму
plt.show()