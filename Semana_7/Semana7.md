# Portafolio de evidencias.

## Semana 7.

Tipo de dato: Str
Cadena de texto (usando comillas o doble comillas)
Representan cualquier cosa que sea texto.
Se pueden concatenar usando "+", no es una suma aritmética sino la unión de un string con otro.
Se puede repetir (concatenar consigo mismo) una cierta cantidad de veces usando "*"
Son inmutables: No se pueden cambiar a menos que se vuelva a definir.
Se puede acceder a los caracteres específicos dentro de un string usando paréntesis cuadrados []. Las posiciones empiezan en 0 para el primero y así consecutivamente.
Se puede acceder a un conjunto de caractere específicos dentro de un string usando slicing e.g.: "string[inicio:final+1]"
Se usa "\" para indicar ciertos símbolos que no se pueden escribir mediante el teclado e.g.: Nueva línea/enter (\n=new line), Escribir \ (\\="\")

len(str) captura la longitud de un string, cada uno de los elementos dentro de un texto es considerado como un caracter
.upper (mayúsculas) .lower(minúsculas)
strip para quitar caractere a los extremos de un string
replace: remplaza un símbolo de un string por otro nuevo.

Archivo: La info se guarda en archivos, que a su vez se guardan en directorios.
El programa y su código es, igualmente guardado dentro de un archivo. 
Importante aprender a (leer, escribir, copiar, mover, etc.) porque así se comunican los datos.
función open para abrir un archivo, se puede indica el parametro de lectura (r) o escritura (w)
Al usar w: se borra el archivo pasado (con el mismo nombre) para dar espacio al nuevo archivo (versión actualizada)
close: se cierra y se guarda la información actualizada
