def read_valid(lines: list(str)) -> list[dict]:
    lis = []
    for line in lines:
        try:
            a = parse_record(line)
            lis.append(a)
        except ValueError:
            continue

        
