/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package modelo;

import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Column;
import org.springframework.data.relational.core.mapping.Table;

/**
 *
 * @author Juan
 */
@Table("Museo")
public class Museo {    
    @Id
    @Column("idmuseo")        
    private Long idMuseo;
    @Column("nombre")
    private String nombre;
    @Column("ciudad")
    private String ciudad;
    
    private Museo(Long idMuseo, String nombre, String ciudad) {
        this.idMuseo = idMuseo;
        this.nombre = nombre;
        this.ciudad = ciudad;
    }
    
    public static Museo crearMuseo(Long idMuseo, String nombre, String ciudad){
        return new Museo(idMuseo, nombre, ciudad);
    }
    
    public static Museo crearMuseo(String nombre, String ciudad){
        return new Museo(null, nombre, ciudad);
    }
    
    
    public static Museo crearMuseo(){
    return new Museo(null, null, null);
    }

    public Long getIdMuseo() {
        return idMuseo;
    }

    public void setIdMuseo(Long idMuseo) {
        this.idMuseo = idMuseo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCiudad() {
        return ciudad;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }

    @Override
    public String toString() {
        return "Museo{" + "idMuseo=" + idMuseo + ", nombre=" + nombre + ", ciudad=" + ciudad + '}';
    }
    
}
