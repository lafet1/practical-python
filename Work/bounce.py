# bounce.py
#
# Exercise 1.5

height = 100
i = 0

while i <= 10:
    i += 1
    height *= 0.6
    height = round(height, ndigits=4)
    print(f'{i} {height}')
