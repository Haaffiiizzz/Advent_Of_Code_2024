with open("day4input.txt", "r") as file:
    file = file.read()
import re

pattern = r"XMAS"
check = re.findall(pattern, file)
print(len(check))