def nota(aciertos , errores , numero_respuestas):
    return ((aciertos*10)/numero_respuestas) - ((errores*10)/(50 - numero_respuestas))
def nota2():
    print("Escriba el Nº de aciertos")
    a = int(input()) 
    print("Escriba el Nº de errores")
    b = int(input()) 
    print("Escriba el Nº de aciertos totales")
    c = int(input())
    print("===Cálculo de nota===")
    print("Si el Nº de aciertos es" , a ,"el Nº de errores es", b ,"y el Nº de respuestas correctas era", c ,", su nota final es", ((a*10)/c)-(b*10)/(50-c))