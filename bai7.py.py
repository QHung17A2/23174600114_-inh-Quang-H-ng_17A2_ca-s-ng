def giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2):

    determinant = a1 * b2 - a2 * b1


    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return x, y

def main():

    a1 = float(input("Nhập hệ số a1: "))
    b1 = float(input("Nhập hệ số b1: "))
    c1 = float(input("Nhập hệ số c1: "))
    a2 = float(input("Nhập hệ số a2: "))
    b2 = float(input("Nhập hệ số b2: "))
    c2 = float(input("Nhập hệ số c2: "))


    x, y = giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2)


    print(f"Giải hệ phương trình: x = {x:.2f}, y = {y:.2f}")

if __name__ == "__main__":
    main()