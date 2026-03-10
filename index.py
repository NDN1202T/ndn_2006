def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Không thể chia cho 0"
    return a / b


a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

print("Tích:", nhan(a, b))
print("Thương:", chia(a, b))