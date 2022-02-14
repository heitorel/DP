import java.util.Scanner;

public class Main {
    private static int criptografia(char letra) {
        return switch (letra) {
            case 'G', 'Q', 'a', 'k', 'u' -> 0;
            case 'I', 'S', 'b', 'l', 'v' -> 1;
            case 'E', 'O', 'Y', 'c', 'm', 'w' -> 2;
            case 'F', 'P', 'Z', 'd', 'n', 'x' -> 3;
            case 'J', 'T', 'e', 'o', 'y' -> 4;
            case 'D', 'N', 'X', 'f', 'p', 'z' -> 5;
            case 'A', 'K', 'U', 'g', 'q' -> 6;
            case 'C', 'M', 'W', 'h', 'r' -> 7;
            case 'B', 'L', 'V', 'i', 's' -> 8;
            case 'H', 'R', 'j', 't' -> 9;
            default -> -1;
        };
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = Integer.parseInt(sc.nextLine());
        char[] frase = new char[12];

        while (N > 0) {
            String string = sc.nextLine().replace(" ", "");
            if (string.length() > 12) {
                frase = string.substring(0, 12).toCharArray();
            } else {
                frase = string.toCharArray();
            }

            for (char c : frase) {
                System.out.print(criptografia(c));
            }
            System.out.println();
            N--;
        }
    }
}