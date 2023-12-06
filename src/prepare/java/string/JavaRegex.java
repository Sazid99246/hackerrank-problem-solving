package prepare.java.string;

import java.util.Scanner;

public class JavaRegex {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNext()) {
            String IP = in.next();
            new MyRegex();
            System.out.println(IP.matches(MyRegex.pattern));
        }
        in.close();
    }
}

// Write your code here
/**
 * MyRegex
 */
class MyRegex {

    static String zeroTo255 = "(\\d{1,2}|(0|1)\\d{2}|2[0-4]\\d|25[0-5])";
    public static String pattern = zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255 + "\\." + zeroTo255;

}
