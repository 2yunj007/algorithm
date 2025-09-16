import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String vowels = "aeiou";

        while (sc.hasNext()) {
            String word = sc.next();
            if (word.equals("end")) break;

            if (isAcceptable(word, vowels)) {
                System.out.println("<" + word + "> is acceptable.");
            } else {
                System.out.println("<" + word + "> is not acceptable.");
            }
        }

        sc.close();
    }

    private static boolean isAcceptable(String word, String vowels) {
        boolean hasVowel = false;
        int consecVowel = 0;
        int consecCons = 0;
        char prev = 0;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            boolean isVowel = vowels.indexOf(c) != -1;

            if (isVowel) {
                hasVowel = true;
                consecVowel++;
                consecCons = 0;
            } else {
                consecCons++;
                consecVowel = 0;
            }

            if (consecVowel == 3 || consecCons == 3) return false;

            if (i > 0 && c == prev && c != 'e' && c != 'o') return false;

            prev = c;
        }

        return hasVowel;
    }
}
