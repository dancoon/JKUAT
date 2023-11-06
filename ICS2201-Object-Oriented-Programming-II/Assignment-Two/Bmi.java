import java.util.*;

public class Bmi {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int normalBmi = 24;
        // int height;
        // int weight;

        // int myBmi = weight / (height * height);        
        int myBmi = scanner.nextInt();
        scanner.close();
        if (myBmi >= normalBmi) {
            System.out.println("Normal BMI");
        } else {
            System.out.println("Moderate BMI");
        }
    }
}
