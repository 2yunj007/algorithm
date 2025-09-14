import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            char[] ans = sc.next().toCharArray();

            int score = 0;
            int temp = 0;

            for (char a : ans) {
                if (a == 'O') {
                    score += ++temp;
                }
                else {
                    temp = 0;
                }
            }

            System.out.println(score);
        }
    }
}
