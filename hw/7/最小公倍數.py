x = int(input("please input a number:"))
y = int(input("please input a number:"))
if x > y :
    c = x
else:
    c = y
m = x *y + 1
for k in range(c, m):
    if k % x == 0 and k % y == 0:
        print(k)
        break