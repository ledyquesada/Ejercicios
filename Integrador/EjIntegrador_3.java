/**
*
* Encapsulamiento persona
*/

class Persona {
    private String nombre;
    private int edad;

    Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void saludar() {
        System.out.println("Hola, soy " + nombre + " y tengo " + edad + " años.");
    }

    // Métodos getter y setter
    String getNombre() {
        return nombre;
    }

    void setNombre(String nombre) {
        this.nombre = nombre;
    }

    int getEdad() {
        return edad;
    }

    void setEdad(int edad) {
        this.edad = edad;
    }
}

public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan", 25);
        persona1.saludar();

        // Uso de métodos getter y setter
        persona1.setNombre("Carlos");
        persona1.setEdad(30);
        System.out.println("Nuevo nombre: " + persona1.getNombre());
        System.out.println("Nueva edad: " + persona1.getEdad());
    }
}
