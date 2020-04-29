from space import Ufo
import turtle as tr
from random import randint
tr.tracer(0)

#u1 = Ufo('Рокетааа-0', 100, 150, 100, 'green', 5, 2, False, False)
u2 = Ufo('Рокетааа-999', -50, 50, 200, 'red', 3, 6)

for i in range(50):
    x = randint(-10, 10)
    y = randint(-10, 10)
    u1 = Ufo('Рокетааа-0', x, y, 100, 'green', 5, 2, False, False)
    u1.show()
    u1.high()


#u1.set_name('Пришелец')
#t.speed(0)

#u2.show()
print(u1.get_name())

u1.set_maid_in= 'USA'
#print(u1.made_in)\
#u2.engine_grade = ''
#print(u2.engine_grade)
tr.update()
tr.done()

#метод убирающий нарисованную тарелку