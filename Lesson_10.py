# Câu 1
def timSoNguyenTo(n):
    count = 0
    for x in range(n):   
        if x>1 and n>1 and n%x == 0:
            count = count + 1
    if count == 0:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải số nguyên tố")

# timSoNguyenTo(5)
# Câu 2: 
def tinhGiaiThua(n):
    result = 1
    for x in range(n):
        if x>0 and n>0:
            result = result*(x+1)
    print(result, "là giai thừa của", n)

# tinhGiaiThua(3)
# Câu 3:
def tinhTong(n):
    tong = 0
    for x in range(n):
        tong = tong+(x+1)
        print(x,n)
    print(tong,"là tong của", n)

# tinhTong(3)
# Câu 4:
def tinhTrungBinh(n):
    tong = 0
    # n = int(input("Nhập số n: "))
    for x in range(n):
        tong= tong+(x+1)
    trung_binh = tong/n
    print(trung_binh,"là trung binh của", n)

# tinhTrungBinh(4)
# Câu 5:
def demSolanXuatHien(n):
    count = 0
    for x in n:
        for y in n:
            if x == y:
                count = count + 1
        print("x:", x, "count :",count)
        count = 0

demSolanXuatHien([1,2,2,2,3,3,4,5,5,5])