# the class that makes all the conversions + defines the typical math operations
class Rim:
    all_num = 'LXIVMCD'
    dict_num = {'L': '50', 'X': '10', 'I': '1', 'V': '5', 'M': '1000', 'C': '100', 'D': '500'}

    def __init__(self, rim_number, exception=True, ten=0):
        self.rim_number = rim_number
        self.exception = exception
        self.ten = ten

        cnt = 0
        for ltn, lt1 in enumerate(rim_number):
            for lt2 in rim_number[ltn + 1:]:
                if lt1 == lt2:
                    cnt += 1
            if cnt >= 4:
                self.exception = False
                break

# checks if all the letters are rim numbers
        if self.exception:
            for i in self.rim_number:
                if i not in Rim.all_num:
                    self.exception = False
                    break

# checks if there are no more than 3 equal letters in a row
        if self.exception:
            dict_ten = []
            for i in self.rim_number:
                dict_ten.append(int(Rim.dict_num[i]))
            for j in range(len(dict_ten)):
                try:
                    if dict_ten[j] < dict_ten[j + 1]:
                        self.ten -= dict_ten[j]
                    else:
                        self.ten += dict_ten[j]
                except IndexError:
                    self.ten += dict_ten[j]

    def __str__(self):
        if self.exception:
            return str(self.ten)
        else:
            return 'Некоректное значение'

# calculations
    def __add__(self, other):
        return self.ten + other.ten

    def __sub__(self, other):
        return self.ten - other.ten

    def __mul__(self, other):
        return self.ten * other.ten

    def __truediv__(self, other):
        return self.ten / other.ten

    def __floordiv__(self, other):
        return self.ten // other.ten

    def __mod__(self, other):
        return self.ten % other.ten

    def __pow__(self, other):
        return self.ten ** other.ten

# comparison block
    def __lt__(self, other):
        return self.ten < other.ten

    def __le__(self, other):
        return self.ten <= other.ten

    def __eq__(self, other):
        return self.ten == other.ten

    def __ne__(self, other):
        return self.ten != other.ten

    def __gt__(self, other):
        return self.ten > other.ten

    def __ge__(self, other):
        return self.ten >= other.ten

