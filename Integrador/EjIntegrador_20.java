//
//Pila operaciones matematicas
//

import java.util.Stack;

// Implementación de la clase PilaOperaciones
public class PilaOperaciones {
    private Stack<String> operaciones;

    public PilaOperaciones() {
        this.operaciones = new Stack<>();
    }

    // Método para realizar operaciones y mostrar el estado actual
    public void realizarOperacion(String operacion) {
        if (esOperacionValida(operacion)) {
            operaciones.push(operacion);
            System.out.println("Operación realizada: " + operacion);
            mostrarEstado();
        } else {
            System.out.println("Operación no válida: " + operacion);
        }
    }

    // Método para mostrar el estado actual de la pila
    public void mostrarEstado() {
        System.out.println("Estado actual de la pila: " + operaciones);
    }

    // Método privado para verificar si la operación es válida
    private boolean esOperacionValida(String operacion) {
        // En este ejemplo, se consideran válidas las operaciones de suma, resta y multiplicación
        return operacion.equals("+") || operacion.equals("-") || operacion.equals("*");
    }

    public static void main(String[] args) {
        PilaOperaciones pila = new PilaOperaciones();

        pila.realizarOperacion("+");
        pila.realizarOperacion("-");
        pila.realizarOperacion("*");
        pila.realizarOperacion("/");
        pila.realizarOperacion("+");

        // La salida esperada mostrará el estado actual de la pila después de cada operación válida
    }
}

