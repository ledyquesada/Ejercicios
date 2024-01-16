//
//Pila de palabras palíndromas
//

import java.util.Stack;

public class PilaPalindromas {
    private Stack<String> pilaPalabras;

    public PilaPalindromas() {
        this.pilaPalabras = new Stack<>();
    }

    // Método para verificar si una palabra es palíndroma
    public boolean esPalindroma(String palabra) {
        // Eliminar espacios y convertir a minúsculas para una comparación más precisa
        String palabraSinEspacios = palabra.replaceAll("\\s", "").toLowerCase();
        int longitud = palabraSinEspacios.length();
        
        // Crear una pila temporal para almacenar la mitad de la palabra
        Stack<Character> pilaMitadPalabra = new Stack<>();
        
        // Empujar la primera mitad de la palabra a la pila
        for (int i = 0; i < longitud / 2; i++) {
            pilaMitadPalabra.push(palabraSinEspacios.charAt(i));
        }

        // Verificar si la longitud es impar y omitir el carácter central
        if (longitud % 2 != 0) {
            pilaMitadPalabra.pop();
        }

        // Comparar la segunda mitad de la palabra con la pila
        for (int i = longitud / 2; i < longitud; i++) {
            if (palabraSinEspacios.charAt(i) != pilaMitadPalabra.pop()) {
                return false;
            }
        }

        return true;
    }

    // Método para agregar una palabra a la pila
    public void agregarPalabra(String palabra) {
        pilaPalabras.push(palabra);
        System.out.println("Palabra agregada: " + palabra);
        mostrarEstadoPila();
    }

    // Método para mostrar el estado actual de la pila de palabras
    public void mostrarEstadoPila() {
        System.out.print("Estado actual de la pila: [");
        for (String palabra : pilaPalabras) {
            System.out.print(palabra + " ");
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        PilaPalindromas pilaPalindromas = new PilaPalindromas();

        pilaPalindromas.agregarPalabra("radar");
        pilaPalindromas.agregarPalabra("oso");
        pilaPalindromas.agregarPalabra("java");
        System.out.println("¿Es 'java' palíndroma? " + pilaPalindromas.esPalindroma("java"));
        pilaPalindromas.agregarPalabra("reconocer");
        System.out.println("¿Es 'reconocer' palíndroma? " + pilaPalindromas.esPalindroma("reconocer"));
    }
}

