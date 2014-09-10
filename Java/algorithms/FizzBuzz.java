// Problem: Print all integers in a given range, but for multiples of 3 print
// "Fizz" and for multiples of 5 print "Buzz". For multiples of 3 and 5 print
// "FizzBuzz".

public class FizzBuzz
{
    public static void printRange(int range)
    {
        for (int i=0; i<=range; i++)
        {
            String output = "";
            if (i % 3 == 0)
                output += "Fizz";
            if (i % 5 == 0)
                output += "Buzz";
            if (output == "")
                output += Integer.toString(i);
            System.out.println(output);
        }
    }

    public static void main(String[] args)
    {
        int range = 100;
        printRange(range);
    }
}
