/**
*
* Serializacion
*/

import java.io.*;

class Empleado implements Serializable {
    private String nombre;
    private int edad;
    private double salario;

    Empleado(String nombre, int edad, double salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    @Override
    public String toString() {
        return "Empleado{" +
                "nombre='" + nombre + '\'' +
                ", edad=" + edad +
                ", salario=" + salario +
                '}';
    }
}

public class Main {
    public static void main(String[] args) {
        Empleado empleado = new Empleado("Juan", 30, 50000.0);

        // Serialización
        try (ObjectOutputStream salida = new ObjectOutputStream(new FileOutputStream("empleado.ser"))) {
            salida.writeObject(empleado);
            System.out.println("Empleado serializado correctamente.");
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Deserialización
        try (ObjectInputStream entrada = new ObjectInputStream(new FileInputStream("empleado.ser"))) {
            Empleado empleadoDeserializado = (Empleado) entrada.readObject();
            System.out.println("Empleado deserializado: " + empleadoDeserializado);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
