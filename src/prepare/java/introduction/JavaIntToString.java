package prepare.java.introduction;

import java.util.*;

public class JavaIntToString {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();

        // Convert the integer to a String
        String s = String.valueOf(n);

        // Check if the conversion is correct
        if (n == Integer.parseInt(s)) {
            System.out.println("Good job");
        } else {
            System.out.println("Wrong answer.");
        }
    }
}
