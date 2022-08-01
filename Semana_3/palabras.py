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