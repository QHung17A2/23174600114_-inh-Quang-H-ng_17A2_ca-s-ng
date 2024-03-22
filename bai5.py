def tinh_tien_ve_xem_phim(so_luong_nguoi):
  """
  Hàm tính tiền vé xem phim

  Tham số:
    so_luong_nguoi (int): Số lượng người mua vé

  Trả về:
    float: Tổng số tiền phải trả
  """
  gia_ve_mot_nguoi = 120000

  # Tính tổng tiền trước khi giảm giá
  tong_tien = so_luong_nguoi * gia_ve_mot_nguoi

  # Áp dụng giảm giá
  if so_luong_nguoi >= 10:
    phan_tram_giam_gia = 20
  elif so_luong_nguoi >= 4:
    phan_tram_giam_gia = 10
  elif so_luong_nguoi >= 2:
    phan_tram_giam_gia = 5
  else:
    phan_tram_giam_gia = 0

  # Tính số tiền giảm giá
  tien_giam_gia = tong_tien * phan_tram_giam_gia / 100

  # Tính tổng số tiền phải trả
  so_tien_phai_tra = tong_tien - tien_giam_gia

  return so_tien_phai_tra

# Nhập số lượng người từ bàn phím
so_luong_nguoi = int(input("Nhập số lượng người: "))

# Tính tổng số tiền phải trả
tong_tien = tinh_tien_ve_xem_phim(so_luong_nguoi)

# In ra kết quả
print(f"Tổng số tiền phải trả là: {tong_tien:,.0f} đồng")
