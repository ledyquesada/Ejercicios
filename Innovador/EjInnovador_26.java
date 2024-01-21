//

// Producto.java
import org.springframework.data.annotation.Id;

public class Producto {
    @Id
    private Long id;
    private String nombre;

    // getters y setters
}

// ProductoRepository.java
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface ProductoRepository extends CrudRepository<Producto, Long> {
    @Query("SELECT * FROM Producto WHERE nombre = :nombre")
    Iterable<Producto> findByNombre(String nombre);
}
