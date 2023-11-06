public class SumTwoDArray {
    public static void main(String[] args) {
        int[][] myArray = {
            {1, 2, 3, 4},
            {5, 6, 7, 8},
            {9, 10, 11, 12},
            {13, 14, 15, 16},
        };
        int sum = 0;

        for (int i = 0; i < myArray.length; i++) {
            for (int j = 0; j < myArray[i].length; j++) {
                sum += myArray[i][j];
            }
        }
        System.out.println("The sum of my 2-D array is: " + sum);
    }
}