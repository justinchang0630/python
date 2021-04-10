import random
r = int(input())
ans = random.randint(1, r)
for i in range(1,r+1):
    print(i)
    if (i == ans):
       print('ya')
       break