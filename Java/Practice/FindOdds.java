import java.util.Set;
import java.util.Arrays;
import java.util.HashSet;

public class FindOdds {
    public static Set odds(Integer[] arr) {
        Set<Integer> hs = new HashSet<Integer>();
        for (int i: arr) {
            if (hs.contains(i)) {
                hs.remove(i);
            }
            else {
                hs.add(i);
            }
        }

        return hs;
    }

    public static void main(String[] args) {
        // 2 appears an odd number of times
        Integer[] arr = {1, 2, 1, 3, 2, 3, 2};

        Set result = odds(arr);
        System.out.println(result);
    }
}
