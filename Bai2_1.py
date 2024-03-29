import math
#check xem 1 số có phải số nguyên tố không
def check(a):
    for i in range (2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
        else :
            return True
#kiểm tra xem 1 số có phải số đối xứng không
def doixung(a):
    b = 0
    while ( a > 0):
        b = b*10 + a % 10
        a //= 10
    return b
def kiemtra(a):
    flag = a - doixung(a)
    if flag == 0:
        return True
    else :
        return False
#bài 2_1_3
s = int(input("Nhập vào số nguyên s: "))
e = int(input("Nhập vào số nguyên e: "))
while s > e or e >= 100000000:
    print('SỐ không thỏa mãn yêu cầu!')
    s = int(input("Nhập lại s: "))
    e = int(input("Nhập lại e: "))

sum = 0
for i in range (s, e + 1):
    if check(i) and kiemtra(i):
       sum += i
print("Tổng các số thỏa mãn là: ", sum)
      
