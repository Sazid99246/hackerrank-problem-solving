package tutorials.thirtyDaysOfCode;

import java.util.*;

class Person {
    protected String firstName;
    protected String lastName;
    protected int idNumber;

    // Constructor
    Person(String firstName, String lastName, int identification) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.idNumber = identification;
    }

    // Print person data
    public void printPerson() {
        System.out.println(
                "Name: " + lastName + ", " + firstName
                        + "\nID: " + idNumber);
    }

}

class Student extends Person {

    private int[] testScores;
    char grade;

    /*
     * Class Constructor
     * 
     * @param firstName - A string denoting the Person's first name.
     * 
     * @param lastName - A string denoting the Person's last name.
     * 
     * @param id - An integer denoting the Person's ID number.
     * 
     * @param scores - An array of integers denoting the Person's test scores.
     */
    Student(String firstName, String lastName, int id, int[] scores) {
        super(firstName, lastName, id);
        this.testScores = scores;
    }

    /*
     * Method Name: calculate
     * 
     * @return A character denoting the grade.
     */
    char calculate() {
        int totalScore = 0;
        for (int i : testScores) {
            totalScore += i;
        }
        int score = totalScore / testScores.length;
        if (score < 40) {
            grade = 'T';
        } else if (score >= 40 && score < 55) {
            grade = 'D';
        } else if (score >= 55 && score < 70) {
            grade = 'P';
        } else if (score >= 70 && score < 80) {
            grade = 'A';
        } else if (score >= 80 && score < 90) {
            grade = 'E';
        } else if (score >= 90 && score <= 100) {
            grade = 'O';
        }
        return grade;
    }
}

public class Day12 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String firstName = scan.next();
        String lastName = scan.next();
        int id = scan.nextInt();
        int numScores = scan.nextInt();
        int[] testScores = new int[numScores];
        for (int i = 0; i < numScores; i++) {
            testScores[i] = scan.nextInt();
        }
        scan.close();

        Student s = new Student(firstName, lastName, id, testScores);
        s.printPerson();
        System.out.println("Grade: " + s.calculate());
    }
}