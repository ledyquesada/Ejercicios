package controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.List;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;
import modelo.Museo;
import modelo.RepositorioMuseo;
import vista.Vista;

public class Controlador implements ActionListener{
   
    RepositorioMuseo repositorio;
    Museo museo = Museo.crearMuseo();
    Vista vista; 
    DefaultTableModel modelo = new DefaultTableModel();

    public Controlador(){
        super();
    } 

    public Controlador(RepositorioMuseo repositorio, Vista vista) {
        super();
        this.repositorio = repositorio;
        this.vista = vista;
        agregarEventos();
        vista.setVisible(true);
        
    }

    private void agregarEventos() {
        vista.getListarjButton().addActionListener(this);
        vista.getBuscarjButton().addActionListener(this);
        vista.getActualizarjButton().addActionListener(this);
        vista.getCrearjButton().addActionListener(this);
        vista.getEliminarjButton().addActionListener(this);    
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        

        if (e.getSource() == vista.getListarjButton()){
            listarClic(e);
        }
        if (e.getSource() == vista.getBuscarjButton()){
            buscarClic(e);
        }
        
        if (e.getSource() == vista.getActualizarjButton()){
            actualizarClic(e);
        }
        
        if (e.getSource() == vista.getCrearjButton()){
            crearClic(e);
        }
        
        if (e.getSource() == vista.getEliminarjButton()){
            eliminarClic(e);
        }     
    
    }
    
    public void buscarClic(ActionEvent e){
        
        JTextField idField = vista.getIdjTextField();
        JTextField nombreField = vista.getNombreJTextField();
        JTextField ciudadField = vista.getCiudadJTextField();
        
        Long idBusqueda = Long.valueOf(idField.getText());
        Museo museo = repositorio.findById(idBusqueda).get();
        nombreField.setText(museo.getNombre());
        ciudadField.setText(museo.getCiudad());
    }

    public void actualizarClic(ActionEvent e){
        
        JTextField idField = vista.getIdjTextField();
        JTextField nombreField = vista.getNombreJTextField();
        JTextField ciudadField = vista.getCiudadJTextField();
        
        Long idBusqueda = Long.valueOf(idField.getText());
        String nombreBusqueda = nombreField.getText();
        String ciudadBusqueda = ciudadField.getText();
        Museo museo = repositorio.findById(idBusqueda).get();
        museo.setNombre(nombreBusqueda);
        museo.setCiudad(ciudadBusqueda);
        repositorio.save(museo);
        listarClic(e);
    }

    public void eliminarClic(ActionEvent e){
        
        JTextField idField = vista.getIdjTextField(); 
        Long idBusqueda = Long.valueOf(idField.getText());
        
        if (repositorio.existsById(idBusqueda)){
            repositorio.deleteById(idBusqueda);
        }
        listarClic(e);
    }

    public void crearClic(ActionEvent e){
        
        JTextField nombreField = vista.getNombreJTextField();
        JTextField ciudadField = vista.getCiudadJTextField();
        
        String nombreBusqueda = nombreField.getText();
        String ciudadBusqueda = ciudadField.getText();
        Museo museo = Museo.crearMuseo(nombreBusqueda, ciudadBusqueda);
        repositorio.save(museo);
        listarClic(e);
    }

    public void listarClic(ActionEvent e){
        JTable tabla = vista.getTabla();       
        List<Museo> listaMuseos = (List<Museo>) repositorio.findAll();
        int cont = 0;
        for (Museo s : listaMuseos){
            tabla.setValueAt(s.getIdMuseo(), cont, 0);
            tabla.setValueAt(s.getNombre(), cont, 1);
            tabla.setValueAt(s.getCiudad(), cont, 2);
            cont ++;
        }
        tabla.setValueAt("", cont, 0);
        tabla.setValueAt("", cont, 1);
        tabla.setValueAt("", cont, 2);   
    }        
}
    
    

