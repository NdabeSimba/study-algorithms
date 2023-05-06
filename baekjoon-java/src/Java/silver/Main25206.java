package Java.silver;

import java.util.Scanner;

public class Main25206 {
    public static void main(String[] args) {

        String[][] grade = new String[20][3];
        Scanner sc = new Scanner(System.in);

        double creditSum = 0;

        for (int i = 0; i  < 20; i++) {
            for (int j = 0; j < 3; j++){
                grade[i][j] = sc.nextLine();
                System.out.println(grade[i][j]);
            }
            
        }

    }

}
