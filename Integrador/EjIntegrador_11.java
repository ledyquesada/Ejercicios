/**
*
* Tienda de productos
*/

abstract class Producto {
    private String nombre;
    private double precio;

    Producto(String nombre, double precio) {
        this.nombre = nombre;
        this.precio = precio;
    }

    abstract double calcularDescuento();
}

class Libro extends Producto {
    Libro(String nombre, double precio) {
        super(nombre, precio);
    }

    @Override
    double calcularDescuento() {
        return getPrecio() * 0.1;  // Descuento del 10% para libros
    }
}

class Electrodomestico extends Producto {
    Electrodomestico(String nombre, double precio) {
        super(nombre, precio);
    }

    @Override
    double calcularDescuento() {
        return getPrecio() * 0.05;  // Descuento del 5% para electrodomésticos
    }
}

public class Main {
    public static void main(String[] args) {
        Producto libro = new Libro("Java Programming", 50.0);
        Producto electrodomestico = new Electrodomestico("Refrigerador", 500.0);

        List<Producto> productos = Arrays.asList(libro, electrodomestico);

        for (Producto producto : productos) {
            System.out.println("Descuento para " + producto.getNombre() + ": " + producto.calcularDescuento());
        }
    }
}
