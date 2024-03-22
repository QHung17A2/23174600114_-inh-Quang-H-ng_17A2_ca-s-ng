def vi_tri_tuong_doi(he_so_goc_1, he_so_tu_do_1, he_so_goc_2, he_so_tu_do_2):
  """
  Hàm xác định vị trí tương đối của hai đường thẳng

  Tham số:
    he_so_goc_1 (float): Hệ số góc của đường thẳng thứ nhất
    he_so_tu_do_1 (float): Hệ số tự do của đường thẳng thứ nhất
    he_so_goc_2 (float): Hệ số góc của đường thẳng thứ hai
    he_so_tu_do_2 (float): Hệ số tự do của đường thẳng thứ hai

  Trả về:
    str: Vị trí tương đối của hai đường thẳng
  """
  # So sánh hệ số góc
  if he_so_goc_1 == he_so_goc_2:
    # So sánh hệ số tự do
    if he_so_tu_do_1 == he_so_tu_do_2:
      return "Trùng nhau"
    else:
      return "Song song"
  else:
    return "Cắt nhau"

# Nhập thông số của hai đường thẳng
he_so_goc_1 = float(input("Nhập hệ số góc của đường thẳng thứ nhất: "))
he_so_tu_do_1 = float(input("Nhập hệ số tự do của đường thẳng thứ nhất: "))
he_so_goc_2 = float(input("Nhập hệ số góc của đường thẳng thứ hai: "))
he_so_tu_do_2 = float(input("Nhập hệ số tự do của đường thẳng thứ hai: "))

# Xác định vị trí tương đối
vi_tri = vi_tri_tuong_doi(he_so_goc_1, he_so_tu_do_1, he_so_goc_2, he_so_tu_do_2)

# In ra kết quả
print(f"Vị trí tương đối của hai đường thẳng là: {vi_tri}")
