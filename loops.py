letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

items = (0, "a")
#we can unpack like this
index, item = items

print(items) # (0, 'a')

# if we use enumerate it will be read only
# step 1
# for letter in enumerate(letters):
    #print(letter) Output - (0, 'a'), (1, 'b')
    #print(letter[0], letter[1]) o b, 1 b

#Step 2
for index, letter in enumerate(letters):
    print(index, letter)  # - >  0 a, 1 b, 2 c