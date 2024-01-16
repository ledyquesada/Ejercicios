/**
*
* Cuenta Bancaria
*/


class CuentaBancaria {
    private String titular;
    private double saldo;

    CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    void depositar(double monto) {
        saldo += monto;
        System.out.println("Depósito realizado. Nuevo saldo: " + saldo);
    }

    void retirar(double monto) {
        if (monto <= saldo) {
            saldo -= monto;
            System.out.println("Retiro realizado. Nuevo saldo: " + saldo);
        } else {
            System.out.println("Saldo insuficiente.");
        }
    }

    String getTitular() {
        return titular;
    }

    double getSaldo() {
        return saldo;
    }
}

class CuentaCorriente extends CuentaBancaria {
    private double limiteDescubierto;

    CuentaCorriente(String titular, double saldoInicial, double limiteDescubierto) {
        super(titular, saldoInicial);
        this.limiteDescubierto = limiteDescubierto;
    }

    @Override
    void retirar(double monto) {
        if (monto <= getSaldo() + limiteDescubierto) {
            setSaldo(getSaldo() - monto);
            System.out.println("Retiro realizado. Nuevo saldo: " + getSaldo());
        } else {
            System.out.println("Límite de descubierto alcanzado.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        CuentaBancaria cuenta1 = new CuentaBancaria("Juan", 1000.0);
        cuenta1.depositar(500.0);
        cuenta1.retirar(200.0);

        CuentaCorriente cuenta2 = new CuentaCorriente("Ana", 2000.0, 500.0);
        cuenta2.depositar(1000.0);
        cuenta2.retirar(3000.0);
    }
}
