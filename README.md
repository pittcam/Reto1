# Integrantes
1. Maikol Vergara
2. Juliana Castro

# Taller de Búsqueda de Datos Binaria y Secuencial

Este proyecto en Python se centra en la implementación y comparación de dos técnicas de búsqueda: la búsqueda binaria y la búsqueda secuencial. El objetivo principal es analizar y evaluar el rendimiento de ambas técnicas en la búsqueda de información en un censo ficticio de personas, con el propósito de determinar cuál de ellas es más eficiente.

# Funcionalidades
1. Generación aleatoria de un censo de personas con información como ID, nombre, edad y si paga impuestos.
2. Búsqueda binaria de personas por ID en el censo.
3. Búsqueda secuencial de personas por nombre en el censo.
4. Comparación de los tiempos de búsqueda entre búsqueda binaria y búsqueda secuencial para analizar su eficiencia.
5. Visualización de estadísticas de tiempo promedio de búsqueda.

# Uso
1. Ejecuta el programa e ingresa la cantidad de personas que deseas registrar en el censo.
2. Selecciona una opción del menú para realizar consultas por ID o por nombre en el censo.
3. Observe y compare los tiempos de búsqueda entre búsqueda binaria y búsqueda secuencial para analizar su eficiencia.
4.Visualiza las estadísticas para obtener información sobre el rendimiento de ambas técnicas.
5. Explora los primeros y últimos 20 registros del censo para comprender mejor la distribución de los datos.

# Resultados
Este proyecto proporciona una herramienta para analizar y comparar el rendimiento de las búsquedas binarias y secuenciales en un contexto práctico. Los resultados se presentan en forma de estadísticas que muestran el tiempo promedio de búsqueda para cada técnica, lo que permite una evaluación detallada de su eficiencia.

# Ejemplo
    
![image](https://github.com/pittcam/Reto1/assets/54080930/b883baca-b039-49aa-991c-384ac605f0bd)

En el gráfico, podemos ver que los tiempos de la búsqueda binaria (representada por los círculos azules) son consistentemente bajos y se mantienen relativamente constantes independientemente del número de consulta. Esto es indicativo de la eficiencia de la búsqueda binaria, que no se ve fuertemente afectada por la posición del elemento objetivo dentro de la lista debido a su estrategia de división del espacio de búsqueda.

En contraste, los tiempos de la búsqueda secuencial (representados por las cruces naranjas) parecen ser extremadamente bajos, casi en la línea del eje x, lo que sugiere que los tiempos de ejecución son mucho menores que los de la búsqueda binaria para este conjunto particular de datos. Esto es atípico, ya que se esperaría que la búsqueda secuencial tuviera tiempos de ejecución más altos, especialmente en listas grandes, debido a su naturaleza lineal.

La conclusión general que se podría sacar de este gráfico, basándose únicamente en la información proporcionada y asumiendo que no hay errores en la medición o en la presentación de los datos, sería que para este conjunto específico de consultas y datos, la búsqueda secuencial es más rápida que la búsqueda binaria, lo cual es inusual.

Sin embargo, esta conclusión es contraintuitiva, y deberíamos cuestionar si hay otros factores en juego, como el tamaño de los datos, la implementación de los algoritmos, el costo de la inicialización o el entorno de prueba. Por ejemplo, si las búsquedas secuenciales siempre encuentran el elemento objetivo al principio de la lista, o si los datos son muy pocos, entonces es posible que los resultados muestren tiempos más bajos para la búsqueda secuencial. Además, si la búsqueda binaria está mal implementada o si el costo de la división es significativamente alto en el contexto de la prueba, esto también podría explicar los resultados.
