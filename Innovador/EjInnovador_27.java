// Operaciones CRUD JDBC

// Aplicación de Consola
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.Scanner;

@SpringBootApplication
public class ConsoleApp implements CommandLineRunner {

    @Autowired
    private ProductoRepository productoRepository;

    public static void main(String[] args) {
        SpringApplication.run(ConsoleApp.class, args);
    }

    @Override
    public void run(String... args) {
        Scanner scanner = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("1. Agregar Producto");
            System.out.println("2. Buscar Productos por Nombre");
            System.out.println("3. Actualizar Nombre de Producto");
            System.out.println("4. Eliminar Producto");
            System.out.println("0. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();

            switch (opcion) {
                case 1:
                    agregarProducto();
                    break;
                case 2:
                    buscarPorNombre();
                    break;
                case 3:
                    actualizarNombre();
                    break;
                case 4:
                    eliminarProducto();
                    break;
            }

        } while (opcion != 0);
    }

    private void agregarProducto() {
        // Implementar lógica para agregar un nuevo producto
    }

    private void buscarPorNombre() {
        // Implementar lógica para buscar productos por nombre
    }

    private void actualizarNombre() {
        // Implementar lógica para actualizar el nombre de un producto
    }

    private void eliminarProducto() {
        // Implementar lógica para eliminar un producto
    }
}
