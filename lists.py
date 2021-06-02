#4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

more_then = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]
print(more_then)

#5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([i for i in src if src.count(i) == 1])

