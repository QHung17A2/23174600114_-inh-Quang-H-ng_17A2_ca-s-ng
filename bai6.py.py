mport math

# Nhập vào tọa độ của hai vector a và b
x_a = float(input("Nhập vào tọa độ x của vector a: "))
y_a = float(input("Nhập vào tọa độ y của vector a: "))
x_b = float(input("Nhập vào tọa độ x của vector b: "))
y_b = float(input("Nhập vào tọa độ y của vector b: "))

# Tính phép cộng vector a + b và phép trừ vector a - b
vector_sum = (x_a + x_b, y_a + y_b)
vector_difference = (x_a - x_b, y_a - y_b)

# Tính độ dài của vector a và vector b
length_a = math.sqrt(x_a ** 2 + y_a ** 2)
length_b = math.sqrt(x_b ** 2 + y_b ** 2)
# Tính cosin góc hợp giữa hai vector a và b
cosine_angle = (x_a * x_b + y_a * y_b) / (length_a * length_b)

# Hiển thị kết quả
print(f"Vector sum: {vector_sum}")
print(f"Vector difference: {vector_difference}")
print(f"Length of vector a: {round(length_a, 2)}")
print(f"Length of vector b: {round(length_b, 2)}")
print(f"Cosine of the angle between vectors a and b: {round(cosine_angle, 2)}")