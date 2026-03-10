def sum(a,b):
    tong = a + b
    hieu = a - b
    return tong, hieu
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

tong, hieu = sum(a,b)
print("Tổng của a và b là: ", tong)
print("Hiệu của a và b là: ", hieu)