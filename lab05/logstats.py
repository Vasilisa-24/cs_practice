from collections import Counter

def parse_event(line: str) -> dict:
    parts = line.strip().split()
    if len(parts) < 3:
        raise ValueError("Недостаточно частей в строке")
    
    time, level, message = parts
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("Неизвестный уровень")
        
    return {"time": time, "level": level, "message": message}


