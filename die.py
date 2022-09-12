from random import randint
import pygal

class Die():
    """Класс для представления одного кубика"""

    def __init__(self, num_sides=6):
        """По умолчанию шестигранный кубик"""
        self.num_sides = num_sides

    def roll(self):
        """Возвращает случайное число от 1 до числа граней"""
        return randint(1, self.num_sides)

# моделирование бросков кубика с сохранением результатов в список
die_1 = Die()
die_2 = Die(10)
max_num_sides = die_1.num_sides + die_2.num_sides
num = 10000
results = []
for roll in range(num):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# определяем частоту выпаданий значений кубика
freqencies = []
for val in range(1, max_num_sides + 1):
    freq = results.count(val)
    freqencies.append(freq)

# print(results, '/n', freqencies)

# визуализация результатов
hist = pygal.Bar()

hist.title = f'Results of rolling one D{(die_1.num_sides)} and one D{die_2.num_sides} {num} times'
hist.x_labels = [str(x) for x in list(range(1, max_num_sides + 1))]
hist._x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add(f'D{(die_1.num_sides)} + D{die_2.num_sides}', freqencies)
hist.render_to_file('die_visual.svg')

# print([str(x) for x in list(range(1, die.num_sides + 1))])
