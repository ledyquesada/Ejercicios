//Ejercicio 1: Gestion de inventarios de productos

public class Producto {
    private String codigo;
    private String nombre;
    private int cantidadDisponible;
    private double precioUnitario;

    public Producto(String codigo, String nombre, int cantidadDisponible, double precioUnitario) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.cantidadDisponible = cantidadDisponible;
        this.precioUnitario = precioUnitario;
    }

    public void aumentarStock(int cantidad) {
        cantidadDisponible += cantidad;
    }

    public void disminuirStock(int cantidad) {
        if (cantidad <= cantidadDisponible) {
            cantidadDisponible -= cantidad;
        } else {
            System.out.println("No hay suficiente stock para retirar " + cantidad + " unidades.");
        }
    }

    public double calcularValorInventario() {
        return cantidadDisponible * precioUnitario;
    }

    public String getResumen() {
        return "Producto: " + nombre + " | Stock: " + cantidadDisponible + " | Total: $" + calcularValorInventario();
    }
}

//Ejercicio 2 Usuario:

public class Usuario {
    protected String nombre;
    protected String correo;
    protected String rol;

    public Usuario(String nombre, String correo, String rol) {
        this.nombre = nombre;
        this.correo = correo;
        this.rol = rol;
    }

    public boolean esAdministrador() {
        return rol.equalsIgnoreCase("admin");
    }

    public String getInfo() {
        return "Usuario: " + nombre + " | Rol: " + rol;
    }
}

public class Administrador extends Usuario {
    public Administrador(String nombre, String correo) {
        super(nombre, correo, "admin");
    }

    public void gestionarUsuarios() {
        System.out.println(nombre + " está gestionando usuarios...");
    }
}


//Ejercicio 3: Entradas y salidas de inventario

import java.util.*;

public class MovimientoInventario {
    private String tipoMovimiento; // "entrada" o "salida"
    private Producto producto;
    private int cantidad;
    private Date fecha;

    public MovimientoInventario(String tipoMovimiento, Producto producto, int cantidad) {
        this.tipoMovimiento = tipoMovimiento;
        this.producto = producto;
        this.cantidad = cantidad;
        this.fecha = new Date(); // fecha actual
    }

    public void aplicarMovimiento() {
        if (tipoMovimiento.equalsIgnoreCase("entrada")) {
            producto.aumentarStock(cantidad);
        } else if (tipoMovimiento.equalsIgnoreCase("salida")) {
            producto.disminuirStock(cantidad);
        }
    }

    public String getResumen() {
        return tipoMovimiento.toUpperCase() + " - " + producto.getResumen() + " - Fecha: " + fecha;
    }
}

public class Inventario {
    private List<Producto> productos;

    public Inventario() {
        productos = new ArrayList<>();
    }

    public void agregarProducto(Producto p) {
        productos.add(p);
    }

    public void registrarMovimiento(String codigoProducto, String tipo, int cantidad) {
        for (Producto p : productos) {
            if (p.getResumen().contains(codigoProducto)) {
                MovimientoInventario mov = new MovimientoInventario(tipo, p, cantidad);
                mov.aplicarMovimiento();
                System.out.println("Movimiento registrado: " + mov.getResumen());
                return;
            }
        }
        System.out.println("Producto no encontrado.");
    }

    public void mostrarInventario() {
        for (Producto p : productos) {
            System.out.println(p.getResumen());
        }
    }
}


