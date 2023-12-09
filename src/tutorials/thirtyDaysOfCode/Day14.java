package tutorials.thirtyDaysOfCode;

import java.util.*;

class Difference {
    private int[] elements;
    public int maximumDifference;

    // Add your code here
    public Difference(int[] elements) {
        this.elements = elements;
    }

    void computeDifference() {
        int maxNum = elements[0];
        int minNum = maxNum;
        for (int i = 1; i < elements.length; i++) {
            if (elements[i] > maxNum) {
                maxNum = elements[i];
            }
            if (elements[i] < minNum) {
                minNum = elements[i];
            }
        }
        maximumDifference = Math.abs(maxNum - minNum);
    }

} // End of Difference class

public class Day14 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}