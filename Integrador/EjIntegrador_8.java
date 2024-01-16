/**
*
* Division
*/

class Calculadora {
    double dividir(double numerador, double denominador) throws ArithmeticException {
        if (denominador == 0) {
            throw new ArithmeticException("No se puede dividir por cero.");
        }
        return numerador / denominador;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();

        try {
            double resultado = calculadora.dividir(10.0, 2.0);
            System.out.println("Resultado: " + resultado);

            // Intento de división por cero
            resultado = calculadora.dividir(5.0, 0.0);
            System.out.println("Resultado: " + resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
