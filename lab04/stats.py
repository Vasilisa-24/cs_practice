def parse_record(line):
    l1 = line.split(";")
    if len(l1)!=3:
        raise ValueError("Передано не три поля")
    l1 = [item.strip() for item in l1]
    if l1[0] == "" or l1[1] == "":
        raise ValueError("Пустое поле города или даты")
    try:
        l1[1] = float(l1[1].replace(',','.')
    except ValueError:
        raise ValueError("Данные о темп-ре не являются числом")
    total = {"city": l1[0], "temperature": l1[1], "date": l1[2]}
    return total

def read_valid(lines):
    lis = []
    for line in lines:
        if not line.strip():
            continue
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
    if not mit:
        return ''
    best = None
    maxt = -float('inf')
    for city, temp in mit.items():
        if temp > maxt:
            maxt = temp
            best = city
    return best
    
