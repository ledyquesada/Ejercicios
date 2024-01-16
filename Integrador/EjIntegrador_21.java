//
//Cola de tareas pendientes
//

import java.util.PriorityQueue;

// Implementación de la clase Tarea y ColaTareasPendientes
class Tarea implements Comparable<Tarea> {
    String nombre;
    int prioridad;

    public Tarea(String nombre, int prioridad) {
        this.nombre = nombre;
        this.prioridad = prioridad;
    }

    @Override
    public int compareTo(Tarea otra) {
        // Ordenar por prioridad de manera ascendente
        return Integer.compare(this.prioridad, otra.prioridad);
    }

    // Otros métodos según sea necesario
}

public class ColaTareasPendientes {
    private PriorityQueue<Tarea> tareasPendientes;

    public ColaTareasPendientes() {
        this.tareasPendientes = new PriorityQueue<>();
    }

    // Método para agregar tareas a la cola
    public void agregarTarea(String nombre, int prioridad) {
        Tarea nuevaTarea = new Tarea(nombre, prioridad);
        tareasPendientes.add(nuevaTarea);
        System.out.println("Tarea agregada: " + nuevaTarea.nombre + " (Prioridad: " + nuevaTarea.prioridad + ")");
        mostrarTareasPendientes();
    }

    // Método para realizar la siguiente tarea en la cola
    public void realizarSiguienteTarea() {
        if (!tareasPendientes.isEmpty()) {
            Tarea siguienteTarea = tareasPendientes.poll();
            System.out.println("Realizando tarea: " + siguienteTarea.nombre + " (Prioridad: " + siguienteTarea.prioridad + ")");
            mostrarTareasPendientes();
        } else {
            System.out.println("No hay tareas pendientes.");
        }
    }

    // Método para mostrar las tareas pendientes
    public void mostrarTareasPendientes() {
        System.out.println("Tareas Pendientes: " + tareasPendientes);
    }

    public static void main(String[] args) {
        ColaTareasPendientes cola = new ColaTareasPendientes();

        cola.agregarTarea("Hacer informe", 2);
        cola.agregarTarea("Revisar correo", 1);
        cola.agregarTarea("Preparar presentación", 3);
        cola.realizarSiguienteTarea();
        cola.realizarSiguienteTarea();
        cola.realizarSiguienteTarea();
        cola.realizarSiguienteTarea();
    }
}
