v=float(input("nhap diem van: "))
t=float(input("nhap diem toan: "))
a=float(input("nhap diem tieng anh: "))

tb=(v+t+a)/3
if(tb>=8.5 and t>=9 and t>v and t>a):
    print("Dau chuyen toan")
if(tb>=8.5 and v>=9 and v>a):
    print("Dau chuyen van")
if(tb>=8.5 and a>=8.0):
    print("Dau chuyen tieng anh")
if(tb>=8.5):
    print("Dau chuyen tin hoc")
else:
    print("khong dau")