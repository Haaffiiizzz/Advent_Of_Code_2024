with open("day1input.txt", "r") as file:
    file_lines = file.readlines()

right = []
left = []
for line in file_lines:
    right.append(int(line.split()[1]))
    left.append(int(line.split()[0]))
original_left = left[:]
original_right = right[:]

differences = 0
count = len(right)

while count > 0:
    differences += abs(min(right) - min(left))
    right.remove(min(right))
    left.remove(min(left))
    count -= 1
print(differences)


#part two


appearance = {}
score = 0
for num in original_left:
    occurence = original_right.count(num)
    score += occurence * num

print(score) 