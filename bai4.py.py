# Nhập thông tin của hình chóp tứ giác
cạnh_đáy = float(input("Nhập độ dài cạnh đáy của hình chóp tứ giác: "))
chieu_cao = float(input("Nhập chiều cao của hình chóp tứ giác: "))

# Tính diện tích xung quanh, diện tích toàn phần và thể tích của hình chóp tứ giác
surface_area = 4 * cạnh_đáy * (cạnh_đáy ** 2) ** 0.5 + 4 * cạnh_đáy * chieu_cao
total_area = cạnh_đáy ** 2 + surface_area
volume = (cạnh_đáy ** 2 * chieu_cao) / 3

# Hiển thị kết quả
print(f"Diện tích xung quanh: {round(surface_area, 2)}")
print(f"Diện tích toàn phần: {round(total_area, 2)}")
print(f"Thể tích: {round(volume, 2)}")