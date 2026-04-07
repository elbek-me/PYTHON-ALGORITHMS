n = int(input())
b = 0 
for a in range(1, n + 1):
    if a % 3 == 0 or a % 5 == 0 or a % 7 == 0:
        b += a
print(b)
