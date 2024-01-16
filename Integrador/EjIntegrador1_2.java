/**
 *
 * Herencia estudiante
 */

class Estudiante extends Persona {
    String curso;

    Estudiante(String nombre, int edad, String curso) {
        super(nombre, edad);
        this.curso = curso;
    }

    void estudiar() {
        System.out.println(nombre + " está estudiando en el curso de " + curso);
    }
}

public class Main {
    public static void main(String[] args) {
        Estudiante estudiante1 = new Estudiante("Maria", 20, "Matemáticas");
        estudiante1.saludar();
        estudiante1.estudiar();
    }
}
