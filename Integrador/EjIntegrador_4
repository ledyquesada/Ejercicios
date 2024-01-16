/**
*
* Animal
*/

class Animal {
    String nombre;
    int edad;

    Animal(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    void hacerSonido() {
        System.out.println("El animal hace un sonido.");
    }
}

class Perro extends Animal {
    Perro(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    void hacerSonido() {
        System.out.println("El perro ladra.");
    }
}

class Gato extends Animal {
    Gato(String nombre, int edad) {
        super(nombre, edad);
    }

    @Override
    void hacerSonido() {
        System.out.println("El gato maulla.");
    }
}

public class Main {
    public static void main(String[] args) {
        Perro perro1 = new Perro("Max", 3);
        Gato gato1 = new Gato("Whiskers", 2);

        perro1.hacerSonido();
        gato1.hacerSonido();
    }
}
