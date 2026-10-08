def parse_record(line):
    l1 = line.split(";")
    if len(l1)!=3:
        raise ValueError("Передано не три поля")
    if l1[0] == "" or l1[1] == "":
        raise ValueError("Пустое поле города или даты")
    try:
        float(l1[2])
    except ValueError:
        raise ValueError("Данные о темп_ре не являются числом")
    total = {"Город": l1[0], "Дата": l1[1], "Температура": l1[2]}
    return total


'''import sys

lines = sys.stdin.read().splitlines()
total = {}
count = {}
for line in lines:
    city, temp, date = line.split(";")
    total[city] = total.get(city, 0) + float(temp)
    count[city] = count.get(city, 0) + 1
best = ""
for city in total:
    if best == "" or total[city] / count[city] > total[best] / count[best]:
        best = city
print(len(lines))
print(0)
print(total[best] / count[best])'''
