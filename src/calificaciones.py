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

def calcula_nota_cuatrimestre(parcial , proyecto):
    result = 0    
    if proyecto < 5:
        return result + 3  
    else:
        print("Indique la nota del primer cuestionario en el cuatrimestre")
        C1 = float(input())
        print("Indique la nota del segundo cuestionario en el cuatrimestre")
        C2 = float(input())
        print("Indique la nota del tercer cuestionario en el cuatrimestre")
        C3 = float(input())
        cuestionarios = (C1 , C2 , C3)
        return result + sum(cuestionarios) * 0.1 + parcial * 0.6 + proyecto * 0.1
