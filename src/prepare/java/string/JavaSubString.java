package prepare.java.string;

import java.util.*;

public class JavaSubString {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String S = in.next();
        int start = in.nextInt();
        int end = in.nextInt();
        in.close();

        String res = S.substring(start, end);
        System.out.println(res);
    }
}
