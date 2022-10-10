def nota(aciertos , errores , numero_respuestas):
    return ((aciertos*10)/numero_respuestas) - ((errores*10)/(50 - numero_respuestas))

def darnumero():
    int(input())

def Dame_cuestionarios(j):
    cuestionarios= []
    for n in range(j):
        cuestionarios.append(float(input(f"Dame la nota del cuestionario {n+1}:")))
    return cuestionarios

def notas_proyecto(h):
    proyecto=[]
    for y in range(h):
        proyecto.append(float(input(f"Dame la nota del proyecto {y + 1}:")))
    return proyecto

def notas_practica(g):
    practica=[]
    for x in range(g):
        practica.append(float(input(f"Dame la nota de la práctica {x + 1}:")))
    return practica

def darnumero():
    int(input())

def nota2():
    print("Escriba el Nº de aciertos")
    a = darnumero() 
    print("Escriba el Nº de errores")
    b = darnumero() 
    print("Escriba el Nº de aciertos totales")
    c = darnumero()
    print("===Cálculo de nota===")
    print("Si el Nº de aciertos es" , a ,"el Nº de errores es", b ,"y el Nº de respuestas correctas era", c ,", su nota final es", ((a*10)/c)-(b*10)/(50-c))

def calcula_nota_cuatrimestre(parcial , proyecto):
    result = 0    
    if proyecto < 5:
        return print("tu nota del cuatrimestre es:" ,result + 3)  
        
    else:
        C1 = float(input("Indique la nota del primer cuestionario en el cuatrimestre"))
        C2 = float(input("Indique la nota del segundo cuestionario en el cuatrimestre"))
        print("Indique la nota del tercer cuestionario en el cuatrimestre")
        C3 = float(input())
        cuestionarios = (C1 , C2 , C3)
        return print("tu nota del cuatrimestre es:" , result + sum(cuestionarios) * 0.1 + parcial * 0.6 + proyecto * 0.1)

def calcula_nota_evaluacion_continua():
    result = 0
    cuestionarios = Dame_cuestionarios(6)
    proyecto= notas_proyecto(2)
    practica= notas_practica(2)
    if cuestionarios[0] + cuestionarios[1] + cuestionarios[2] < 12 or cuestionarios[3] + cuestionarios[4] + cuestionarios[5] < 12:
        print("Tu nota de evaluación continua es 4")
    else:
        return print("tu nota es:", (result + sum(cuestionarios)*0.05 + sum(proyecto) * 0.05 + sum(practica) * 0.3)) 
        

