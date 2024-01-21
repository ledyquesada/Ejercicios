//Categoria

// Categoria.java
import org.springframework.data.annotation.Id;

public class Categoria {
    @Id
    private Long id;
    private String nombre;

    // getters y setters
}

// Producto.java (actualizado)
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

@Table("Producto")
public class Producto {
    @Id
    private Long id;
    private String nombre;

    @Column("categoria_id")
    private Long categoriaId;

    // getters y setters
}

// ProductoRepository.java (actualizado)
import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;

public interface ProductoRepository extends CrudRepository<Producto, Long> {
    @Query("SELECT * FROM Producto WHERE categoria_id = :categoriaId")
    Iterable<Producto> findByCategoriaId(Long categoriaId);
}
