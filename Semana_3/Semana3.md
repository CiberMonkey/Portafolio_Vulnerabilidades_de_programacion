# Portafolio de evidencias.

## Semana 3.

Conitnué con el curso y vi un proyecto que me llamó la atención, el cuál evidencio con la siguiente preguinta. ¿Cómo *e.g.* Word puede contabilizar las palabras?
Debido a esto, investigué como podía hacer lo mismo en python y, usando una serie de condicionales y listas, logré entender y replicar con éxito el "contador de palabras".
Básicamente lo que hago es convertir un solo stirng a una seride de strings separados por sus espacios, elimino las mayúsculas para evitar confusión y contabilizo las que son idénticas.
Como resultado, al correr él código lo que arroja en la terminal son las distintas palabras existentes y su repetición a lo largo del texto.

Código:

texto = """​

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""

quitar = ",;:.\n!\"'`"
for caracter in quitar:
 texto = texto.replace(caracter,
  "") 
texto = texto.lower()

palabras = texto.split(" ")

diccionario_frecuencias = {}
for palabra in palabras:
 if palabra in diccionario_frecuencias:
  diccionario_frecuencias[palabra] += 1
 else:
  diccionario_frecuencias[palabra] = 1

for palabra in diccionario_frecuencias:
 frecuencia = diccionario_frecuencias[palabra]

 if frecuencia >= 1 : {
      print(f"'{palabra}'", "\033[1m" + f"tiene una frecuencia de {frecuencia}")
 }
