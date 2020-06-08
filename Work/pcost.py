# pcost.py
#
# Exercise 1.27

overall_cost = 0

with open('Data/portfolio.csv', 'rt') as file:
    next(file)
    for line in file:
        _, no_shares, price = line.split(',')
        overall_cost += int(no_shares) * float(price)

print(f'Total cost {overall_cost}')
