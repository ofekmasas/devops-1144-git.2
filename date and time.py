lines = ['2024-11-16 21:12:37.261978 yonatan\n', '2024-11-16 21:12:42.626825 halach lagan\n', '2024-11-16 21:12:49.404463 rahamim\n', '2024-11-16 21:12:51.246973 lo\n', '2024-11-16 21:12:53.101098 yada\n']
sum=0
for line in lines:
    words_in_line=len(line.split())
    sum +=words_in_line
print(sum)