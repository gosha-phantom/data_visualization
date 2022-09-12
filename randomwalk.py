from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
    """Генерирование случайных блужданий"""

    def __init__(self, num_points=5000):
        """Инициализация атрибутов блуждания"""
        self.num_points = num_points

        # все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
            """Определяет направление и длину смещения"""
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4])
            return direction * distance

    def fill_walk(self):
        """Шаги генерируются до достижения нужной длины"""
        while len(self.x_values) < self.num_points:
            # # определение направления и длины перемещения
            x_step = self.get_step()
            y_step = self.get_step()

            # вычисление следующих значений x и y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # добавляем новые точки в массив
            self.x_values.append(next_x)
            self.y_values.append(next_y)

        

# создаем экземпляр класса блужданий
rw = RandomWalk()
# создаем массивы точек блужданий с координатами
rw.fill_walk()

# выводим точки на диаграмму
point_numbers = list(range(rw.num_points))
# прорисовка точками
plt.scatter(rw.x_values, rw.y_values, s=15, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')
# прорисовка линиями
# plt.plot(rw.x_values, rw.y_values, linewidth=1, c='blue')

# выделение первой и последней точек
plt.scatter(0, 0, s=50, c='green', edgecolors='none')
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

# удаление осей с дмаграммы = НЕ РАБОТАЕТ
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

# назначение размера области просмотра
# plt.figure(figsize=(10,6))

# показать график
plt.show()