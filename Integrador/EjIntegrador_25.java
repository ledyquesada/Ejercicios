//
// Arbol binario de busqueda (ABB)
//
// Implementación del Nodo de un Árbol Binario
class NodoABB {
    int valor;
    NodoABB izquierdo, derecho;

    public NodoABB(int valor) {
        this.valor = valor;
        izquierdo = derecho = null;
    }
}

// Implementación del Árbol Binario de Búsqueda
class ArbolBinarioBusqueda {
    NodoABB raiz;

    public ArbolBinarioBusqueda() {
        raiz = null;
    }

    // Método para insertar un valor en el ABB
    public void insertar(int valor) {
        raiz = insertarRec(raiz, valor);
    }

    private NodoABB insertarRec(NodoABB nodo, int valor) {
        if (nodo == null) {
            return new NodoABB(valor);
        }

        if (valor < nodo.valor) {
            nodo.izquierdo = insertarRec(nodo.izquierdo, valor);
        } else if (valor > nodo.valor) {
            nodo.derecho = insertarRec(nodo.derecho, valor);
        }

        return nodo;
    }

    // Método para recorrer el árbol en orden (in-order)
    public void imprimirInOrden() {
        imprimirInOrdenRec(raiz);
        System.out.println();
    }

    private void imprimirInOrdenRec(NodoABB nodo) {
        if (nodo != null) {
            imprimirInOrdenRec(nodo.izquierdo);
            System.out.print(nodo.valor + " ");
            imprimirInOrdenRec(nodo.derecho);
        }
    }

    public static void main(String[] args) {
        ArbolBinarioBusqueda abb = new ArbolBinarioBusqueda();
        int[] numeros = {50, 30, 70, 20, 40, 60, 80};

        for (int numero : numeros) {
            abb.insertar(numero);
        }

        System.out.println("Árbol Binario de Búsqueda (In-Orden):");
        abb.imprimirInOrden();
    }
}
