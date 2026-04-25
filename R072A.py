n_str = input().strip()
juft_yigindi = 0    
toq_yigindi = 0
for i in range(len(n_str)):
    raqam = int(n_str[i])
    if raqam % 2 == 0:
        juft_yigindi += raqam   
    else:
        toq_yigindi += raqam

if (toq_yigindi - juft_yigindi) % 11 == 0:
    print("Yes")
else:
    print("No")