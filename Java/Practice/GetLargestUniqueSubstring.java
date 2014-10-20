// Given string S, find max sized substring in which no duplicate chars exist.
import java.util.*;

public class GetLargestUniqueSubstring {
    public static String largest(String s) {
        if (s == "" || s.length() == 1) {
            return s;
        }
        List<Character> recorded = new ArrayList<Character>();
        String longest = "";
        for (int i = 0; i < s.length(); i++) {
            if (recorded.contains(s.charAt(i))) {
                StringBuilder new_str = new StringBuilder(recorded.size());
                for (Character c: recorded) {
                    new_str.append(c);
                }
                if (new_str.length() > longest.length()) {
                    longest = new_str.toString();
                }
                recorded.clear();
                recorded.add(s.charAt(i));
            }
            else {
                recorded.add(s.charAt(i));
            }
        }

        return longest;
    }

    public static void main(String[] args) {
        String s = "abccdefghiij";
        String result = largest(s);
        String testone = String.format("Input string: %s\nResult: %s\n",
                                        s, result);

        String s2 = "";
        String result2 = largest(s2);
        String testtwo = String.format("Input string: %s\nResult: %s\n",
                                        s2, result2);

        String s3 = "a";
        String result3 = largest(s3);
        String testthree = String.format("Input string: %s\nResult: %s\n",
                                          s3, result3);

        System.out.println(testone);
        System.out.println(testtwo);
        System.out.println(testthree);
    }
}
