import java.util.Arrays;
import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int k = sc.nextInt();

        for (int i = 1; i <= k; i++) {
            int n = sc.nextInt();
            int[] scores = new int[n];

            for (int j = 0; j < n; j++) {
                scores[j] = sc.nextInt();
            }

            Arrays.sort(scores);

            int maxGap = 0;
            for (int j = 1; j < n; j++) {
                 maxGap = Math.max(maxGap, scores[j] - scores[j - 1]);
            }

            System.out.println("Class " + i);
            System.out.println("Max " + scores[n - 1] + ", Min " + scores[0] + ", Largest gap " + maxGap);
        }
    }
}
