# Creación de la lista inicial:
estudiantes = ["Ana", "Carlos", "Diana"]
print("1 Lista inicial:", estudiantes)

estudiantes.append("Elena")
estudiantes.insert(1, "Beatriz")
print("2 Lista tras inserciones:", estudiantes)

print("\n3 Búsqueda por índice:")
print(f"Estudiante en el índice 0: {estudiantes[0]}")
print(f"Estudiante en el índice 2: {estudiantes[2]}")
indice_diana = estudiantes.index("Diana")
print(f"Diana se encuentra en el índice {indice_diana}")

print("\n4 Resultados de Slicing:")
primeros_tres = estudiantes[:3]
print(f"Primeros 3 estudiantes [:3]: {primeros_tres}")

subgrupo = estudiantes[1:4]
print(f"Subgrupo del índice 1 al 3 [1:4]: {subgrupo}")

ultimos_dos = estudiantes[-2:]
print(f"Últimos dos estudiantes [-2:]: {ultimos_dos}")

invertida = estudiantes[::-1]
print(f"Lista totalmente invertida [::-1]: {invertida}")