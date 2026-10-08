def parse_record(line):
    l1 = line.split(";")
    if len(l1)!=3:
        raise ValueError("Передано не три поля")
    if l1[0] == "" or l1[1] == "":
        raise ValueError("Пустое поле города или даты")
    try:
        l1[2] = float(l1[2])
    except ValueError:
        raise ValueError("Данные о темп-ре не являются числом")
    total = {"Город": l1[0], "Дата": l1[1], "Температура": l1[2]}
    return total

def read_valid(lines):
    lis = []
    for line in lines:
        try:
            a = parse_record(line)
            lis.append(a)
        except ValueError:
            continue
    return lis
        
def average_by_city(records):
    total = {}
    count = {}
    midt = {}
    for record in records:
        city, temp, date = record.values()
        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1
    for city in total:
        midt[city] = float(f'{(total[city]/count[city]):.1f}')
    return midt

def warmest_city(records):
    mit = average_by_city(records)
    best = ''
    for city in mit:
        if mit[city] >mit.get(best, "0"):
            best = city
    return best
    
