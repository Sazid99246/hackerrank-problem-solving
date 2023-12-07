package tutorials.thirtyDaysOfCode;

import java.util.*;

public class Day6 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after the integer input

        for (int i = 0; i < T; i++) {
            String evenIndexed = "";
            String oddIndexed = "";
            String s = scanner.nextLine();
            char[] char1 = s.toCharArray();

            for (int j = 0; j < char1.length; j++) {
                if (j % 2 == 0) {
                    evenIndexed += char1[j];
                } else {
                    oddIndexed += char1[j];
                }
            }
            System.out.println(evenIndexed + " " + oddIndexed);
        }
        scanner.close();
    }
}
