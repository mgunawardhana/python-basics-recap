count = 0

for number in range(1, 11):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")