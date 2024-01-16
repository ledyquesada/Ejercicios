/**
*
* Lista Ligada de Personas
*/

// Implementación de la clase Nodo y ListaLigada
class Persona {
    String nombre;
    int edad;
    String país;

    public Persona(String nombre, int edad, String país) {
        this.nombre = nombre;
        this.edad = edad;
        this.país = país;
    }

    // Otros métodos, getters y setters según sea necesario
}

class Nodo {
    Persona persona;
    Nodo siguiente;

    public Nodo(Persona persona) {
        this.persona = persona;
        this.siguiente = null;
    }
}

class ListaLigada {
    Nodo cabeza;

    public ListaLigada() {
        this.cabeza = null;
    }

    public void agregarPersona(Persona persona) {
        Nodo nuevoNodo = new Nodo(persona);
        if (cabeza == null) {
            cabeza = nuevoNodo;
        } else {
            Nodo actual = cabeza;
            while (actual.siguiente != null) {
                actual = actual.siguiente;
            }
            actual.siguiente = nuevoNodo;
        }
    }

    public void mostrarPersonas() {
        Nodo actual = cabeza;
        while (actual != null) {
            System.out.println("Nombre: " + actual.persona.nombre +
                    ", Edad: " + actual.persona.edad +
                    ", País: " + actual.persona.país);
            actual = actual.siguiente;
        }
    }

    // Otros métodos según se quiera
}

public class Main {
    public static void main(String[] args) {
        ListaLigada listaPersonas = new ListaLigada();

        Persona persona1 = new Persona("Juan", 25, "Argentina");
        Persona persona2 = new Persona("Ana", 30, "España");
        Persona persona3 = new Persona("Carlos", 22, "México");

        listaPersonas.agregarPersona(persona1);
        listaPersonas.agregarPersona(persona2);
        listaPersonas.agregarPersona(persona3);

        listaPersonas.mostrarPersonas();
    }
}

