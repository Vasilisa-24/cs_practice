from stats import average_by_city, read_valid, warmest_city
import sys

lines = sys.stdin.read().splitlines()

non_empt = [line for line in lines if line.strip()]

valid_lines = read_valid(non_empt)
if not valid_lines:
    sys.exit(0)
best_city = warmest_city(valid_lines)
aver = average_by_city(valid_lines)
best_t = averages.get(best_city,0.0)
print(len(valid_lines))
print(len(lines) - len(valid_lines))
print(best_t)
