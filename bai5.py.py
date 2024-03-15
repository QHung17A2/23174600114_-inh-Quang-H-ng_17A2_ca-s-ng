def tinh_tien_dien(gio_su_dung, hieu_dien_ap, cuong_do_dien):
    # Công suất của máy lọc không khí (W)
    cong_suat = hieu_dien_ap * cuong_do_dien

    # Số kWh sử dụng
    so_kwh = (cong_suat * gio_su_dung) / 1000

    # Tổng số tiền điện phải trả
    tien_dien = so_kwh * 5000

    return tien_dien

def main():
    # Nhập số giờ sử dụng máy lọc không khí từ người dùng
    gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))

    # Thông số của máy lọc không khí
    hieu_dien_ap = 220  # V
    cuong_do_dien = 1.5  # A

    # Tính tổng số tiền điện phải trả
    tien_dien = tinh_tien_dien(gio_su_dung, hieu_dien_ap, cuong_do_dien)

    # Hiển thị tổng số tiền điện phải trả
    print(f"Số tiền điện phải trả cho việc sử dụng máy lọc không khí trong {gio_su_dung} giờ là: {tien_dien} đồng.")

if __name__ == "__main__":
    main()