def tinh_chi_so_bmi(can_nang, chieu_cao):
  """
  Hàm tính chỉ số BMI

  Tham số:
    can_nang (float): Cân nặng (kg)
    chieu_cao (float): Chiều cao (mét)

  Trả về:
    float: Chỉ số BMI
  """
  return can_nang / chieu_cao ** 2

def phan_loai_bmi(chi_so_bmi):
  """
  Hàm phân loại chỉ số BMI

  Tham số:
    chi_so_bmi (float): Chỉ số BMI

  Trả về:
    str: Phân loại BMI
  """
  if chi_so_bmi < 18.5:
    return "Gầy"
  elif chi_so_bmi < 25:
    return "Bình thường"
  elif chi_so_bmi < 30:
    return "Hơi béo"
  else:
    return "Béo"

# Nhập cân nặng và chiều cao từ người dùng
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (mét): "))

# Tính chỉ số BMI
chi_so_bmi = tinh_chi_so_bmi(can_nang, chieu_cao)

# Phân loại chỉ số BMI
phan_loai = phan_loai_bmi(chi_so_bmi)

# In ra kết quả
print(f"Chỉ số BMI của bạn là: {chi_so_bmi:.2f}")
print(f"Phân loại BMI: {phan_loai}")
