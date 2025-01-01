print(type(5))
print(type(range(5)))

for num in range(5):
    print(num)

for val in "Maneesha":
    print(val)

count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
