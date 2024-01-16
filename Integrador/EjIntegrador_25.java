//
// Arbol binario de busqueda (ABB)
//


// Implementación de un Nodo para el Árbol Binario de Búsqueda (ABB)
class Nodo {
    int valor;
    Nodo izquierda, derecha;

    public Nodo(int valor) {
        this.valor = valor;
        this.izquierda = this.derecha = null;
    }
}

// Implementación del Árbol Binario de Búsqueda (ABB)
public class ArbolBinarioBusqueda {
    private Nodo raiz;

    public ArbolBinarioBusqueda() {
        this.raiz = null;
    }

    // Método para insertar un valor en el árbol
    private Nodo insertar(Nodo nodo, int valor) {
        if (nodo == null) {
            return new Nodo(valor);
        }

        if (valor < nodo.valor) {
            nodo.izquierda = insertar(nodo.izquierda, valor);
        } else if (valor > nodo.valor) {
            nodo.derecha = insertar(nodo.derecha, valor);
        }

        return nodo;
    }

    // Método público para insertar un valor en el árbol
    public void insertar(int valor) {
        raiz = insertar(raiz, valor);
    }

    // Método para realizar un recorrido en orden (in-order) del árbol
    private void recorridoInOrden(Nodo nodo) {
        if (nodo != null) {
            recorridoInOrden(nodo.izquierda);
            System.out.print(nodo.valor + " ");
            recorridoInOrden(nodo.derecha);
        }
    }

    // Método público para realizar un recorrido en orden del árbol
    public void recorridoInOrden() {
        recorridoInOrden(raiz);
    }

    public static void main(String[] args) {
        ArbolBinarioBusqueda abb = new ArbolBinarioBusqueda();

        // Insertar valores en el árbol
        abb.insertar(50);
        abb.insertar(30);
        abb.insertar(70);
        abb.insertar(20);
        abb.insertar(40);
        abb.insertar(60);
        abb.insertar(80);

        // Realizar un recorrido en orden para verificar la construcción del árbol
        System.out.println("Recorrido en orden del Árbol Binario de Búsqueda:");
        abb.recorridoInOrden();
    }
}
