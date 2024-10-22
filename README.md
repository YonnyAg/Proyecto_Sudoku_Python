# Aplicación Solucionador de Sudoku

Este proyecto es una aplicación gráfica para resolver Sudokus, construida en Python usando la biblioteca `tkinter`. La aplicación permite a los usuarios ingresar un puzzle de Sudoku y resolverlo automáticamente utilizando un algoritmo de backtracking.

## Características

- **Cuadrícula para ingresar el Sudoku**: Los usuarios pueden introducir su propio puzzle en la interfaz de 9x9.
- **Botón de Solución**: Después de ingresar el puzzle, al hacer clic en el botón "Resolver" se muestra la solución.
- **Temporizador**: Muestra el tiempo que toma resolver el puzzle en segundos.
- **Manejo de errores**: Si no existe una solución para el puzzle ingresado, aparece un cuadro de mensaje informando al usuario.

## Uso

1. Clona este repositorio.
2. Asegúrate de tener Python instalado en tu computadora.
3. Ejecuta la aplicación con el siguiente comando en tu terminal:
   ```bash
   python main.py
4. Ingresa el puzzle de Sudoku en la cuadrícula de 9x9. Deja las celdas vacías para los espacios sin número.
5. Haz clic en el botón "Resolver" para que se resuelva el puzzle.
   
¿Cómo funciona?
El algoritmo que resuelve el Sudoku utiliza backtracking para rellenar las celdas vacías. Prueba los números del 1 al 9 en cada celda vacía, asegurándose de que el número sea válido tanto en la fila, la columna como en el subcuadro de 3x3.
Una vez que se coloca un número válido, el algoritmo pasa a la siguiente celda vacía. Si no se puede colocar un número válido, retrocede a la celda anterior y prueba un número diferente.
La cuadrícula se actualiza dinámicamente cuando se encuentra la solución, y se muestra el tiempo que tomó resolverlo.

Bibliotecas utilizadas
- tkinter: Una biblioteca estándar de Python para crear interfaces gráficas.
- time: Un módulo de Python para medir el tiempo que tarda en resolverse el puzzle.
- messagebox: Un módulo de tkinter para mostrar mensajes emergentes cuando no se encuentra una solución.
  
Estructura de archivos
- main.py: El archivo principal de la aplicación que contiene la lógica para la interfaz gráfica y el algoritmo de resolución de Sudoku.

Requisitos
- Python 3.x
- No se requieren librerías externas, todas las dependencias forman parte de la biblioteca estándar de Python.
