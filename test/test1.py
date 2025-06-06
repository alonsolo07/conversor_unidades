from conversor.velocity import Velocity
from conversor.mass import Mass
from conversor.distance import Distance
from conversor.temperature import Temperature


def main():
    print("Pruebas básicas de conversión\n")

    # Velocity
    print("Velocidad:")
    print("100 km/h a m/s =", Velocity.kmh_to_mps(100))
    print("60 mph a km/h =", Velocity.mph_to_kmh(60))
    print()

    # Mass
    print("Masa:")
    print("10 kg a lb =", Mass.kg_to_lb(10))
    print("5000 g a lb =", Mass.g_to_lb(5000))
    print()

    # Distance
    print("Distancia:")
    print("5 km a mi =", Distance.km_to_mi(5))
    print("3 mi a m =", Distance.mi_to_m(3))
    print()

    # Temperature
    print("Temperatura:")
    print("0 °C a °F =", Temperature.c_to_f(0))
    print("32 °F a K =", Temperature.f_to_k(32))
    print()

if __name__ == "__main__":
    main()