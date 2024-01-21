//Métricas

// ProductoMetrics.java
import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.data.jdbc.core.JdbcAggregateOperations;
import org.springframework.stereotype.Component;

@Component
public class ProductoMetrics {

    private final JdbcAggregateOperations jdbcAggregateOperations;

    public ProductoMetrics(JdbcAggregateOperations jdbcAggregateOperations, MeterRegistry meterRegistry) {
        this.jdbcAggregateOperations = jdbcAggregateOperations;

        // Registrar una métrica personalizada
        meterRegistry.gauge("productos.total", this, ProductoMetrics::totalProductos);
    }

    private double totalProductos() {
        // Obtener el número total de productos utilizando Spring Data JDBC
        return jdbcAggregateOperations.queryForObject("SELECT COUNT(*) FROM Producto", Integer.class);
    }
}
