/**
*
* Clase Genérica
*/

class ListaGenerica<T> {
    private java.util.List<T> elementos = new ArrayList<>();

    void agregarElemento(T elemento) {
        elementos.add(elemento);
    }

    void eliminarElemento(T elemento) {
        elementos.remove(elemento);
    }

    void mostrarElementos() {
        for (T elemento : elementos) {
            System.out.println(elemento);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ListaGenerica<String> listaString = new ListaGenerica<>();
        listaString.agregarElemento("Hola");
        listaString.agregarElemento("Mundo");
        listaString.mostrarElementos();

        ListaGenerica<Integer> listaInteger = new ListaGenerica<>();
        listaInteger.agregarElemento(42);
        listaInteger.agregarElemento(17);
        listaInteger.mostrarElementos();
    }
}
