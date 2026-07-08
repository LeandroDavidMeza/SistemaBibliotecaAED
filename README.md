# Trabajo Final Integrador del Lab. de Python: Sistema de Gestión de Biblioteca
**Asignatura:** Algoritmos y Estructuras de Datos - ISI  
**Ciclo:** 2026

## Comisión e Integrantes
* **Comisión ISI B (K1.2)**
- Alvarez, Daniel Agustin
- Brailovsky Chas, Ramiro Iván
- Kohler, Sofía Pilar
- Meza, Leandro David
- Sanz, Victoria
   > Video editado por Kohler, Sofía Pilar

-----

## Descripción
Sistema de gestión de biblioteca desarrollado en Python, para ejecutarse
mediante consola. Su objetivo es automatizar las tareas diarias de una
biblioteca: administrar el catálogo de libros, el registro de socios y el
circuito completo de préstamos y devoluciones.

El sistema está organizado en una arquitectura modular, donde cada archivo se
ocupa de un dominio específico (libros, usuarios, préstamos, persistencia y
utilidades). La información se almacena en archivos de texto (.txt), de modo
que los datos se conservan entre una ejecución y la siguiente.

## Utilización de IA
Para la realización de este trabajo se utilizaron dos Inteligencias Artificiales diferentes, Gemini y Claude, las cuales fueron útiles para generar ideas nuevas, diseñar estructuras y depurar errores. Cabe aclarar que, en todos los casos, las decisiones finales sobre qué aplicar y qué rechazar fueron tomadas y comprendidas por el equipo completo. Por ejemplo, descartamos una sugerencia de validar las opciones del menú con una función que mezclaba enteros y strings, por considerarla incoherente con el resto del sistema.

## Instrucciones de Ejecución

1. **Clonar o descargar** el repositorio en la máquina local:

   ```bash
   git clone https://github.com/LeandroDavidMeza/SistemaBibliotecaAED
   ```

2. **Ingresar a la carpeta** del proyecto:

   ```bash
   cd SistemaBibliotecaAED
   ```

3. **Ejecutar el programa** desde la terminal:

   ```bash
   python main.py
   ```

   > En algunos sistemas el comando es `python3` en lugar de `python`.

4. Utilizar el **menú principal** ingresando el número de la opción deseada y
   presionando Enter. Para conservar los cambios realizados, salir siempre con
   la opción **5. Guardar cambios y Salir**, que escribe los datos en los
   archivos `.txt` antes de cerrar el programa.

> ⚠️ **Advertencia sobre los datos de ejemplo:**
> En el repositorio de GitHub, la carpeta `datos/` incluye datos de ejemplo
> (libros, usuarios y préstamos) para poder realizar pruebas. Si se desea poner
> el programa en funcionamiento real, se deben **eliminar estos casos de
> ejemplo** —vaciando o borrando los archivos de la carpeta `datos/`— para
> comenzar con una base de datos limpia.
