n = int(input())
b=input()
a = tuple(map(int, b.split(' ')))
print(hash(a))
