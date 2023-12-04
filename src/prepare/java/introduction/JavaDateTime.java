package prepare.java.introduction;

import java.time.LocalDate;
import java.util.Scanner;

public class JavaDateTime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int month = scanner.nextInt();
        int day = scanner.nextInt();
        int year = scanner.nextInt();

        LocalDate date = LocalDate.of(year, month, day);
        String dayOfWeek = date.getDayOfWeek().toString().toUpperCase();

        System.out.println(dayOfWeek);

        scanner.close();
    }
}
