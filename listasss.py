def burbuja(lista):
  # Creamos una copia para no modificar la lista original
  arr = list(lista)
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


def seleccion(lista):
  arr = list(lista)
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


def insercion(lista):
  arr = list(lista)
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr


def quicksort(lista):
  if len(lista) <= 1:
    return list(lista)
  pivot = lista[len(lista) // 2]
  left = [x for x in lista if x < pivot]
  middle = [x for x in lista if x == pivot]
  right = [x for x in lista if x > pivot]
  return quicksort(left) + middle + quicksort(right)


def main():
  print("SISTEMA DE MÉTODOS DE ORDENAMIENTO EN PYTHON")

  # Solicitar la lista inicial al usuario
  try:
    entrada = input(
        "Ingresa los números separados por comas (ej. 9, 3, 7, 1, 4): "
    )
    lista_original = [int(x.strip()) for x in entrada.split(",")]
  except ValueError:
    print(
        "Error: Asegúrate de ingresar únicamente números enteros separados por"
        " comas."
    )
    return

  print(f"Lista original ingresada: {lista_original}")

  while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1.- Ordenar con algoritmo de Burbuja (Bubble Sort)")
    print("2.- Ordenar con algoritmo de Selección (Selection Sort)")
    print("3.- Ordenar con algoritmo de Inserción (Insertion Sort)")
    print("4.- Ordenar con algoritmo QuickSort")
    print("5.- Ingresar una nueva lista de números")
    print("6.- Salir")

    opcion = input("Selecciona una opción (1-6): ").strip()

    if opcion == "1":
      resultado = burbuja(lista_original)
      print(f"Resultado [Bubble Sort]: {resultado}")
    elif opcion == "2":
      resultado = seleccion(lista_original)
      print(f"Resultado [Selection Sort]: {resultado}")
    elif opcion == "3":
      resultado = insercion(lista_original)
      print(f"Resultado [Insertion Sort]: {resultado}")
    elif opcion == "4":
      resultado = quicksort(lista_original)
      print(f"Resultado [QuickSort]: {resultado}")
    elif opcion == "5":
      try:
        entrada = input(
            "Ingresa los números separados por comas (ej. 9, 3, 7, 1, 4): "
        )
        lista_original = [int(x.strip()) for x in entrada.split(",")]
        print(f"Lista original ingresada: {lista_original}")
      except ValueError:
        print(
            "Error: Asegúrate de ingresar únicamente números enteros separados"
            " por comas."
        )
    elif opcion == "6":
      print("¡Saliendo del programa. Hasta luego!")
      break
    else:
      print("Opción inválida. Por favor, selecciona un número entre 1 y 6.")


if __name__ == "__main__":
  main()