# Bạn đầu tư một số tiền ban đầu
tiền_đầu_tư_ban_đầu = 10000

# Lãi suất hàng năm
lãi_suất_hàng_năm = 0.06

# Tính toán số tiền sẽ có sau 5 năm
tiền_sau_5_năm = tiền_đầu_tư_ban_đầu * (1 + lãi_suất_hàng_năm) ** 5

# Tính toán số tiền sẽ có sau 10 năm
tiền_sau_10_năm = tiền_đầu_tư_ban_đầu * (1 + lãi_suất_hàng_năm) ** 10

# Tính toán tỷ lệ tăng trưởng của số tiền bạn sẽ có sau 10 năm so với số tiền bạn
# sẽ có sau 5 năm
tỷ_lệ_tăng_trưởng = (tiền_sau_10_năm - tiền_sau_5_năm) / tiền_sau_5_năm

# In kết quả của tất cả các tính toán trên ra màn hình
print("Số tiền sau 5 năm: {:.2f}".format(tiền_sau_5_năm))
print("Số tiền sau 10 năm: {:.2f}".format(tiền_sau_10_năm))
print("Tỷ lệ tăng trưởng: {:.2%}".format(tỷ_lệ_tăng_trưởng))