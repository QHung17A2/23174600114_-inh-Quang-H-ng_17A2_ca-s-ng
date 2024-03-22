
public class DocSoNguyen
{
    public static void Main(string[] args)
    {
        // Nhập số nguyên
        Console.Write("Nhập số nguyên có ba chữ số: ");
        int soNguyen = int.Parse(Console.ReadLine());

        // Kiểm tra tính hợp lệ
        if (soNguyen < 100 || soNguyen > 999)
        {
            Console.WriteLine("Số nguyên không hợp lệ!");
            return;
        }

        // Lấy các chữ số
        int hangTram = soNguyen / 100;
        int hangChuc = (soNguyen % 100) / 10;
        int hangDonVi = soNguyen % 10;

        // Chuỗi lưu cách đọc
        string cachDoc = "";

        // Đọc hàng trăm
        if (hangTram > 0)
        {
            cachDoc += DocSoDon(hangTram) + " hundred";
        }

        // Đọc hàng chục và hàng đơn vị
        if (hangChuc == 1)
        {
            switch (hangDonVi)
            {
                case 0:
                    cachDoc += " ten";
                    break;
                case 1:
                    cachDoc += " eleven";
                    break;
                case 2:
                    cachDoc += " twelve";
                    break;
                case 3:
                    cachDoc += " thirteen";
                    break;
                case 4:
                    cachDoc += " fourteen";
                    break;
                case 5:
                    cachDoc += " fifteen";
                    break;
                case 6:
                    cachDoc += " sixteen";
                    break;
                case 7:
                    cachDoc += " seventeen";
                    break;
                case 8:
                    cachDoc += " eighteen";
                    break;
                case 9:
                    cachDoc += " nineteen";
                    break;
            }
        }
        else
        {
            if (hangChuc > 0)
            {
                cachDoc += DocSoDon(hangChuc) + " ";
            }
            if (hangDonVi > 0)
            {
                cachDoc += DocSoDon(hangDonVi);
            }
        }

        // In ra kết quả
        Console.WriteLine($"Cách đọc của số {soNguyen} là: {cachDoc}");
    }

    static string DocSoDon(int so)
    {
        switch (so)
        {
            case 1:
                return "one";
            case 2:
                return "two";
            case 3:
                return "three";
            case 4:
                return "four";
            case 5:
                return "five";
            case 6:
                return "six";
            case 7:
                return "seven";
            case 8:
                return "eight";
            case 9:
                return "nine";
            default:
                return "";
        }
    }
}
