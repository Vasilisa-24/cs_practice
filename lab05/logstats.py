from collections import Counter

def parse_event(line: str) -> dict:
    parts = line.strip().split()
    if len(parts) < 3:
        raise ValueError("Недостаточно частей в строке")
    
    time, level, message = parts
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("Неизвестный уровень")
        
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = Counter()
    for line in lines:
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return dict(counts)

