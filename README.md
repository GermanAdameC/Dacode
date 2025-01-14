Se encontraron distintos retos, los cuales algunos se abordan de cierta manera, sin embargo puede no ser la solucion final
Retos encontrados:
1. Como se sugirio en la instrucciones, se utilizaron librerias como requests con la cual no se podia acceder a los archivos html(se probo configurar headers etc..), por lo que tambien se realizaron intentos como con la libreria Selenium con la cual si se pudo acceder a las urls sin embargo no se recuperaban toda la estructura del archivo.
2. Como tuve conflictos para poder acceder directamente mediante las librerias propuestas, presento esta solucion. Presento una forma que en base a investigacion y a un analisis de la estructura de los archivos propongo.

 Se describe cada detalle en el codigo para su facil lectura y entendimiento.

Descripcion de la solución presentada:
Si bien se mantiene la idea principal, se abordo de distinta manera la solución.
Para generar los archivos parquet se definieron las secciones solicitadas:
Estado de Resultados (CONSOLIDATED STATEMENTS OF OPERATIONS)
Balance General (CONSOLIDATED BALANCE SHEETS)
Estado de Flujos de Efectivo (CONSOLIDATED STATEMENTS OF CASH FLOWS)
En estas secciones, se escogieron ciertos campos de los cuales se iban a extraer valores e iban a ser parte de las tablas finales en la base de datos.
En lugar de generar un archivo parque por cada html, se decidio generar un archivo parquet por cada seccion y cada año, con este enfoque, se iban a generar tres tablas en la base de datos, en las cuales se iban a insertar los datos de cada seccion de los años procesados. Con esto se iba a lograr un mejor manejo de los datos y un analisis mas sencillo.

Pasos para replicar el proyecto realizado

1. Se requiere instalación previa de python y algunas librerias necesarias.
   Una vez descargado python, puede proceder a instalar las librerias. Puedes instalar las librerias con el siguiente comando bash: pip install beautifulsoup4 pandas pyarrow requests

2. Ubiquese en el path raiz del proyecto: Dacode/

3. Ejecute el script download_html_files.py para descargar los archivos html con el comando:
   python scripts/download_html_files.py

4. Ejecute el script parse_and_transform.py para parsear los datos con el comando:
   python scripts/parse_and_transform.py

5. Ejecute el script load_to_sqlite.py para cargar los datos procesados en la base de datos con el comando:
   python scripts/load_to_sqlite.py

6. Ejcute el script analysis.py para generar resultados con el comando:
   python scripts/analysis.py
