/**
*
* Figuras Geometricas
*/


abstract class FiguraGeometrica {
    abstract double calcularArea();
}

class Circulo extends FiguraGeometrica {
    private double radio;

    Circulo(double radio) {
        this.radio = radio;
    }

    @Override
    double calcularArea() {
        return Math.PI * Math.pow(radio, 2);
    }
}

class Cuadrado extends FiguraGeometrica {
    private double lado;

    Cuadrado(double lado) {
        this.lado = lado;
    }

    @Override
    double calcularArea() {
        return Math.pow(lado, 2);
    }
}

class Triangulo extends FiguraGeometrica {
    private double base;
    private double altura;

    Triangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
    }

    @Override
    double calcularArea() {
        return (base * altura) / 2;
    }
}

public class Main {
    public static void main(String[] args) {
        FiguraGeometrica circulo = new Circulo(5.0);
        FiguraGeometrica cuadrado = new Cuadrado(4.0);
        FiguraGeometrica triangulo = new Triangulo(3.0, 6.0);

        List<FiguraGeometrica> figuras = Arrays.asList(circulo, cuadrado, triangulo);

        for (FiguraGeometrica figura : figuras) {
            System.out.println("Área: " + figura.calcularArea());
        }
    }
}
