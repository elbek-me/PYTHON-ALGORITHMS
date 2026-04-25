# n = int(input())
# a = input().split()
# a.reverse()
# print(*(a))



# n = int(input())
# a = list(map(int, input().split()))
# a = a[0]
# for i in range(1, n):
#     if a[i] < a:
#         a = a[i]
# print(a)




# n = int(input())
# a = list(map(int, input().split()))
# b = min(a)
# index = a.index(b) + 1
# print(index)


n = int(input())
a = list(map(int, input().split()))
b = a.index(min(a))
c = a.index(max(a))
d = abs(c - b) - 1
print(d)


# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(*a)


PYTHON-ALGORITHMS 





