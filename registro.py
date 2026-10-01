def mostrar_encabezado_escuela():
  
    print("      UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DE PUEBLA  ")
    print("    REPORTE DE EVALUACIÓN Y RENDIMIENTO ACADÉMICO")
   


def obtener_nota_minima_aprobatoria():
   
    return 6.0

def evaluar_rendimiento(nota_final):
   
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    else:  
        return "Excelente"


def calcular_promedio_ponderado(nota_examenes, nota_tareas):
   
    promedio = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(promedio, 1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
   
    mostrar_encabezado_escuela()

    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado_academico = evaluar_rendimiento(nota_final)

    necesita_extraordinario = "SÍ" if nota_final < nota_minima else "NO"
   
    print(f"Alumno:                        {nombre_alumno}")
    print(f"Nota Exámenes (70%):           {nota_examenes}")
    print(f"Nota Tareas (30%):             {nota_tareas}")
    print("      " )
    print(f"Nota Final:                    {nota_final}")
    print(f"Estado Académico:              {estado_academico}")
    print(f"Nota Mínima Aprobatoria:       {nota_minima}")
    print(f"¿Presenta Examen Extraordinario? {necesita_extraordinario}")
 
#ejemplo
if __name__ == "__main__":
   
    generar_boleta("Luis Roberto", 9.5, 9.0)

    print("\n")

    generar_boleta("Pepe el mago", 5.0, 8.5)