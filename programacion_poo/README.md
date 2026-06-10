# Sistema de Gestión de Mascotas - Tarea de Programación

## Datos del Estudiante
* **Nombre Completo:** Justin Mauricio Lugmaña Cedeño
* **Institución:** Universidad Estatal Amazónica (UEA)
* **Carrera:** Tecnologías de la Información / Ingeniería de Software

---

## Descripción del Proyecto
Este repositorio contiene la solución práctica para la gestión básica de mascotas (nombre, especie y edad) implementada bajo dos paradigmas de desarrollo diferentes en Python:

1. **Programación Tradicional (Estructurada):** Ubicado en la carpeta `PROGRAMACION_TRADICIONAL/`. Se diseñó usando lógica secuencial, variables globales, funciones independientes (`def`) y estructuras de datos nativas como listas y diccionarios, todo controlado por un menú interactivo en consola.
2. **Programación Orientada a Objetos (POO):** Ubicado en la carpeta `PROGRAMACION_POO/`. Se implementó de forma modular separando el código en `mascota.py` (la clase o molde con sus atributos y métodos) y `main.py` (el flujo principal donde se instancian los objetos independientes y se ejecutan sus comportamientos).

---

## Reflexión: Diferencias entre la Programación Tradicional y la POO

Tras el desarrollo de ambos programas, se identifican las siguientes diferencias fundamentales:

* **Organización de Datos y Lógica:** En el enfoque tradicional, los datos (los diccionarios) y las funciones que los procesan están completamente separados. En la POO, los datos (atributos) y el comportamiento (métodos) se empaquetan juntos de forma lógica dentro de una sola entidad llamada Clase.
* **Modularidad y Mantenimiento:** La programación tradicional es ideal para scripts pequeños y rápidos, pero se vuelve compleja de mantener a gran escala. La POO destaca por su modularidad; separar el molde (`mascota.py`) de la ejecución (`main.py`) hace que el código sea mucho más limpio, ordenado y fácil de actualizar sin romper el programa principal.
* **Nivel de Abstracción:** El enfoque tradicional nos obliga a manipular colecciones crudas directamente en el flujo del menú. La POO permite un nivel de abstracción más cercano al mundo real, donde tratamos a cada mascota como un "objeto" único que sabe cómo mostrar su propia información y cómo reaccionar (hacer sonido) de forma autónoma.