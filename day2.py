with open("day2input.txt", "r") as file:
    file_lines = file.readlines()
    
count = 0
new_count = 0
def checkSafe(nums):
    
    safe = True
    trend = None
    for i in range(1, len(nums)):
            
            if nums[i] - nums[i-1] > 3 or nums[i] == nums[i-1] or nums[i] - nums[i-1] < -3:
                safe = False
                break
            current = "I" if nums[i] - nums[i-1] > 0 else "D"
            
            if trend and trend != current:
                safe = False
                break
            
            trend = current
    return safe

for line in file_lines:
    listOf = line.split()
    nums = [int(x) for x in listOf]
    
    if checkSafe(nums):
        count += 1
        
    else:
        for i in range(len(nums)):
            newList = nums[:i] + nums[i+1:]
            
            if checkSafe(newList):
                new_count += 1
                break
            
print(count)
print(new_count+count)
# 2
