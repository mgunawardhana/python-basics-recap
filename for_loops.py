
for number in range(1,4):
    print("Attempt ", number, number * ".")

for number in range(1,10,2):
    print("Attempt ", number, number * ".")

"""
FOR ELSE ---------------------------------------------------------------------------------------------------------------
"""

count = 0
for number in range(1, 5):
    if count == 3:
        print("Your account is temporarily blocked!")
        break
    else:
        print("Try ", number)
        count += 1
else:
    print("Attempted 3 times Failed!")

"""
NESTED LOOPS -----------------------------------------------------------------------------------------------------------
"""

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")














