// This is a Java implementation of the "wiggle problem" - given an array,
// arrange it such that alternate elements are large and small.
//
// NOTE: This is not the most efficient answer, but simply an excuse for me to
// practice Java syntax again after a long period of absence.
import java.util.Arrays;


class Wiggle
{
    public static void main(String args[])
    {
        int[] arr = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 };
        // Sort the array (for cases where it was given to us out of order)
        Arrays.sort(arr);
        //System.out.println(Arrays.toString(arr));

        // Split the array in two. Make sure the first half (lower values)
        // receives the greater number of values if we have an odd sized array
        int split = arr.length/2;
        int[] first = Arrays.copyOfRange(arr, 0, split);
        System.out.println(Arrays.toString(first));
        int[] second = Arrays.copyOfRange(arr, split, arr.length);
        System.out.println(Arrays.toString(second));

        int[] result = new int[arr.length];

        int count = 0;
        for (int i=0; i < arr.length/2; i++)
        {
            result[count] = first[i];
            count ++;
            result[count] = second[i];
            count ++;
        }

        // Takes care of the case where we have an uneven split (odd sized
        // array)
        if (split * 2 < arr.length)
        {
            result[count] = second[second.length-1];
        }

        System.out.println(Arrays.toString(result));
    }
}
