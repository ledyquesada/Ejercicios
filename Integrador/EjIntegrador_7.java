/**
*
* Validador
*/

import java.util.Scanner;

class Validador {
    static boolean validarRango(int numero, int minimo, int maximo) {
        return numero >= minimo && numero <= maximo;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese un número entre 0 y 100: ");
        int numero = scanner.nextInt();

        if (Validador.validarRango(numero, 0, 100)) {
            System.out.println("Número válido.");
        } else {
            System.out.println("Número fuera de rango.");
        }
    }
}
