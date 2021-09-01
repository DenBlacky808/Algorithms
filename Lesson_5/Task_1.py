from collections import defaultdict


def average_profit(def_dict):
    num_comps_1 = 0
    sum_all = 0
    for _ in def_dict.keys():
        num_comps_1 += 1
        for value in def_dict.values():
            sum_all = sum_all + sum(value)
    return sum_all / num_comps_1 ** 2


def good_comp(def_dict):
    good_comps_list = []
    for c_name, profit_per_quarter in def_dict.items():
        if sum(profit_per_quarter) > average_profit(def_dict):
            good_comps_list.append(c_name)
    return good_comps_list


def bad_comp(def_dict):
    bad_comps_list = []
    for c_name, profit_per_quarter in def_dict.items():
        if sum(profit_per_quarter) < average_profit(def_dict):
            bad_comps_list.append(c_name)
    return bad_comps_list


s = defaultdict(list)
num_comps = int(input('Введите количество компаний '))
for _ in range(num_comps):
    company_name = input('Введите название компании ')
    for i in range(4):
        profit = int(input(f'Введите прибыль в {i + 1} квартале '))
        s[company_name].append(profit)

print(f'Среднее значение прибыли {average_profit(s)}')
print(f'Прибыльные компании \n{good_comp(s)}')
print('*' * 40)
print(f'Убыточные компании \n{bad_comp(s)}')
