#Cau 1:

# x = int(input('Hay nhap mot so'))
# if x >0:
#     print (x, "la so duong")
# elif x<0:
#     print (x, "là so am")

#Cau 2

# x = float(input('Hay nhap diem trung binh: '))
# if x < 4:
#     print (x, "Xếp loại yếu")
# elif 4 <= x < 6.5:
#     print (x, "Xếp loại trung bình")
# elif 6.5 <= x < 8:
#     print (x, "Xếp loại khá")
# else:
#     print (x, "Xếp loại giỏi " )

# Cau 3:

# a = float(input("Mời bạn nhập hệ số a: "))
# while True:
#     if a == 0:
#         a = float(input("Số a phải khác 0. Mời nhập lại số a: "))
#     else:
#         break
# b = float(input("Mời bạn nhập hệ số b: "))
# c = float(input("Mời bạn nhập hệ số c: "))
# D = b*2 - 4*a*c
# if D < 0:
#     print("Phương trình vô nghiệm")
# elif D == 0:
#     print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
# else:
#     print("Phương trình có hai nghiệm phân biệt:")
#     print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
#     print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) ) 

# Cau 4
# a1 = float(input("Mời bạn nhập hệ số a1: "))
# b1 = float(input("Mời bạn nhập hệ số b1: "))
# c1 = float(input("Mời bạn nhập hệ số c1: "))
# a2 = float(input("Mời bạn nhập hệ số a2: "))
# b2 = float(input("Mời bạn nhập hệ số b2: "))
# c2 = float(input("Mời bạn nhập hệ số c2: "))
# D=a1*b2-a2*b1 
# Dx=c1*b2-c2*b1
# Dy=a1*c2-a2*c1 
# if D==0:
#     if Dx+Dy==0:
#         print("HE PHUONG TRINH CO VO SO NGHIEM")
#     else:
#         print("HE PHUONG TRINH VO NGHIEM")
# else:
#     x=Dx/D 
#     y=Dy/D 
#     print("NGHIEM CUA HE PHUONG TRINH LA:" '\n'
#     "X=",round(x,3),'\n'
#     "Y=",round(y,3),'\n')

# Cau 5:

Day = int(input("Nhập Ngày: "))
Month = int(input("Nhập Tháng: "))
Year = int(input("Nhập Năm: "))

Yesterday = (Day-1), Month, Year
if Day == 1 and Month in [1,3,5,7,8,10,12]:
    print(31,Month -1, Year)
else:
    print(Yesterday)

Tomorrow = (Day+1), Month, Year
if Day == 31 and Month in [1,3,5,7,8,10,12]:
    print(1,Month+1, Year)
elif Day == 30 and Month not in [1,3,5,7,8,10,12]:
    print(1,Month+1, Year)
else:
    print(Tomorrow)
