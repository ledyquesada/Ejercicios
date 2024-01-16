//
// Lista doble de estudiantes
//
// Implementación de la clase Estudiante y ListaEstudiantes
class Estudiante {
    String nombre;
    int edad;
    double promedioCalificaciones;

    public Estudiante(String nombre, int edad, double promedioCalificaciones) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedioCalificaciones = promedioCalificaciones;
    }

    // Otros métodos según se quiera
}

class NodoEstudiante {
    Estudiante estudiante;
    NodoEstudiante siguiente;
    NodoEstudiante anterior;

    public NodoEstudiante(Estudiante estudiante) {
        this.estudiante = estudiante;
        this.siguiente = null;
        this.anterior = null;
    }
}

public class ListaEstudiantes {
    private NodoEstudiante cabeza;
    private NodoEstudiante cola;

    public ListaEstudiantes() {
        this.cabeza = null;
        this.cola = null;
    }

    // Método para agregar un estudiante al final de la lista
    public void agregarEstudiante(String nombre, int edad, double promedioCalificaciones) {
        Estudiante nuevoEstudiante = new Estudiante(nombre, edad, promedioCalificaciones);
        NodoEstudiante nuevoNodo = new NodoEstudiante(nuevoEstudiante);

        if (cabeza == null) {
            cabeza = nuevoNodo;
            cola = nuevoNodo;
        } else {
            nuevoNodo.anterior = cola;
            cola.siguiente = nuevoNodo;
            cola = nuevoNodo;
        }

        System.out.println("Estudiante agregado: " + nuevoEstudiante.nombre);
        mostrarEstudiantes();
    }

    // Método para eliminar un estudiante por nombre
    public void eliminarEstudiante(String nombre) {
        NodoEstudiante actual = cabeza;

        while (actual != null) {
            if (actual.estudiante.nombre.equals(nombre)) {
                if (actual.anterior != null) {
                    actual.anterior.siguiente = actual.siguiente;
                } else {
                    cabeza = actual.siguiente;
                }

                if (actual.siguiente != null) {
                    actual.siguiente.anterior = actual.anterior;
                } else {
                    cola = actual.anterior;
                }

                System.out.println("Estudiante eliminado: " + nombre);
                mostrarEstudiantes();
                return;
            }

            actual = actual.siguiente;
        }

        System.out.println("Estudiante no encontrado: " + nombre);
    }

    // Método para mostrar los estudiantes en la lista
    public void mostrarEstudiantes() {
        NodoEstudiante actual = cabeza;

        System.out.println("Estudiantes en la lista:");

        while (actual != null) {
            System.out.println("Nombre: " + actual.estudiante.nombre +
                    ", Edad: " + actual.estudiante.edad +
                    ", Promedio de Calificaciones: " + actual.estudiante.promedioCalificaciones);
            actual = actual.siguiente;
        }
    }

    public static void main(String[] args) {
        ListaEstudiantes lista = new ListaEstudiantes();

        lista.agregarEstudiante("Juan", 20, 85.5);
        lista.agregarEstudiante("Ana", 22, 90.0);
        lista.agregarEstudiante("Carlos", 21, 88.2);
        lista.eliminarEstudiante("Ana");
    }
}
