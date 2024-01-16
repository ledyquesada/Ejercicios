/**
*
* Expresiones Lambda y Streams
*/

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        List<Integer> numerosParesDuplicados = numeros.stream()
                .filter(numero -> numero % 2 == 0)
                .map(numero -> numero * 2)
                .collect(Collectors.toList());

        System.out.println("Números pares duplicados: " + numerosParesDuplicados);
    }
}
