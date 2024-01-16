//
// Suma de nodos
//

// Implementación de un Nodo para el Árbol Binario
class Nodo {
    int valor;
    Nodo izquierda, derecha;

    public Nodo(int valor) {
        this.valor = valor;
        this.izquierda = this.derecha = null;
    }
}

// Implementación de un Árbol Binario
public class ArbolBinario {
    private Nodo raiz;

    public ArbolBinario() {
        this.raiz = null;
    }

    // Método para calcular la suma de nodos en un nivel dado del árbol
    private int calcularSumaNodosEnNivel(Nodo nodo, int nivelDeseado, int nivelActual) {
        if (nodo == null) {
            return 0;
        }

        if (nivelActual == nivelDeseado) {
            return nodo.valor;
        }

        int sumaIzquierda = calcularSumaNodosEnNivel(nodo.izquierda, nivelDeseado, nivelActual + 1);
        int sumaDerecha = calcularSumaNodosEnNivel(nodo.derecha, nivelDeseado, nivelActual + 1);

        return sumaIzquierda + sumaDerecha;
    }

    // Método público para obtener la suma de nodos en un nivel dado del árbol
    public int obtenerSumaNodosEnNivel(int nivelDeseado) {
        return calcularSumaNodosEnNivel(raiz, nivelDeseado, 0);
    }

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();

        // Construir el árbol de ejemplo
        arbol.raiz = new Nodo(1);
        arbol.raiz.izquierda = new Nodo(2);
        arbol.raiz.derecha = new Nodo(3);
        arbol.raiz.izquierda.izquierda = new Nodo(4);
        arbol.raiz.izquierda.derecha = new Nodo(5);

        // Calcular y mostrar la suma de nodos en un nivel dado del árbol
        int nivelDeseado = 2;
        System.out.println("Suma de nodos en el nivel " + nivelDeseado + ": " + arbol.obtenerSumaNodosEnNivel(nivelDeseado));
    }
}

