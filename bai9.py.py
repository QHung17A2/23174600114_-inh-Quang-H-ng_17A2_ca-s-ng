import math

def f(x, z):
    return (x**2 * math.sin(z) + math.sqrt(x) * math.log(z) + math.exp(x) - math.log(z) + math.atan(x**2))

x = float(input("Nhập giá trị cho x: "))
z = float(input("Nhập giá trị cho z: "))

kết_quả = f(x, z)
print("f(", x, ",", z, ") =", round(kết_quả, 2))