import java.util.ArrayList;
import java.lang.StringBuilder;



public class GetSubsets
{
    // This (below) is the "meat". This recursively builds the subsets by saving
    // off the previous results and adding the new results in.
    public static ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> set, int index)
    {
        ArrayList<ArrayList<Integer>> all_subsets;
        if (set.size() == index) // Base Case - add empty set
        {
            all_subsets = new ArrayList<ArrayList<Integer>>();
            all_subsets.add(new ArrayList<Integer>());
        }
        else
        {
            all_subsets = subsets(set, index + 1);
            int item = set.get(index);
            ArrayList<ArrayList<Integer>> more =
                new ArrayList<ArrayList<Integer>>();
            for (ArrayList<Integer> subset : all_subsets)
            {
                ArrayList<Integer> new_sub = new ArrayList<Integer>();
                new_sub.addAll(subset);
                new_sub.add(item);
                more.add(new_sub);
            }
            all_subsets.addAll(more);
        }
        return all_subsets;
    }

    public static void main(String[] args)
    {
        ArrayList<Integer> set = new ArrayList<Integer>();
        int number_of_subsets = 0;

        int n;
        for (n = 0; n <= 5; n++)
            set.add(n);

        ArrayList<ArrayList<Integer>> all_subsets = subsets(set, 0);

        // NOTE: String Builders are slow.
        StringBuilder sb = new StringBuilder();

        for (ArrayList<Integer> sub : all_subsets)
        {
            sb.append("[");
            for (Integer i : sub)
            {
                sb.append(String.valueOf(i) + ", ");
            }
            sb.append("]\n");
            number_of_subsets++;
        }

        double expected_subsets = Math.pow(2, n);

        System.out.print(sb.toString());
        System.out.println("-----------------------------");
        System.out.println(" - Should be 2^n possible subsets:");
        System.out.format(" - The value of 'n' here is %d%n", n);
        System.out.format(" - 2^%d == %.0f%n", n, expected_subsets);
        if (expected_subsets == number_of_subsets)
            System.out.println(" - PASS:");
        else
            System.out.println(" - FAIL:");
        System.out.format(" - Expected %.0f subsets, found %d subsets%n",
                expected_subsets, number_of_subsets);
    }
}
