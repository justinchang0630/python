'''
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:
'''
邊a= input(邊a)
邊b= input(邊b)
邊c= input(邊c)
if (邊a+邊b>=邊c),(邊b+邊c>=邊a),(邊c+邊a>=邊b):
    print(邊a+邊b+邊c)
else print(no)





