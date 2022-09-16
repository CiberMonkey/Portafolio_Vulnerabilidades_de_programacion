# Portafolio de evidencias.

## Semana 6.

Funciones: Vienen de la necesidad de reutilizar código en distintos momentos de un programa.
	Fragmento de código que recibe parámetros, ejecuta acciones y retorna un resultado. 
Haciendo el Simil con el ámbito matemático.
Elementos de entrada=Parámetros
Fórmula=Código
Valor de salida=Retorno

Elementos de una Función
Parámetros: Elementos que recibe una función para trabajar con ellos. Se entregan al llamar la función, según la necesidad.
Return: Valor que entrega la función al terminar de ejecutarse. Indica el fin de una función

Módulos: Librerías que contienen funciones, ya programada. e.g.: random/math: Permiten realizar acciones u operaciones cotidianas con un simple llamado a una función.
Se requiere importar (usando import) el módulo o librería, puede ser general o específico:
import xxx                   from xxx import y, yy, yyy                from xxx import r as randomize
Para usar las funciones de un módulo/librería se especifíca primero la lib y, después de un "." la función.
e.g.: math.sin()

Definición de funciones
Estructura: def nombre(parámetros)
Posterior a los parámetros y previo al return, se establece el código de las instrucciones a seguir
Solo se deben definir una sola vez las funciones. En caso de repetir, se tomará la última definición.
No se puede llamar a una función antes de terminar la definición.

Invocación: Llamado, se realiza cuando se quiere ejecutar la función definida.
Scope: Parte de una función, corresponde al manejo  de las variables dentro de la misma. Las variables definidas dentro de una función no existen fuera de ella, se les llaman variables locales.
Fuera del scope: (Externo/Superior) Variables que no fueron definidas en la función.

Funciones como módulo
Cada archivo en Pyhton .py es un módulo. Se pueden importar las funciones y constantes de cualquier otro archivo.
Cudar el origen de las funciones importandas para no perder orden en la esctructura del programa.

