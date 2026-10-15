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


def top_errors(lines, n: int) -> list[list]:
    error_messages = Counter()
    for line in lines:
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                error_messages[event["message"]] += 1
        except ValueError:
            pass
    sorted_errors = sorted(error_messages.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]
