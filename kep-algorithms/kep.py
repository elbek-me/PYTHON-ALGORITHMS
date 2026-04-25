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


# n = int(input())
# a = list(map(int, input().split()))
# b = a.index(min(a))
# c = a.index(max(a))
# d = abs(c - b) - 1
# print(d)


# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(*a)



# n = int(input())
# if n <  2:  
#     print("No")
# else:
#     for son in range(2, int(n**0.5) + 1):
#         if n % son == 0:
#             print("No")
#             break
#     else:
#         print("Yes")





n = int(input())
a = list(map(int, input().split()))
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
c = 0
for d in b:
    if b[d] == 2:
        c += 1
print(c)


