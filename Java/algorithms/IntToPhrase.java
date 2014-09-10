import java.util.ArrayList;

public class IntToPhrase
{
    // NOTE: This solution is not optimal. We can do this better and cleaner by
    // modding/dividing the integer in question by "notable" values to include
    // "bigs" and "tens", etc.
    public static String space = " ";

    public static String[] digits = {"one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"};

    public static String[] teens = {"eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

    public static String[] tens = {"ten", "twenty", "thirty", "fourty", "fifty",
        "sixty", "seventy", "eighty", "ninety"};

    public static String[] bigs = {"hundred", "thousand", "million", "billion"};

    public static String convert(int num)
    {
        String result = "";
        // Break number up into ones, tens, hundreds, thousands, etc.
        ArrayList<Integer> n = new ArrayList<Integer>();
        int length = 0;
        while (num > 0)
        {
            n.add(0, num % 10);
            num = num/10;
            length++;
        }

        int index = 0;

        while (length > 0)
        {
            if (length == 4)
            {
                // Thousands
                result += digits[n.get(index)-1] + space + bigs[1] + space;
            }
            else if (length == 3)
            {
                // Hundreds
                result += digits[n.get(index)-1] + space + bigs[0] + space;
            }
            else if (length == 2)
            {
                // Tens / Teens
                if (n.get(index) == 1 && n.get(index+1) != 0)
                {
                    // Teens - increment index again too to skip last digit.
                    result += teens[n.get(index)-1] + space;
                    index++;
                }
                else
                {
                    // Tens
                    result += tens[n.get(index)-1] + space;
                }
            }
            else if (length == 1)
            {
                // Digits
                if (n.get(index) != 0)
                {
                    result += digits[n.get(index)-1] + space;
                }
            }
            length--;
            index++;
        }

        return result;
    }

    public static void main(String[] args)
    {
        int number = 9999;
        String phrase = convert(number);
        System.out.println(phrase);
    }
}
