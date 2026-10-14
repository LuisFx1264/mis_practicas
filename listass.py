# EJERCICIO PRÁCTICO: Gestión de listas y Slicing en Python[span_1](start_span)[span_1](end_span)


estudiantes = ["Ana", "Carlos", "Diana"][span_2](start_span)[span_2](end_span)
print("1. Lista inicial:", estudiantes)[span_3](start_span)[span_3](end_span)


estudiantes.append("Elena")[span_4](start_span)[span_4](end_span)
estudiantes.insert(1, "Beatriz")[span_5](start_span)[span_5](end_span)
print("2. Lista tras inserciones:", estudiantes)[span_6](start_span)[span_6](end_span)


print("3. Búsqueda por índice")[span_7](start_span)[span_7](end_span)
print(f"- Estudiante en el índice 0: {estudiantes[0]}")[span_8](start_span)[span_8](end_span)
print(f"- Estudiante en el índice 2: {estudiantes[2]}")[span_9](start_span)[span_9](end_span)
print(f"- Diana se encuentra en el índice: {estudiantes.index('Diana')}")[span_10](start_span)[span_10](end_span)

print("4. Resultados de Slicing:")[span_11](start_span)[span_11](end_span)
print(f"- Primeros 3 estudiantes [:3]: {estudiantes[:3]}")[span_12](start_span)[span_12](end_span)
print(f"- Subgrupo del índice 1 al 3 [1:4]: {estudiantes[1:4]}")[span_13](start_span)[span_13](end_span)
print(f"- Últimos dos estudiantes [-2:]: {estudiantes[-2:]}")[span_14](start_span)[span_14](end_span)
print(f"- Lista totalmente invertida [::-1]: {estudiantes[::-1]}")[span_15](start_span)[span_15](end_span)