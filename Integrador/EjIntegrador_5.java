/**
*
* Biblioteca
*/

class Publicacion {
    private String titulo;
    private boolean prestado;

    Publicacion(String titulo) {
        this.titulo = titulo;
        this.prestado = false;
    }

    void prestar() {
        if (!prestado) {
            prestado = true;
            System.out.println(titulo + " ha sido prestado.");
        } else {
            System.out.println(titulo + " ya está prestado.");
        }
    }
}

class Libro extends Publicacion {
    Libro(String titulo) {
        super(titulo);
    }
}

class Revista extends Publicacion {
    Revista(String titulo) {
        super(titulo);
    }
}

public class Main {
    public static void main(String[] args) {
        Libro libro = new Libro("Java Programming");
        Revista revista = new Revista("Tech Magazine");

        libro.prestar();
        libro.prestar();  // Intento de prestar nuevamente

        revista.prestar();
    }
}
