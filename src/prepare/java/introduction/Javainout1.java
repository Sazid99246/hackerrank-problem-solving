package prepare.java.introduction;

import java.util.*;

public class Javainout1 {

    public static void main(String[] args) {
        /*
         * Enter your code here. Read input from STDIN. Print output to STDOUT. Your
         * class should be named Solution.
         */
        Scanner scanner = new Scanner(System.in);

        int n1 = Integer.valueOf(scanner.nextLine());
        int n2 = Integer.valueOf(scanner.nextLine());
        int n3 = Integer.valueOf(scanner.nextLine());

        System.out.println(n1);
        System.out.println(n2);
        System.out.println(n3);
        scanner.close();
    }
}
