//Categoria

// ProductoService.java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class ProductoService {

    @Transactional
    public void agregarYActualizarProducto(Producto nuevoProducto, Long idProductoActualizar, String nuevoNombre) {
        // Lógica para agregar un nuevo producto y actualizar el nombre de otro
        // Ambas operaciones deben ocurrir en una transacción
    }
}
