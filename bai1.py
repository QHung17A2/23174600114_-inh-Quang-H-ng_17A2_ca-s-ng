using System;

public class PhuongTrinhBacNhat
{
    public static void Main(string[] args)
    {
        // Nhập hệ số a và b
        Console.Write("Nhập hệ số a: ");
        double a = double.Parse(Console.ReadLine());
        Console.Write("Nhập hệ số b: ");
        double b = double.Parse(Console.ReadLine());

        // Giải phương trình và in ra kết quả
        if (a == 0)
        {
            if (b == 0)
            {
                Console.WriteLine("Phương trình vô số nghiệm");
            }
            else
            {
                Console.WriteLine("Phương trình vô nghiệm");
            }
        }
        else
        {
            double nghiem = -b / a;
            Console.WriteLine($"Phương trình có nghiệm duy nhất: x = {nghiem}");
        }
    }
}
