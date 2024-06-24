prices = [57.80, 97.00, 48.45, 32.12, 59.01, 67, 83.27, 88.94, 93, 71.40, 47.00, 49.08, 54, 66.66, 24.99, 78, 67.50, 29.70, 13, 31.05]
print(id(prices))
prices.sort()
print(prices)
print(id(prices))
aft = 0
bef = 0
for i in range(len(prices)):
    bef = prices[i] // 1
    print(f"{int(bef)} грн", end='.')
    aft = prices[i] % 1
    aft = aft * 100 // 1
    aft = int(aft)
    if aft < 10:
        print(f'{aft:02} коп.', end=', ')
    else:
        print(f'{int(aft)} коп.', end=', ')

print(end='\n')

prices.reverse()
newprices = []
for i in prices:
    newprices.append(i)
print(id(newprices))

aft = 0
bef = 0
for i in range(len(prices)):
    bef = prices[i] // 1
    print(f"{int(bef)} грн", end='.')
    aft = prices[i] % 1
    aft = aft * 100 // 1
    aft = int(aft)
    if aft < 10:
        print(f'{aft:02} коп.', end=', ')
    else:
        print(f'{int(aft)} коп.', end=', ')

print(end='\n')
aft = 0
bef = 0
i = 5
while i != 0:
    bef = prices[i] // 1
    print(f"{int(bef)} грн", end='.')
    aft = prices[i] % 1
    aft = aft * 100 // 1
    aft = int(aft)
    if aft < 10:
        print(f'{aft:02} коп.', end=', ')
    else:
        print(f'{int(aft)} коп.', end=', ')
    i -= 1
