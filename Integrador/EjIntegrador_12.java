/**
*
* Calcular impuesto
*/

abstract class Vehiculo {
    private String marca;
    private String modelo;

    Vehiculo(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
    }

    abstract double calcularImpuesto();
}

class Coche extends Vehiculo {
    Coche(String marca, String modelo) {
        super(marca, modelo);
    }

    @Override
    double calcularImpuesto() {
        return 100.0;  // Impuesto fijo para coches
    }
}

class Camion extends Vehiculo {
    Camion(String marca, String modelo) {
        super(marca, modelo);
    }

    @Override
    double calcularImpuesto() {
        return 200.0;  // Impuesto fijo para camiones
    }
}

public class Main {
    public static void main(String[] args) {
        Vehiculo coche = new Coche("Toyota", "Corolla");
        Vehiculo camion = new Camion("Volvo", "VNL");

        List<Vehiculo> vehiculos = Arrays.asList(coche, camion);

        for (Vehiculo vehiculo : vehiculos) {
            System.out.println("Impuesto para " + vehiculo.getMarca() + " " + vehiculo.getModelo() +
                    ": " + vehiculo.calcularImpuesto());
        }
    }
}
