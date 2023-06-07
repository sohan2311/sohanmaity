import java.util.Scanner;

public class java1 {
    public static Double getCircumference(Double radius) {
        return 2 * 3.14 * radius;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Double r = sc.nextDouble();
        System.out.println(getCircumference(r));
    }
}

// Give me a code in java to find the area of a circle ?

