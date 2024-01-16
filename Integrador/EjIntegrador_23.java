//
//Cola circular de procesos
//

// Implementación de la clase Proceso y ColaCircularProcesos
class Proceso {
    int identificador;
    int duracion;

    public Proceso(int identificador, int duracion) {
        this.identificador = identificador;
        this.duracion = duracion;
    }

    // Otros métodos según sea necesario
}

public class ColaCircularProcesos {
    private Proceso[] procesos;
    private int frente;
    private int fin;
    private int capacidad;
    private int cantidad;

    public ColaCircularProcesos(int capacidad) {
        this.capacidad = capacidad;
        this.procesos = new Proceso[capacidad];
        this.frente = 0;
        this.fin = -1;
        this.cantidad = 0;
    }

    // Método para verificar si la cola está vacía
    public boolean estaVacia() {
        return cantidad == 0;
    }

    // Método para verificar si la cola está llena
    public boolean estaLlena() {
        return cantidad == capacidad;
    }

    // Método para encolar un proceso
    public void encolarProceso(int identificador, int duracion) {
        if (!estaLlena()) {
            fin = (fin + 1) % capacidad;
            procesos[fin] = new Proceso(identificador, duracion);
            cantidad++;
            System.out.println("Proceso encolado - ID: " + identificador + ", Duración: " + duracion);
            mostrarEstadoCola();
        } else {
            System.out.println("La cola de procesos está llena. No se puede encolar más.");
        }
    }

    // Método para ejecutar el siguiente proceso
    public void ejecutarSiguienteProceso() {
        if (!estaVacia()) {
            Proceso procesoEjecutado = procesos[frente];
            frente = (frente + 1) % capacidad;
            cantidad--;
            System.out.println("Proceso ejecutado - ID: " + procesoEjecutado.identificador +
                    ", Duración: " + procesoEjecutado.duracion);
            mostrarEstadoCola();
        } else {
            System.out.println("La cola de procesos está vacía. No hay procesos para ejecutar.");
        }
    }

    // Método para mostrar el estado actual de la cola de procesos
    public void mostrarEstadoCola() {
        System.out.print("Estado actual de la cola: [");
        for (int i = 0; i < cantidad; i++) {
            int indice = (frente + i) % capacidad;
            System.out.print("(ID: " + procesos[indice].identificador + ", Duración: " + procesos[indice].duracion + ") ");
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        ColaCircularProcesos colaProcesos = new ColaCircularProcesos(5);

        colaProcesos.encolarProceso(1, 10);
        colaProcesos.encolarProceso(2, 8);
        colaProcesos.ejecutarSiguienteProceso();
        colaProcesos.encolarProceso(3, 12);
        colaProcesos.ejecutarSiguienteProceso();
        colaProcesos.encolarProceso(4, 6);
        colaProcesos.encolarProceso(5, 15);
        colaProcesos.ejecutarSiguienteProceso();
        colaProcesos.ejecutarSiguienteProceso();
        colaProcesos.ejecutarSiguienteProceso();
        colaProcesos.ejecutarSiguienteProceso();
    }
}
