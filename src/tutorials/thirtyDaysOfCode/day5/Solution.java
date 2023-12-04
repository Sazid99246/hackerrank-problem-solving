package tutorials.thirtyDaysOfCode.day5;

import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        bufferedReader.close();

        for (int i = 1; i <= 10; i++) {
            System.out.println(String.format("%d x %d = %d", n, i, n * i));
        }
    }
}
