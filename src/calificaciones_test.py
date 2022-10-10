from calificaciones import nota , nota2 , calcula_nota_cuatrimestre , calcula_nota_evaluacion_continua
# Primero el número de aciertos, después el número de errores y por último el número de 
# respuestas correctas.
print(nota(23 , 3 , 27))

# Otra forma de saber la nota que se pedira los valores en el terminal de abajo.
print(nota2())

# El primer valor es la nota del práctico y el otro es la nota del proyecto
# Dentro del proceso, si proyecto es mayor que 5, te pedira tus notas de los cuestionarios
print(calcula_nota_cuatrimestre(5 , 6)) 
print(calcula_nota_evaluacion_continua())