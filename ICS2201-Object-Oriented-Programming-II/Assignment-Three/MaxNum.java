/*
    Find the maximum number in array
*/

public class MaxNum {
    static int maximumNum(int[] arr) {
        int max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] > max) max = arr[i];
        }
        return max;
    }

    public static void main(String[] args) {
        int[] myArray = {30, 70, 20, 60, 60, 15};
        System.out.println("The maximum number in the array is: " + maximumNum(myArray));
    }
}
