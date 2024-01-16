/**
*
* Calculadora
*/

class Calculadora {
    private double resultado;

    Calculadora(double valorInicial) {
        this.resultado = valorInicial;
    }

    static double sumar(double a, double b) {
        return a + b;
    }

    static double restar(double a, double b) {
        return a - b;
    }

    static double multiplicar(double a, double b) {
        return a * b;
    }

    static double dividir(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Error: división por cero.");
            return Double.NaN;
        }
    }

    double getResultado() {
        return resultado;
    }

    void setResultado(double resultado) {
        this.resultado = resultado;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculadora calc = new Calculadora(0.0);

        calc.setResultado(Calculadora.sumar(calc.getResultado(), 5.0));
        calc.setResultado(Calculadora.multiplicar(calc.getResultado(), 3.0));

        System.out.println("Resultado final: " + calc.getResultado());
    }
}
