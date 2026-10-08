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
