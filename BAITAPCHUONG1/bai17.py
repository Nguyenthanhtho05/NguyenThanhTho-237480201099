n = int(input("nhap so nguyen duong n la: "))

tong_le = sum(i for i in range(1, n, 2))
tong_chan = sum(i for i in range(2, n, 2))

print("Tong cac so le nho hon n la:", tong_le)
print("Tong cac so chan nho hon n la:", tong_chan)