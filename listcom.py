a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# another way:  print([x for x in a if x % 2 == 0])
b = list(filter(lambda x: x % 2 == 0, a))
print(b)
