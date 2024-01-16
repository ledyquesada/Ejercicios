/**
*
* Deforestacion
*/

import java.net.HttpURLConnection;
import java.net.URL;
import java.io.BufferedReader;
import java.io.InputStreamReader;

class RegiónDeforestada {
    private String nombre;
    private double áreaDeforestada;

    // Constructor, getters y setters
}

class ConectorAPI {
    static String obtenerDatosAPI(String url) {
        StringBuilder respuesta = new StringBuilder();
        try {
            URL urlAPI = new URL(url);
            HttpURLConnection conexión = (HttpURLConnection) urlAPI.openConnection();
            conexión.setRequestMethod("GET");

            BufferedReader lector = new BufferedReader(new InputStreamReader(conexión.getInputStream()));
            String línea;

            while ((línea = lector.readLine()) != null) {
                respuesta.append(línea);
            }
            lector.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return respuesta.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        String urlAPI = "https://ejemplo.api/deforestacion/colombia";
        String datosAPI = ConectorAPI.obtenerDatosAPI(urlAPI);

        // Procesar los datos y crear instancias de RegiónDeforestada
        // Puedes utilizar bibliotecas como Gson para convertir datos JSON a objetos Java

        // Ejemplo de procesamiento básico:
        RegiónDeforestada región = new RegiónDeforestada();
        región.setNombre("Amazonía");
        región.setÁreaDeforestada(5000.0);

        // Continuar con la lógica de tu aplicación
    }
}
