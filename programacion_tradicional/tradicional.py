historial_mascota = []

def registrae_mascota():
    print("\n--- Registrar nueva mascota ---")
    nombre_mascota = input("Nombre de la mascota: ")
    especie = input("Especie de la mascota: ")
    edad = int(input("Edad de la mascota: "))

    nueva_mascota = {
        "nombre_mascota": nombre_mascota,
        "especie": especie,
        "edad": edad
    }

    historial_mascota.append(nueva_mascota)
    print(f"Mascota {nombre_mascota} registrada con éxito")


def mostrar_mascota():
    print("\n=== Historial de mascotas registradas ===")

    if not historial_mascota:
        print("No hay mascotas registradas en este momento")
        return

    for mascota in historial_mascota:
        print(f"Nombre: {mascota['nombre_mascota']} | Especie: {mascota['especie']} | Edad: {mascota['edad']} años")


def menu():
    while True:
        print("\n==============================")
        print("   Sistema Veterinario (Estructurado)   ")
        print("==============================")
        print("1. Registrar Mascota")
        print("2. Mostrar Mascota")
        print("3. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            registrae_mascota()
        elif opcion == "2":
            mostrar_mascota()
        elif opcion == "3":
            print("Saliendo del sistema... ¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo")


if __name__ == "__main__":
    menu()