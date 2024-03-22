from math import sqrt

def vi_tri_tuong_doi(he_so_goc, he_so_tu_do, toa_do_tam_x, toa_do_tam_y, ban_kinh):
  """
  Hàm kiểm tra vị trí tương đối giữa đường thẳng và đường tròn

  Tham số:
    he_so_goc (float): Hệ số góc của đường thẳng
    he_so_tu_do (float): Hệ số tự do của đường thẳng
    toa_do_tam_x (float): Tọa độ x của tâm đường tròn
    toa_do_tam_y (float): Tọa độ y của tâm đường tròn
    ban_kinh (float): Bán kính đường tròn

  Trả về:
    str: Vị trí tương đối giữa đường thẳng và đường tròn
  """

  # Tính khoảng cách từ tâm đường tròn đến đường thẳng
  d = abs(he_so_goc * toa_do_tam_x - toa_do_tam_y + he_so_tu_do) / sqrt(he_so_goc ** 2 + 1)

  # So sánh khoảng cách với bán kính
  if d > ban_kinh:
    return "Nằm ngoài"
  elif d == ban_kinh:
    return "Tiếp xúc"
  elif d < ban_kinh:
    # Tính điểm giao nhau
    x1, y1 = toa_do_tam_x, toa_do_tam_y
    x2, y2 = x1 - he_so_goc * d, y1 + d
    x3, y3 = x1 + he_so_goc * d, y1 - d

    # Kiểm tra điểm giao nhau nằm trong hay ngoài khoảng [-ban_kinh, ban_kinh]
    if (x1 - ban_kinh <= x2 <= x1 + ban_kinh) or (x1 - ban_kinh <= x3 <= x1 + ban_kinh):
      return "Cắt nhau"
    else:
      return "Nằm trong"

# Nhập thông số của đường thẳng và đường tròn
he_so_goc = float(input("Nhập hệ số góc của đường thẳng: "))
he_so_tu_do = float(input("Nhập hệ số tự do của đường thẳng: "))
toa_do_tam_x = float(input("Nhập tọa độ x của tâm đường tròn: "))
toa_do_tam_y = float(input("Nhập tọa độ y của tâm đường tròn: "))
ban_kinh = float(input("Nhập bán kính đường tròn: "))

# Kiểm tra vị trí tương đối
vi_tri = vi_tri_tuong_doi(he_so_goc, he_so_tu_do, toa_do_tam_x, toa_do_tam_y, ban_kinh)

# In ra kết quả
print(f"Vị trí tương đối giữa đường thẳng và đường tròn là: {vi_tri}")
