"""
Topic:請使用input輸入要印制的箭頭大小，最小為2行
印出箭頭

e.g.
Please in row: 3
   *
  ***
 *****
   *
   *
   *
"""
row= int(input('how many rows do you want:'))
for x in range(row):
    show1 = (' ' * (row -x-1)) + ('*' * ( x * 2 +1))
    print (show1)
for y in range(row):
    show2 = (' ' * (row-1)) + ('*')
    print (show2)
