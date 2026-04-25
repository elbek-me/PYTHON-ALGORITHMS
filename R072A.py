n_str = input().strip()
juft_yigindi = 0    
toq_yigindi = 0
for i in range(len(n_str)):
    raqam = int(n_str[i])
    if i % 2 == 0:
        toq_yigindi += raqam
    else:
        juft_yigindi += raqam
if (toq_yigindi - juft_yigindi) % 11 == 0:
    print("Yes")
else:
    print("No")
