package prepare.java.introduction;

import java.util.*;

public class Javainout2 {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */

        Scanner scanner = new Scanner(System.in);

        int n = Integer.valueOf(scanner.nextLine());
        double d = Double.valueOf(scanner.nextLine());
        String s = String.valueOf(scanner.nextLine());

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + n);

        scanner.close();
    }
}
