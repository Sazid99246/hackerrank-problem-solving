package tutorials.thirtyDaysOfCode;

import java.util.Scanner;

public class Day25 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input the number of test cases
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            // Input the number to be tested for primality
            int n = scanner.nextInt();

            // Check if the number is prime and print the result
            if (isPrime(n)) {
                System.out.println("Prime");
            } else {
                System.out.println("Not prime");
            }
        }

        scanner.close();
    }

    // Function to check if a number is prime
    private static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }

        // Check for divisibility from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false; // If divisible, not a prime number
            }
        }

        return true; // If not divisible by any number, it's a prime number
    }
}
