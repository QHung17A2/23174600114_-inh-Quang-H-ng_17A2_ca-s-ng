def main():
  # Danh sách thể loại phim
  the_loai_phim = ["Hành động", "Kinh dị", "Tình cảm", "Hài hước", "Hoạt hình"]

  # Lựa chọn thể loại phim
  while True:
    print("Chọn thể loại phim:")
    for i, the_loai in enumerate(the_loai_phim):
      print(f"{i + 1}. {the_loai}")
    lua_chon_the_loai = int(input())
    if 1 <= lua_chon_the_loai <= len(the_loai_phim):
      break
    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

  # Lựa chọn thời gian xem phim
  while True:
    print("Chọn thời gian xem phim:")
    print("1. Sáng")
    print("2. Trưa")
    print("3. Chiều")
    print("4. Tối")
    lua_chon_thoi_gian = int(input())
    if 1 <= lua_chon_thoi_gian <= 4:
      break
    print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

  # Xác định thời gian chiếu phim
  thoi_gian_chieu_phim = ""
  if the_loai_phim[lua_chon_the_loai - 1] == "Tình cảm":
    if lua_chon_thoi_gian == 4:
      thoi_gian_chieu_phim = "Tối"
    else:
      thoi_gian_chieu_phim = "Không có suất chiếu"
  elif the_loai_phim[lua_chon_the_loai - 1] == "Hoạt hình":
    if lua_chon_thoi_gian <= 2:
      thoi_gian_chieu_phim = "Sáng/Trưa"
    else:
      thoi_gian_chieu_phim = "Không có suất chiếu"
  elif the_loai_phim[lua_chon_the_loai - 1] == "Kinh dị":
    if lua_chon_thoi_gian == 4:
      thoi_gian_chieu_phim = "Tối"
    else:
      thoi_gian_chieu_phim = "Không có suất chiếu"
  else:
    thoi_gian_chieu_phim = ["Sáng", "Trưa", "Chiều", "Tối"][lua_chon_thoi_gian - 1]

  # In thông báo
  print(f"Bạn đã chọn xem phim {the_loai_phim[lua_chon_the_loai - 1]} vào lúc {thoi_gian_chieu_phim}")

if __name__ == "__main__":
  main()
