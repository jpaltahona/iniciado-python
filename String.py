colors = ["blue", "azul", "amarillo", "red"]
print(colors)

colors[2] = "marron"
print(colors)

#Usar pop para eliminar el ultimo elemento de una lista
colors.pop()
print(colors)

# Utilizar extend cuando querramos agregar multiples valores pero hay que ponerlos dentro de una tupla o lista

colors.extend( ['salmon', 'salamnaca'] ) 
print(colors)

#Utilizar append cuando querramos agregar un solo alor
colors.append('salmon')
print(colors)

#Usar insert cuando vallamar agregar un valir en una posicion exacta
colors.insert(1, 'violet')
print(colors)

colors.insert(len(colors), 'morado')
print(colors)

#REmover elementos

colors.remove("blue")

print(colors)