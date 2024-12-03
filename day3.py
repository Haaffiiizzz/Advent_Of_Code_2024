import re
with open("day3input.txt", "r") as file:
    file_lines = file.read()

pattern = r"mul\((\d+),(\d+)\)"

match = re.findall(pattern, file_lines)
print(match)

total = sum(int(x) * int(y) for x, y in match)
print(total)

