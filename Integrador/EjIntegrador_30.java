//
//Arbol AVL
//

// Implementación de un Nodo para el Árbol AVL
class Nodo {
    int valor, altura;
    Nodo izquierda, derecha;

    public Nodo(int valor) {
        this.valor = valor;
        this.altura = 1; // La altura de un nuevo nodo es 1
        this.izquierda = this.derecha = null;
    }
}

// Implementación de un Árbol AVL
public class ArbolAVL {
    private Nodo raiz;

    // Método para obtener la altura de un nodo
    private int obtenerAltura(Nodo nodo) {
        if (nodo == null) {
            return 0;
        }
        return nodo.altura;
    }

    // Método para obtener el máximo de dos números
    private int maximo(int a, int b) {
        return Math.max(a, b);
    }

    // Método para realizar una rotación simple a la derecha
    private Nodo rotacionDerecha(Nodo y) {
        Nodo x = y.izquierda;
        Nodo T2 = x.derecha;

        // Realizar la rotación
        x.derecha = y;
        y.izquierda = T2;

        // Actualizar alturas
        y.altura = maximo(obtenerAltura(y.izquierda), obtenerAltura(y.derecha)) + 1;
        x.altura = maximo(obtenerAltura(x.izquierda), obtenerAltura(x.derecha)) + 1;

        // Devolver la nueva raíz
        return x;
    }

    // Método para realizar una rotación simple a la izquierda
    private Nodo rotacionIzquierda(Nodo x) {
        Nodo y = x.derecha;
        Nodo T2 = y.izquierda;

        // Realizar la rotación
        y.izquierda = x;
        x.derecha = T2;

        // Actualizar alturas
        x.altura = maximo(obtenerAltura(x.izquierda), obtenerAltura(x.derecha)) + 1;
        y.altura = maximo(obtenerAltura(y.izquierda), obtenerAltura(y.derecha)) + 1;

        // Devolver la nueva raíz
        return y;
    }

    // Método para obtener el factor de equilibrio de un nodo
    private int obtenerFactorEquilibrio(Nodo nodo) {
        if (nodo == null) {
            return 0;
        }
        return obtenerAltura(nodo.izquierda) - obtenerAltura(nodo.derecha);
    }

    // Método para insertar un valor en el Árbol AVL
    public Nodo insertar(Nodo nodo, int valor) {
        // Paso 1: Realizar la inserción normal de un Árbol de Búsqueda Binario
        if (nodo == null) {
            return new Nodo(valor);
        }

        if (valor < nodo.valor) {
            nodo.izquierda = insertar(nodo.izquierda, valor);
        } else if (valor > nodo.valor) {
            nodo.derecha = insertar(nodo.derecha, valor);
        } else {
            // Valores duplicados no están permitidos en AVL, no realizar la inserción
            return nodo;
        }

        // Paso 2: Actualizar la altura del nodo actual
        nodo.altura = 1 + maximo(obtenerAltura(nodo.izquierda), obtenerAltura(nodo.derecha));

        // Paso 3: Obtener el factor de equilibrio del nodo actual
        int factorEquilibrio = obtenerFactorEquilibrio(nodo);

        // Paso 4: Realizar las rotaciones necesarias
        // Rotación a la izquierda-izquierda
        if (factorEquilibrio > 1 && valor < nodo.izquierda.valor) {
            return rotacionDerecha(nodo);
        }

        // Rotación a la derecha-derecha
        if (factorEquilibrio < -1 && valor > nodo.derecha.valor) {
            return rotacionIzquierda(nodo);
        }

        // Rotación a la izquierda-derecha
        if (factorEquilibrio > 1 && valor > nodo.izquierda.valor) {
            nodo.izquierda = rotacionIzquierda(nodo.izquierda);
            return rotacionDerecha(nodo);
        }

        // Rotación a la derecha-izquierda
        if (factorEquilibrio < -1 && valor < nodo.derecha.valor) {
            nodo.derecha = rotacionDerecha(nodo.derecha);
            return rotacionIzquierda(nodo);
        }

        // El nodo está equilibrado
        return nodo;
    }

    // Método para realizar una eliminación en un Árbol AVL
    public Nodo eliminar(Nodo nodo, int valor) {
        // Paso 1: Realizar la eliminación normal de un Árbol de Búsqueda Binario
        if (nodo == null) {
            return nodo;
        }

        if (valor < nodo.valor) {
            nodo.izquierda = eliminar(nodo.izquierda, valor);
        } else if (valor > nodo.valor) {
            nodo.derecha = eliminar(nodo.derecha, valor);
        } else {
            // Nodo con uno o ningún hijo
            if ((nodo.izquierda == null) || (nodo.derecha == null)) {
                Nodo temp = null;
                if (temp == nodo.izquierda) {
                    temp = nodo.derecha;
                } else {
                    temp = nodo.izquierda;
                }

                // No hay hijo
                if (temp == null) {
                    temp = nodo;
                    nodo = null;
                } else {
                    // Copiar el contenido del hijo no nulo
                    nodo = temp;
                }
            } else {
                // Nodo con dos hijos, obtener el sucesor inorden (menor valor en el subárbol derecho)
                Nodo temp = obtenerNodoMinimo(nodo.derecha);

                // Copiar los datos del sucesor inorden al nodo actual
                nodo.valor = temp.valor;

                // Eliminar el sucesor inorden
                nodo.derecha = eliminar(nodo.derecha, temp.valor);
            }
        }

        // Si el árbol tenía solo un nodo, no se necesita más la eliminación
        if (nodo == null) {
            return nodo;
        }

        // Paso 2: Actualizar la altura del nodo actual
        nodo.altura = 1 + maximo(obtenerAltura(nodo.izquierda), obtenerAltura(nodo.derecha));

        // Paso 3: Obtener el factor de equilibrio del nodo actual
        int factorEquilibrio = obtenerFactorEquilibrio(nodo);

        // Paso 4: Realizar las rotaciones necesarias
        // Rotación a la izquierda-izquierda
        if (factorEquilibrio > 1 && obtenerFactorEquilibrio(nodo.izquierda) >= 0) {
            return rotacionDerecha(nodo);
        }

        // Rotación a la derecha-derecha
        if (factorEquilibrio < -1 && obtenerFactorEquilibrio(nodo.derecha) <= 0) {
            return rotacionIzquierda(nodo);
        }

        // Rotación a la izquierda-derecha
        if (factorEquilibrio > 1 && obtenerFactorEquilibrio(nodo.izquierda) < 0) {
            nodo.izquierda = rotacionIzquierda(nodo.izquierda);
            return rotacionDerecha(nodo);
        }

        // Rotación a la derecha-izquierda
        if (factorEquilibrio < -1 && obtenerFactorEquilibrio(nodo.derecha) > 0) {
            nodo.derecha = rotacionDerecha(nodo.derecha);
            return rotacionIzquierda(nodo);
        }

        // El nodo está equilibrado
        return nodo;
    }

    // Método para obtener el nodo con el valor mínimo en un Árbol AVL
    private Nodo obtenerNodoMinimo(Nodo nodo) {
        Nodo actual = nodo;
        while (actual.izquierda != null) {
            actual = actual.izquierda;
        }
        return actual;
    }

    // Método para realizar un recorrido inorden en un Árbol AVL
    private void recorridoInorden(Nodo nodo) {
        if (nodo != null) {
            recorridoInorden(nodo.izquierda);
            System.out.print(nodo.valor + " ");
            recorridoInorden(nodo.derecha);
        }
    }

    // Método público para realizar un recorrido inorden en el Árbol AVL
    public void recorridoInorden() {
        recorridoInorden(raiz);
        System.out.println();
    }

    public static void main(String[] args) {
        ArbolAVL arbol = new ArbolAVL();

        // Insertar nodos de ejemplo en el Árbol AVL
        arbol.raiz = arbol.insertar(arbol.raiz, 10);
        arbol.raiz = arbol.insertar(arbol.raiz, 20);
        arbol.raiz = arbol.insertar(arbol.raiz, 30);
        arbol.raiz = arbol.insertar(arbol.raiz, 40);
        arbol.raiz = arbol.insertar(arbol.raiz, 50);
        arbol.raiz = arbol.insertar(arbol.raiz, 25);

        // Realizar un recorrido inorden en el Árbol AVL
        System.out.println("Árbol AVL después de la inserción:");
        arbol.recorridoInorden();

        // Eliminar un nodo del Árbol AVL
        arbol.raiz = arbol.eliminar(arbol.raiz, 30);

        // Realizar un recorrido inorden después de la eliminación
        System.out.println("Árbol AVL después de la eliminación:");
        arbol.recorridoInorden();
    }
}

