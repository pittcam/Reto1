import random
import time
import matplotlib.pyplot as plt

# Lista de 50 nombres colombianos
nombres_colombianos = [
    "Sofía", "Valentina", "Isabella", "Samantha", "Antonia",
    "Emiliano", "Santiago", "Sebastián", "Matías", "Alejandro",
    "Valeria", "Mariana", "Gabriela", "Salomé", "Daniela",
    "Nicolás", "Samuel", "Daniel", "Diego", "Tomás",
    "Lucía", "Natalia", "Martina", "Sara", "Camila",
    "David", "Andrés", "Juan", "José", "Miguel",
    "Laura", "Carolina", "Paola", "Andrea", "Juliana",
    "Carlos", "Fernando", "Sergio", "Felipe", "Esteban",
    "Ana", "Teresa", "Alejandra", "Lorena", "Catalina",
    "Mario", "Gustavo", "César", "Alfredo", "Iván"
]

def generar_nombre():
    """Selecciona un nombre al azar de la lista de nombres colombianos."""
    return random.choice(nombres_colombianos)

def generar_persona(id):
    """Genera un diccionario con los datos de una persona."""
    return {
        'id': id,
        'nombre': generar_nombre(),
        'edad': random.randint(18, 100),
        'paga_impuestos': random.choices([True, False], weights=[75, 25], k=1)[0]
    }

def generar_censo(n):
    """Genera una lista de personas para el censo."""
    return [generar_persona(i) for i in range(n)]

def busqueda_binaria(censo, id_buscado):
  """Realiza una búsqueda binaria por ID en el censo."""
  izquierda, derecha = 0, len(censo) - 1
  while izquierda <= derecha:
      medio = (izquierda + derecha) // 2
      if censo[medio]['id'] == id_buscado:
          return censo[medio]
      elif censo[medio]['id'] < id_buscado:
          izquierda = medio + 1
      else:
          derecha = medio - 1
  return None

def busqueda_secuencial(censo, nombre_buscado):
  """Realiza una búsqueda secuencial por nombre en el censo."""
  for persona in censo:
      if persona['nombre'] == nombre_buscado:
          return persona
  return None

def mostrar_estadisticas(tiempos_binaria, tiempos_secuencial, consultas_realizadas):
  if not tiempos_binaria and not tiempos_secuencial:
      print("No se realizaron consultas aún.")
  else:
      if len(tiempos_binaria) < consultas_realizadas:
          tiempos_binaria.extend([0] * (consultas_realizadas - len(tiempos_binaria)))
      if len(tiempos_secuencial) < consultas_realizadas:
          tiempos_secuencial.extend([0] * (consultas_realizadas - len(tiempos_secuencial)))

      if consultas_realizadas > 0:
          # Calcular el tiempo promedio por consulta
          tiempo_promedio_binaria = sum(tiempos_binaria) / consultas_realizadas
          tiempo_promedio_secuencial = sum(tiempos_secuencial) / consultas_realizadas

          print(f"Tiempo promedio de búsqueda binaria: {tiempo_promedio_binaria:.6f} segundos")
          print(f"Tiempo promedio de búsqueda secuencial: {tiempo_promedio_secuencial:.6f} segundos")

          # Graficar todos los resultados acumulados
          plt.figure(figsize=(10, 5))
          plt.plot(range(1, consultas_realizadas + 1), tiempos_binaria, label='Búsqueda binaria', marker='o')
          plt.plot(range(1, consultas_realizadas + 1), tiempos_secuencial, label='Búsqueda secuencial', marker='x')
          plt.xlabel('Número de Consulta')
          plt.ylabel('Tiempo (s)')
          plt.title('Tiempos de Búsqueda Binaria vs. Secuencial')
          plt.legend()
          plt.show()
      else:
          print("No se han realizado consultas aún.")


def mostrar_censos(censo):
    if len(censo) >= 40:
        print("\nPrimeros 20 censos:")
        for persona in censo[:20]:
            print(f"ID: {persona['id']}, Nombre: {persona['nombre']}, Edad: {persona['edad']}, Paga Impuestos: {persona['paga_impuestos']}")

        print("\nÚltimos 20 censos:")
        for persona in censo[-20:]:
            print(f"ID: {persona['id']}, Nombre: {persona['nombre']}, Edad: {persona['edad']}, Paga Impuestos: {persona['paga_impuestos']}")
    else:
        print("No hay suficientes censos para mostrar.")

def menu(censo):
    tiempos_binaria = []
    tiempos_secuencial = []
    consultas_realizadas = 0
    consultas_por_lote = 500  # Número de consultas por lote

    while True:
        print("\n1. Realizar consultas por ID")
        print("2. Realizar consultas por nombre")
        print("3. Mostrar estadísticas")
        print("4. Mostrar los primeros y últimos 20 censos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Realizar consultas por ID
            cantidad_consultas = int(input("Ingrese la cantidad de consultas por ID a realizar: "))
            for _ in range(cantidad_consultas):
                id_buscado = random.randint(0, len(censo) - 1)
                inicio = time.time()
                resultado = busqueda_binaria(censo, id_buscado)
                fin = time.time()
                tiempo = fin - inicio
                tiempos_binaria.append(tiempo)
                consultas_realizadas += 1
            print(f"Se realizaron {cantidad_consultas} consultas por ID.")
        elif opcion == '2':
            # Realizar consultas por nombre
            cantidad_consultas = int(input("Ingrese la cantidad de consultas por nombre a realizar: "))
            for _ in range(cantidad_consultas):
                nombre_buscado = generar_nombre()
                inicio = time.time()
                resultado = busqueda_secuencial(censo, nombre_buscado)
                fin = time.time()
                tiempo = fin - inicio
                tiempos_secuencial.append(tiempo)
                consultas_realizadas += 1
            print(f"Se realizaron {cantidad_consultas} consultas por nombre.")
        elif opcion == '3':
            if consultas_realizadas > 0:
                mostrar_estadisticas(tiempos_binaria, tiempos_secuencial, consultas_realizadas)
            else:
                print("No se han realizado consultas aún.")
        elif opcion == '4':
            mostrar_censos(censo)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == '__main__':
    n = int(input("Ingrese la cantidad de personas a registrar: "))
    censo = generar_censo(n)
    censo.sort(key=lambda x: x['id'])  # Ordenamos por ID para la búsqueda binaria
    menu(censo)