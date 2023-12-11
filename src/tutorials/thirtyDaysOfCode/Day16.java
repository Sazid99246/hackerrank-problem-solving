package tutorials.thirtyDaysOfCode;

import java.util.Scanner;

public class Day16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        scanner.close();

        try {
            int n = Integer.parseInt(s);
            System.out.println(n);
        } catch (NumberFormatException e) {
            System.out.println("Bad String");
        }
    }
}
