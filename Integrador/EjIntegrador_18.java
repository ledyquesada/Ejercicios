/**
*
* Deforestacion
*/

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

class RegiónDeforestada {
    private String nombre;
    private double áreaDeforestada;

    // Constructor, getters y setters

    @Override
    public String toString() {
        return "Región: " + nombre + ", Área Deforestada: " + áreaDeforestada + " km²";
    }
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
        String urlAPI = "https://jsonplaceholder.typicode.com/posts"; // Ejemplo de API simulada
        String datosAPI = ConectorAPI.obtenerDatosAPI(urlAPI);

        List<RegiónDeforestada> regionesDeforestadas = procesarDatosAPI(datosAPI);

        // Imprimir resultados
        for (RegiónDeforestada región : regionesDeforestadas) {
            System.out.println(región);
        }
    }

    private static List<RegiónDeforestada> procesarDatosAPI(String datosAPI) {
        List<RegiónDeforestada> regionesDeforestadas = new ArrayList<>();

        Gson gson = new Gson();
        JsonArray jsonArray = gson.fromJson(datosAPI, JsonArray.class);

        for (JsonElement elemento : jsonArray) {
            JsonObject jsonObject = elemento.getAsJsonObject();

            String nombre = jsonObject.get("title").getAsString();
            double áreaDeforestada = jsonObject.get("userId").getAsDouble(); // Solo para demostración, debes adaptar según la estructura real

            RegiónDeforestada región = new RegiónDeforestada();
            región.setNombre(nombre);
            región.setÁreaDeforestada(áreaDeforestada);

            regionesDeforestadas.add(región);
        }

        return regionesDeforestadas;
    }
}
/**
*En este ejemplo, he utilizado JSONPlaceholder como una API simulada para demostración. Debes reemplazar la URL con la API real que estés utilizando y ajustar el código según la estructura de los datos reales.
*
*/
