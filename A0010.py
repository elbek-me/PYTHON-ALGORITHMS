a, b, c = map(int, input().split())
d = 0
for n in [a, b, c]:
    if n % 2 == 0:
        d += n // 2  
    else:
        d += (n // 2) + 1  
print(d)