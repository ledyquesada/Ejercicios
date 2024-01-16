//
// Altura del arbol
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

    // Método para calcular la altura de un árbol
    private int calcularAltura(Nodo nodo) {
        if (nodo == null) {
            return 0;
        } else {
            int alturaIzquierda = calcularAltura(nodo.izquierda);
            int alturaDerecha = calcularAltura(nodo.derecha);

            // La altura del árbol es la máxima entre la altura de la izquierda y la altura de la derecha, más 1
            return Math.max(alturaIzquierda, alturaDerecha) + 1;
        }
    }

    // Método público para obtener la altura del árbol
    public int obtenerAltura() {
        return calcularAltura(raiz);
    }

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();

        // Construir el árbol de ejemplo
        arbol.raiz = new Nodo(1);
        arbol.raiz.izquierda = new Nodo(2);
        arbol.raiz.derecha = new Nodo(3);
        arbol.raiz.izquierda.izquierda = new Nodo(4);
        arbol.raiz.izquierda.derecha = new Nodo(5);

        // Calcular y mostrar la altura del árbol
        System.out.println("Altura del Árbol Binario: " + arbol.obtenerAltura());
    }
}
