import random

num = random.randint(1, 100)
print(num)

for i in range(1, 100):
    if i == num:
        print("This is answer " + str(i))

