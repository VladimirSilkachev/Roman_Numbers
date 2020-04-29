import turtle as tr
import math


class Ufo:
    def __init__(self, name, x, y, size, color, count_pillars,
                 count_lamps, pillars_down=True, show_name=True, made_in = 'Russia', engine_grade = 'Turbo'):
        self.__name = name
        #а двойное подчеркивание помогет защитить переменную от пользователя
        #self._name = name внутренняя переменная, пользовтель в интерфейсе к ней не может обращаться
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillars_down
        self.show_name = show_name
        #это ствойство,
        self.__made_in = made_in
        self.__engine_grade = engine_grade


    @property
    def engine_grade(self):
        return self.__engine_grade

    @engine_grade.setter
    def engine_grade(self, new_grade):
        if new_grade == '':
            print('ERROR')
        else:
            self.__engine_grade == new_grade

    @engine_grade.getter
    def engine_grade(self):
        if self.__engine_grade == 'Turbo':
            return 'Стандартный'
        else:
            return  self.__engine_grade



#декоратор это функция, которая в параметре имеет функцию, и
# она способна расщиить функционал, она не только возвращает но и печатает

    @property
    def set_made_in(self, made_in):
        counries = ['USA', 'Russia']
        if made_in in counries:
            self.__made_in = made_in
        else:
            self.__made_in = None

    @property
    def get_maid_in(self, maid_in):
        self.__made_in = maid_in

    def __str__(self):
        s = 'Сконструировано НЛО'
        if self.show_name:
            s += ' под названием {name}\n'.format(name=self.name)
        else:
            s += ' с неизвестным названием\n'
        s += 'Координаты НЛО: ({x}; {y})\n'.format(x=self.x, y=self.y)
        s += 'Размер: {size}\n'.format(size=self.size)
        s += 'Размер: {size}\n'.format(size=self.size)
        if self.pillars_down:
            s += 'Опроы опущены\n'
        else:
            s += 'Опроы подняты\n'
        s += 'Количество опор: {count}'.format(count=self.count_pillars)
        s += 'Количество фонарей: {count}'.format(count=self.count_lamps)
        return s


    def __repr__(self):
        return self.__str__()

    #помогает обратиться к переменной, которой мы псотавили двойное подчеркивание
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name



    def show(self):

        tr.ht()
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                tr.penup()
                tr.goto(self.x, self.y + self.size/3)
                tr.pendown()
                tr.goto(lx, self.y - self.size/6)

        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor('blue')
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

        tr.penup()
        tr.fillcolor(self.color)
        tr.goto(self.x - self.size / 2, self.y + self.size / 4)
        tr.pendown()
        tr.begin_fill()
        tr.fd(self.size)
        i = math.pi / 2
        while i <= 3 * math.pi / 2:
            sx = (self.size / 2) * math.sin(i)
            sy = (self.size / 3) * math.cos(i)
            tr.goto(self.x + sx, self.y + self.size/4 + sy)
            i += math.pi / self.size
        tr.end_fill()

        tr.fillcolor('yellow')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            tr.begin_fill()
            tr.penup()
            tr.goto(self.x -self.size / 2 + i * dx, self.y + self.size / 14)
            tr.pendown()
            tr.circle(dx/4)
            tr.end_fill()

        tr.penup()
        if self.show_name:
            tr.goto(self.x, self.y + self.size / 2)
            tr.pendown()
            #t.write(self.name, align='center')
            tr.penup()
        tr.goto(0, 0)
        tr.st()

    def high(self):
        tr.pencolor('white')
        tr.ht()
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                tr.penup()
                tr.goto(self.x, self.y + self.size / 3)
                tr.pendown()
                tr.goto(lx, self.y - self.size / 6)

        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor('white')
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

        tr.penup()
        tr.fillcolor('white')
        tr.goto(self.x - self.size / 2, self.y + self.size / 4)
        tr.pendown()
        tr.begin_fill()
        tr.fd(self.size)
        i = math.pi / 2
        while i <= 3 * math.pi / 2:
            sx = (self.size / 2) * math.sin(i)
            sy = (self.size / 3) * math.cos(i)
            tr.goto(self.x + sx, self.y + self.size / 4 + sy)
            i += math.pi / self.size
        tr.end_fill()

        tr.fillcolor('white')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            tr.begin_fill()
            tr.penup()
            tr.goto(self.x - self.size / 2 + i * dx, self.y + self.size / 14)
            tr.pendown()
            tr.circle(dx / 4)
            tr.end_fill()

        tr.penup()
        if self.show_name:
            tr.goto(self.x, self.y + self.size / 2)
            tr.pendown()
            # t.write(self.name, align='center')
            tr.penup()
        tr.goto(0, 0)
        tr.st()

