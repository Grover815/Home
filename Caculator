using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Caculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Input first number.");
            var first = Console.ReadLine();
            Console.WriteLine("Input Second Operator.");
            var second = Console.ReadLine();
            Console.WriteLine("Input a number corresponding to the operation.  1.Add  2.Subtract 3.Divide  4.Multiply   5.To the power of");
            var userResponse = Console.ReadLine();
            if (userResponse == "1")
            {
                int result = int.Parse(first) + int.Parse(second);
                Console.WriteLine(result);
            }
            if (userResponse == "2")
            {
                int result = int.Parse(first) - int.Parse(second);
                Console.WriteLine(result);
            }
            if (userResponse == "3")
            {
                int result = int.Parse(first) / int.Parse(second);
                Console.WriteLine(result);
            }
            if (userResponse == "4")
            {
                int result = int.Parse(first) * int.Parse(second);
                Console.WriteLine(result);
            }
            if (userResponse == "5")
            {
                var result = Math.Pow(int.Parse(first), int.Parse(second));
                Console.WriteLine(result);
            }
            Console.ReadKey();
        }
    }
}
