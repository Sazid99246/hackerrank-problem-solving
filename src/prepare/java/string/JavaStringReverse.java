package prepare.java.string;

import java.util.*;

public class JavaStringReverse {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        sc.close();
        /* Enter your code here. Print output to STDOUT. */
        StringBuilder input = new StringBuilder();
        input.append(A);
        input.reverse();
        String output = input.toString();
        if (A.equals(output)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
