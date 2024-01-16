//
//Camino de la raiz a una hoja
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

    // Método para encontrar el camino con la mayor suma desde la raíz hasta una hoja
    private void encontrarCaminoMayorSuma(Nodo nodo, int[] caminoActual, int nivel, int[] mejorCamino, int[] mejorSuma) {
        if (nodo == null) {
            return;
        }

        caminoActual[nivel] = nodo.valor;

        if (nodo.izquierda == null && nodo.derecha == null) {
            // Es una hoja, calcular la suma del camino actual
            int sumaCamino = 0;
            for (int i = 0; i <= nivel; i++) {
                sumaCamino += caminoActual[i];
            }

            // Actualizar el mejor camino y la mejor suma si es mayor
            if (sumaCamino > mejorSuma[0]) {
                mejorSuma[0] = sumaCamino;
                System.arraycopy(caminoActual, 0, mejorCamino, 0, nivel + 1);
            }
        }

        // Recorrer hacia la izquierda y derecha
        encontrarCaminoMayorSuma(nodo.izquierda, caminoActual, nivel + 1, mejorCamino, mejorSuma);
        encontrarCaminoMayorSuma(nodo.derecha, caminoActual, nivel + 1, mejorCamino, mejorSuma);
    }

    // Método público para obtener el camino con la mayor suma desde la raíz hasta una hoja
    public int[] obtenerCaminoMayorSuma() {
        if (raiz == null) {
            return new int[0]; // Árbol vacío, retorno un arreglo vacío
        }

        int[] caminoActual = new int[100]; // Tamaño máximo para el camino (ajustar según sea necesario)
        int[] mejorCamino = new int[100];
        int[] mejorSuma = {Integer.MIN_VALUE}; // Inicializar con el valor mínimo posible de un entero

        encontrarCaminoMayorSuma(raiz, caminoActual, 0, mejorCamino, mejorSuma);

        return mejorCamino;
    }

    public static void main(String[] args) {
        ArbolBinario arbol = new ArbolBinario();

        // Construir el árbol de ejemplo
        arbol.raiz = new Nodo(10);
        arbol.raiz.izquierda = new Nodo(2);
        arbol.raiz.derecha = new Nodo(10);
        arbol.raiz.izquierda.izquierda = new Nodo(20);
        arbol.raiz.izquierda.derecha = new Nodo(1);
        arbol.raiz.derecha.derecha = new Nodo(-25);
        arbol.raiz.derecha.derecha.izquierda = new Nodo(3);
        arbol.raiz.derecha.derecha.derecha = new Nodo(4);

        // Calcular y mostrar el camino con la mayor suma desde la raíz hasta una hoja
        int[] caminoMayorSuma = arbol.obtenerCaminoMayorSuma();
        System.out.println("Camino con la Mayor Suma desde la Raíz hasta una Hoja:");
        for (int valor : caminoMayorSuma) {
            System.out.print(valor + " ");
        }
    }
}


