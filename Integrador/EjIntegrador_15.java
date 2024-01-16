/**
*
* Archivos y Excepciones
*/

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class SumaNumeros {
    static double sumarNumeros(String ruta) throws IOException {
        double suma = 0;

        try (BufferedReader lector = new BufferedReader(new FileReader(ruta))) {
            String linea;

            while ((linea = lector.readLine()) != null) {
                suma += Double.parseDouble(linea);
            }
        }

        return suma;
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            double resultado = SumaNumeros.sumarNumeros("numeros.txt");
            System.out.println("Suma de números: " + resultado);
        } catch (IOException | NumberFormatException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
