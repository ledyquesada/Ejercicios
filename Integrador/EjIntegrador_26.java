//
// Recorrido Post_Orden invertido
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

    // Método para realizar un recorrido post-orden en el árbol y mostrar los nodos en orden inverso
    private void recorridoPostOrdenInvertido(Nodo nodo) {
        if (nodo != null) {
            recorridoPostOrdenInvertido(nodo.derecha);
            recorridoPostOrdenInvertido(nodo.izquierda);
            System.out.print(nodo.valor + " ");
        }
    }

    // Método público para realizar el recorrido post-orden invertido
    public void recorridoPostOrdenInvertido() {
        recorridoPostOrdenInvertido(raiz);
    }

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();

        // Construir el árbol de ejemplo
        arbol.raiz = new Nodo(1);
        arbol.raiz.izquierda = new Nodo(2);
        arbol.raiz.derecha = new Nodo(3);
        arbol.raiz.izquierda.izquierda = new Nodo(4);
        arbol.raiz.izquierda.derecha = new Nodo(5);

        // Realizar el recorrido post-orden invertido
        System.out.println("Recorrido Post-Orden Invertido:");
        arbol.recorridoPostOrdenInvertido();
    }
}
