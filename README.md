Python diseñado para extraer y procesar datos de sensores* almacenados en archivos de texto planos. El objetivo principal es automatizar la lectura de datos como *temperatura, humedad y presión* de logs generados por dispositivos (microcontroladores como ESP32 con MicroPython) y organizarlos en estructuras de datos accesibles para su análisis o visualización.

Las primeras ´N´ líneas pueden ser ignoradas. El número de líneas de encabezado se especifica al llamar a la función.
Cada línea de datos debe contener la siguiente información, separada por comas:
*Fecha y Hora:*En formato `AAAA-MM-DD_HH-MM-SS`.
*Temperatura:* Valor numérico flotante.
*Humedad:* Valor numérico flotante.
*Presión:* Valor numérico flotante.
Una vez que la función "extraer" ha sido ejecutada, los datos procesados se almacenan en las siguientes listas globales:

"fecha": Lista de cadenas con las fechas `['2023-10-26', '2023-10-26']`.
"hora": Lista de cadenas con las horas  `['10-30-00', '10-35-00']`.
"temperatura": Lista de números flotantes con los valores de temperatura.
"humedad": Lista de números flotantes con los valores de humedad.
"presion": Lista de números flotantes con los valores de presión.
pythoon
