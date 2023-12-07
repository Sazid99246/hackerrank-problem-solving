package tutorials.thirtyDaysOfCode;

import java.io.*;
import java.util.*;
import java.util.stream.*;
import static java.util.stream.Collectors.toList;

public class Day7 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        // Reading the line for the count of numbers, but not storing it as it's not
        // used.
        bufferedReader.readLine().trim();

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        Collections.reverse(arr);
        for (Integer i : arr) {
            System.out.print(i + " ");
        }

        bufferedReader.close();
    }
}
