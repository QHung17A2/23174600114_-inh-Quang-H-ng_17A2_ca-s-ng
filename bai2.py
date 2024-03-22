def lay_chu_so_hang_nghin(so_nguyen):
  """
  Hàm lấy chữ số hàng nghìn của số nguyên

  Tham số:
    so_nguyen (int): Số nguyên cần lấy chữ số hàng nghìn

  Trả về:
    int: Chữ số hàng nghìn của số nguyên, hoặc 0 nếu không có
  """
  if so_nguyen < 1000:
    return 0
  else:
    return so_nguyen // 1000 % 10

# Nhập số nguyên từ người dùng
so_nguyen = int(input("Nhập số nguyên: "))

# Lấy chữ số hàng nghìn và xuất ra kết quả
chu_so_hang_nghin = lay_chu_so_hang_nghin(so_nguyen)
print(f"Chữ số hàng nghìn của {so_nguyen} là: {chu_so_hang_nghin}")
