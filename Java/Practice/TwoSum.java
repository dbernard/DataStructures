// You have an unsorted array, and you are given a value S.
// Find all pairs of elements in the array that add up to value S.
import java.util.*;

public class TwoSum {
    public static List<Integer[]> twosum(int S, int[] arr) {
        int start = 0;
        int end = arr.length - 1;
        Arrays.sort(arr);
        List<Integer[]> results = new ArrayList<Integer[]>();
        while (start < end) {
            if (arr[start] + arr[end] == S) {
                Integer[] pair = {arr[start], arr[end]};
                results.add(pair);
                end--;
            }
            else if (arr[start] + arr[end] > S) {
                // Decrement end ptr (we want lower values)
                end--;
            }
            else {
                // Increment start ptr (we want higher values)
                start++;
            }
        }

        return results;
    }

    public static void main(String[] args) {
        int S = 2;
        int[] arr = {0, 2, 1, 3, 1, 4};
        List<Integer[]> result = twosum(S, arr);

        for (Integer[] r: result) {
            System.out.println(Arrays.toString(r));
        }
    }
}
