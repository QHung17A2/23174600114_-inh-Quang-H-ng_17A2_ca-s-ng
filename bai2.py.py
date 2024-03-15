@@ -0,0 +1,31 @@
def xac_suat_bi_do(tong_so_bi, so_bi_do):
    return so_bi_do / tong_so_bi

def xac_suat_it_nhat_mot_bi_xanh(tong_so_bi, so_bi_xanh):
    return 1 - (xac_suat_bi_do(tong_so_bi, so_bi_xanh) ** 0)

def xac_suat_chinh_xac_hai_bi_vang(tong_so_bi, so_bi_vang):
    return (so_bi_vang / tong_so_bi) * ((so_bi_vang - 1) / (tong_so_bi - 1))

def main():
    try:
        tong_so_bi = 50
        so_bi_do = 20
        so_bi_xanh = 15
        so_bi_vang = 15

        so_lan_rut = int(input("Nhập số lượng viên bi muốn rút ra từ hộp mà không nhìn: "))


        prob_bi_do = xac_suat_bi_do(tong_so_bi, so_bi_do)
        prob_bi_xanh = xac_suat_it_nhat_mot_bi_xanh(tong_so_bi, so_bi_xanh)
        prob_bi_vang = xac_suat_chinh_xac_hai_bi_vang(tong_so_bi, so_bi_vang)

        print("1. Xác suất để rút ra tất cả bi đỏ:", round(prob_bi_do ** so_lan_rut, 4))
        print("2. Xác suất để rút ra ít nhất một viên bi xanh:", round(prob_bi_xanh ** so_lan_rut, 4))
        print("3. Xác suất để rút ra đúng hai viên bi vàng:", round(prob_bi_vang, 4))
    except ValueError:
        print("Vui lòng nhập số lượng viên bi là một số nguyên.")

if __name__ == "__main__":
    main()