from stats import average_by_city, read_valid, warmest_city
import sys

lines = [line for line in sys.stdin.read().splitlines() if line.strip()]
valid_lines = read_valid(lines)
if not valid_lines:
    sys.exit(0)
best_city = warmest_city(valid_lines)
best_t = average_by_city(valid_lines)[best_city]
print(len(valid_lines))
print(len(lines) - len(valid_lines))
print(best_t)


def deepest_path(paths):
    return max(paths, key=lambda path: (path.count('/'), path), default="")

def human_size(n_bytes):
    list_1 = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
    for i, unit in enumerate(list_1):
        if n_bytes < 1024:
            return f"{n_bytes:.1f} {unit}" if unit != 'Б' else f"{n_bytes} {unit}"
        n_bytes /= 1024
return f"{n_bytes:.1f} ТБ"
