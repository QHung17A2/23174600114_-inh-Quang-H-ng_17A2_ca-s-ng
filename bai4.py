def danh_gia_diem(diem):
  """
  Hàm đánh giá điểm bài kiểm tra

  Tham số:
    diem (float): Điểm bài kiểm tra

  Trả về:
    str: Thông báo đánh giá điểm
  """
  if diem < 0 or diem > 10:
    return "Điểm không hợp lệ!"
  elif diem < 5:
    return "Điểm kém"
  elif diem < 7:
    return "Điểm trung bình"
  elif diem < 8.5:
    return "Điểm khá"
  else:
    return "Điểm tốt"

# Nhập điểm từ người dùng
diem = float(input("Nhập điểm bài kiểm tra: "))

# Đánh giá điểm và in ra thông báo
thong_bao = danh_gia_diem(diem)
print(thong_bao)
