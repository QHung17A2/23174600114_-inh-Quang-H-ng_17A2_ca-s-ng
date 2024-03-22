def tim_so_lon_thu_hai(a, b, c):
  """
  Hàm tìm số lớn thứ hai trong ba số nguyên

  Tham số:
    a (int): Số nguyên thứ nhất
    b (int): Số nguyên thứ hai
    c (int): Số nguyên thứ ba

  Trả về:
    int: Số lớn thứ hai
  """
  # Tìm số lớn nhất và số nhỏ nhất
  so_lon_nhat = max(a, b, c)
  so_nho_nhat = min(a, b, c)

  # Tìm số lớn thứ hai
  if a != so_lon_nhat and a != so_nho_nhat:
    so_lon_thu_hai = a
  elif b != so_lon_nhat and b != so_nho_nhat:
    so_lon_thu_hai = b
  else:
    so_lon_thu_hai = c

  return so_lon_thu_hai

# Nhập ba số nguyên từ bàn phím
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

# Tìm số lớn thứ hai
so_lon_thu_hai = tim_so_lon_thu_hai(a, b, c)

# In ra kết quả
print(f"Số lớn thứ hai là: {so_lon_thu_hai}")
