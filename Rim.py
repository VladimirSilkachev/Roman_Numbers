class Rim:

    all_num = 'LXIVMCD'
    dict_num = {'L': '50', 'X': '10', 'I': '1', 'V': '5', 'M': '1000', 'C': '100', 'D': '500'}
    dict_ten = list()

    def __init__(self, rim_number, exception=True):
        all_num = 'LXIVMCD'
        self.rim_number = rim_number
        self.exception = exception

        cnt = 0
        for ltn, lt1 in enumerate(rim_number):
            for lt2 in rim_number[ltn + 1:]:
                if lt1 == lt2:
                    cnt += 1
            if cnt >= 4:
                self.exception = False
                break

        if self.exception:
            for i in self.rim_number:
                if i not in all_num:
                    self.exception = False
                    break

    def __str__(self):

        if self.exception:
            dict_num = {'L': '50', 'X': '10', 'I': '1', 'V': '5', 'M': '1000', 'C': '100', 'D': '500'}
            dict_ten = list()
            ten = 0

            for i in self.rim_number:
                dict_ten.append(dict_num[i])
            for j in range(len(dict_ten)):
                try:
                    if dict_ten[j] < dict_ten[j + 1]:
                        ten -= int(dict_ten[j])
                    else:
                        ten += int(dict_ten[j])
                except IndexError:
                    ten += int(dict_ten[j])

            return str(ten)

        else:
            return 'Некоректное значение'
