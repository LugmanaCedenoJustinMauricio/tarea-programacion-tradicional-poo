from mascota import Mascota

def ejecutar_sistema_poo():
    print("========================================")
    print("   Sistema Veterinario (Enfoque POO)   ")
    print("========================================")

    print("\n--- Datos de la Primera Mascota ---")
    nom1 = input("Nombre de la mascota: ")
    esp1 = input("Especie de la mascota: ")
    ed1 = int(input("Edad de la mascota: "))

    mascota1 = Mascota(nom1, esp1, ed1)

    print("\n--- Datos de la Segunda Mascota ---")
    nom2 = input("Nombre de la mascota: ")
    esp2 = input("Especie de la mascota: ")
    ed2 = int(input("Edad de la mascota: "))

    mascota2 = Mascota(nom2, esp2, ed2)

    print("\n=== MOSTRANDO INFORMACIÓN DE LOS OBJETOS ===")
    mascota1.mostrar_informacion()
    mascota2.mostrar_informacion()

    print("\n=== ESCUCHANDO LOS SONIDOS DE LAS MASCOTAS ===")
    mascota1.hacer_sonido()
    mascota2.hacer_sonido()


if __name__ == "__main__":
    ejecutar_sistema_poo()