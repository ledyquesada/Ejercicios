/**
 * Principios de POO
 */

class Persona {
    String nombre;
    int edad;

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void saludar() {
        System.out.println("Hola, soy " + nombre + " y tengo " + edad + " años.");
    }
}

public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 25);
        persona1.saludar();
    }
}
