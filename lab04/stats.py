def parse_record(line: str) -> dict:
    l1 = line.split(";")
    if len(l1)!=3:
        raise ValueError("Передано не три поля")
    if l1[0] == "" or l1[1] == "":
        raise ValueError("Пустое поле города или даты")
    try:
        l1[2] = float(l1[2])
    except ValueError:
        raise ValueError("Данные о темп_ре не являются числом")
    total = {"Город": l1[0], "Дата": l1[1], "Температура": l1[2]}
    return total

def read_valid(lines: list[str]) -> list[dict]:
    lis = []
    for line in lines:
        try:
            a = parse_record(line)
            lis.append(a)
        except ValueError:
            continue
        
def average_by_city(records: list[dict])-> dict:
    total = {}
    count = {}
    midt = {}
    for record in records:
        city, temp, date = record.values()
        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1
    for city in total:
        midt[city] = f'{total[city]/count[city]}:.1f'
    return midt

def warmest_city(records: list[dict]) -> str:
    mit = average_by_city(records)
    best = ""
    for city in mit:
        if mit[city] >mit.get(best, "0"):
            best = city
    return best
    

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
