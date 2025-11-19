# README.md – Proyecto 3: Arquitectura Batch para big data
**ST0263 – Tópicos Especiales en Telemática**

**Proyecto 3 – Automatización del proceso de Captura, Ingesta, Procesamiento y Salida de datos** 

**Profesor:** Edwin Nelson Montoya Munera  

**Autores:** 

- Santiago Sanchez Carvajal
- Yasir Enrique Blandon Varela
- Juan Pablo Rúa Cartagema

**GitHub:** [Pocverdn](https://github.com/Pocverdn)

---

## IMPLEMENTACIÓN DE UNA ARQUITECTURA DE INGESTA, PROCESAMIENTO Y ANÁLISIS DE DATOS

---

## 1.	INTRODUCCIÓN

El estudio, tratamiento y análisis de grandes volúmenes de datos se ha convertido en uno de los pilares fundamentales de los sistemas modernos de ingeniería, particularmente en áreas como salud pública, analítica institucional y toma de decisiones basada en evidencia. En este contexto, las arquitecturas de datos distribuidos representan un componente esencial para la administración eficiente de información proveniente de múltiples fuentes externas e internas, permitiendo automatizar procesos de ingesta, integración, transformación y análisis, garantizando a su vez escalabilidad, resiliencia y disponibilidad continua. El presente documento expone el diseño, la construcción y la implementación integral de un sistema distribuido orientado al procesamiento automatizado de datos relacionados con la pandemia de COVID-19 en Colombia. Su propósito fundamental es reproducir un entorno cercano a los que se encuentran en la industria, en donde flujos complejos de información deben ser administrados de manera robusta, sistemática y replicable.

Para ello, el proyecto se fundamenta en una infraestructura distribuida basada en los servicios nativos de Amazon Web Services (AWS), que permiten no solo la automatización completa de los procesos de ingesta de datos, sino también la ejecución de tareas ETL (Extract, Transform, Load) a gran escala en clústeres administrados (EMR). La información proviene de dos grandes tipos de fuentes: datos abiertos del Ministerio de Salud de Colombia, ofrecidos tanto vía archivos descargables como mediante API, y datos provenientes de un motor de base de datos relacional PostgreSQL desplegado en Amazon RDS. Estos conjuntos de datos heterogéneos se integran en un data lake estructurado, permitiendo mantener una organización coherente del ciclo de vida de la información.

La totalidad del sistema fue diseñada bajo el criterio de ejecución automatizada, lo cual implica que, una vez desplegada la infraestructura requerida, los procesos operan sin intervención humana, logrando reproducir un flujo realista de ingeniería de datos profesional. Se emplearon herramientas como AWS Glue, Amazon EMR, Amazon Athena y Amazon S3, que en conjunto conforman una solución coherente para ingestión, catalogación, procesamiento y consulta de datos. Asimismo, se desarrollaron scripts en Python de forma modular, lo que facilita su administración y su ejecución tanto dentro de los servicios AWS como localmente en entornos de desarrollo.

---

## 2. OBJETIVOS DEL PROYECTO


### 2.1 Objetivo General

Diseñar e implementar una arquitectura distribuida que permita ingestión automática, almacenamiento estructurado, procesamiento ETL y análisis avanzado de datos de COVID-19 en Colombia utilizando servicios administrados de AWS.

### 2.2 Objetivos Específicos

•	Capturar datos de COVID-19 desde fuentes externas (API REST y archivos descargables).

•	Ingestar datos relacionales complementarios desde una base de datos RDS (PostgreSQL).

•	Almacenar todos los datos en un data lake en Amazon S3 en su respectiva zona RAW.

•	Ejecutar procesos ETL y analítica avanzada utilizando Spark sobre AWS EMR de forma automatizada.

•	Transformar y enriquecer los datos para almacenarlos en la zona TRUSTED y REFINED.

•	Facilitar consultas analíticas mediante Amazon Athena.

•	Proveer resultados finales almacenados en S3 para consumo por API Gateway o herramientas analíticas.

---


## 3. CONTEXTO GENERAL Y JUSTIFICACIÓN DEL PROYECTO

Durante el desarrollo del presente proyecto se examinaron los distintos procesos que conforman el ciclo de vida de un sistema analítico: captura, ingesta, almacenamiento, procesamiento y entrega de resultados. Aunque en los ejercicios prácticos se trabajó con cantidades limitadas de datos y ejemplos simplificados, la realidad empresarial exige el diseño de soluciones capaces de manejar volúmenes amplios, fuentes diversas y procesos no manuales. Por ello, se definió como objetivo construir un prototipo funcional que reprodujera un flujo de ingeniería de datos real, específicamente orientado al manejo de información epidemiológica.

El caso seleccionado responde a la importancia histórica y analítica de los datos referentes a la pandemia de COVID-19 en Colombia. El Ministerio de Salud ofrece datos públicos actualizados sobre la evolución del virus, disponibles tanto en formato de archivo como por medio de API. 

A su vez, existe información complementaria que puede ser almacenada en motores de bases de datos relacionales, permitiendo enriquecer los análisis y ofrecer una visión integral sobre el comportamiento epidemiológico a nivel departamental y municipal. De esta manera, la diversidad de fuentes permite replicar un escenario genuino de integración de datos heterogéneos.

La elección de AWS responde a su capacidad de ofrecer servicios administrados que facilitan la orquestación de procesos sin necesidad de aprovisionar infraestructura física. A través de Amazon S3 es posible estructurar un data lake altamente escalable; mediante AWS Glue se administra la ingesta automatizada, la catalogación y la ejecución de jobs ETL; por medio de Amazon RDS se emula un sistema transaccional; y con Amazon EMR se realiza el procesamiento distribuido de grandes volúmenes de información. 

Asimismo, Amazon Athena permite realizar consultas SQL directamente sobre los datos almacenados sin necesidad de servidores adicionales. En conjunto, estos servicios posibilitan la construcción de un entorno distribuido robusto, modular y reproducible para fines académicos y profesionales.

---

## 4. ARQUITECTURA GENERAL DEL SISTEMA

La arquitectura implementada consta de los siguientes componentes:

### 4.1 Captura e Ingesta de Datos

•	Fuente 1: API pública del Ministerio de Salud
Endpoint JSON de datos abiertos.

•	Fuente 2: Archivo CSV descargable desde Datos.gov

•	Fuente 3: Base de datos relacional PostgreSQL en AWS RDS

### 4.2 Procesamiento ETL

•	Clúster emr-proyecto3 configurado con Apache Spark.

•	Jobs de Spark ejecutados como Steps automáticos.

•	Transformaciones y enriquecimiento almacenado en la zona TRUSTED.

### 4.3 Análisis Avanzado

•	Script analítica.py para generación de indicadores departamentales.

•	Resultados almacenados en la zona refined.

•	Consultas mediante Athena.

•	Disponibilidad opcional vía API Gateway.

### 4.4 Servicios Utilizados

•	Amazon S3

•	AWS Glue (ETL Jobs, Crawlers, Data Catalog)

•	Amazon RDS / Aurora PostgreSQL

•	Amazon EMR

•	Amazon Athena

•	Amazon API Gateway (opcional)

•	Amazon IAM para roles y permisos

---

## 5. PROCESOS DE INGESTA AUTOMÁTICA DE DATOS

Con el objetivo de garantizar que la captura de datos no dependa de la intervención humana, se desarrollaron tres scripts en Python destinados a la ingesta automática de las fuentes del sistema. Estos scripts fueron almacenados tanto en un bucket especial de AWS Glue como en un repositorio local de trabajo, asegurando la capacidad de edición, despliegue y actualización.

El script datos_api.py establece una conexión directa con el endpoint JSON del Ministerio de Salud utilizando la librería Requests. Desde allí, descarga los datos mediante streaming y sube el contenido sin almacenarlo en disco intermedio, utilizando el cliente de Amazon S3 provisto por Boto3. Este método resulta eficiente al manejar grandes volúmenes, ya que reduce el uso de memoria y garantiza que los datos lleguen íntegramente a la zona RAW.

Por otra parte, el script datos_url.py realiza una tarea equivalente, pero orientada a la descarga del archivo CSV desde la URL pública. En este caso se emplea también Requests en modo streaming, además de la capacidad de cargar directamente el contenido al bucket en formato comprimido (archivos .csv o .gz). La automatización asegura que, incluso si el tamaño del archivo crece con el tiempo, el sistema puede procesarlo sin modificaciones.

El tercer script, rds_s3.py, es ejecutado por un job en AWS Glue específicamente configurado para leer la tabla catalogada correspondiente a la base de datos en RDS. Este script emplea un GlueContext, transforma los datos en un DynamicFrame y los exporta como archivos parquet en la zona RAW. La utilización de Glue permite además conservar los metadatos estructurales en el Data Catalog, donde posteriormente pueden ser consumidos por Athena o por otros procesos.

Para ejecutar automáticamente estos scripts, se configuraron tres Jobs en AWS Glue: descargaAPI, descargaURL y rds-s3. Cada uno se asocia directamente a su respectivo script y efectúa su tarea de forma independiente, garantizando que la ingestión de cada fuente se mantenga actualizada en el tiempo. Adicionalmente, se configuraron dos crawlers en AWS Glue para catalogar tanto los datos provenientes de RDS como los datos ya disponibles en S3, lo que facilita la consulta posterior mediante Athena y la integración en procesos ETL.

---

## 6. PROCESOS AUTOMÁTICOS – AWS GLUE

Se implementaron tres ETL Jobs, cada uno ejecutando un script específico:

### 6.1 Job: descargaURL

•	Ejecuta: datos_url.py

•	Descarga archivo CSV desde Datos.gov.

### 6.2 Job: descargaAPI

•	Ejecuta: datos_api.py

•	Descarga JSON desde la API pública.

### 6.3 Job: rds-s3

•	Ejecuta: rds_s3.py

•	Extrae datos desde RDS utilizando el Glue Data Catalog.

<img width="921" height="500" alt="image" src="https://github.com/user-attachments/assets/1fe7eb12-3560-4614-8af8-0037a0bea8d8" />


---


## 7. PROCESAMIENTO ETL EN APACHE SPARK UTILIZANDO AMAZON EMR

Uno de los elementos centrales del proyecto es el procesamiento distribuido de los datos mediante Apache Spark. Para ello se creó un clúster EMR denominado emr-proyecto3, configurado con las capacidades necesarias para ejecutar jobs de Spark y Steps automatizados. Este clúster se conectó directamente al bucket proyecto3datalake, lo que permitió leer y escribir archivos en las distintas zonas del data lake.

<img width="921" height="498" alt="image" src="https://github.com/user-attachments/assets/aeed0307-fab0-48af-8a41-36a4c407eddf" />

Los procesos ETL desarrollados tienen como finalidad integrar la información proveniente de la API, los archivos CSV y la base de datos relacional, unificándola bajo un esquema coherente para análisis posterior. Esta etapa incluye tareas como limpieza de datos, estandarización de columnas, manejo de valores faltantes, transformación de tipos, enriquecimiento mediante joins con los datos de RDS, generación de métricas preliminares y creación de nuevos campos derivados.

**Instancias creadas:**

<img width="921" height="260" alt="image" src="https://github.com/user-attachments/assets/2987f60c-e5f7-4e15-a079-fbe2cf8c7af3" />


<img width="921" height="267" alt="image" src="https://github.com/user-attachments/assets/cd02a09c-508b-4a00-95ed-b682661f741b" />


El resultado de este proceso se almacena en la zona trusted/ del data lake, específicamente en la carpeta trusted/enriquecido. Allí se generan archivos parquet, optimizando el desempeño de lectura en Spark y Athena. Este formato, ampliamente utilizado en sistemas de ingeniería de datos, permite la división física de columnas, facilitando consultas parciales de alto rendimiento.

---


**8. AWS S3**

**1) Bucket aws-glue-assets-426491406849-us-east-1**
   
Contiene:

•	**Carpeta scripts/**

Guarda todos los scripts ejecutados por los Jobs de Glue.

•	**Carpeta SparkHistoryLog/**

Para almacenamiento del historial de ejecuciones de aplicaciones Spark.

**2) Bucket principal del Data Lake: proyecto3datalake**

Organizado en zonas:

•	**Zona raw/**

<img width="966" height="340" alt="image" src="https://github.com/user-attachments/assets/55b624b9-c66b-4db0-9a9d-9f820c92e762" />

<img width="965" height="272" alt="image" src="https://github.com/user-attachments/assets/596e9f55-179b-4f92-9510-bdee802ce3e4" />

<img width="943" height="265" alt="image" src="https://github.com/user-attachments/assets/86309a4c-1a06-4d47-8e31-f246c5196c45" />

<img width="944" height="290" alt="image" src="https://github.com/user-attachments/assets/aecf6635-d33a-4af2-9775-cbdaf0c6b9d3" />

<img width="969" height="411" alt="image" src="https://github.com/user-attachments/assets/9fa090d7-77da-485e-adce-680998083679" />

•	**Zona trusted/**

<img width="921" height="310" alt="image" src="https://github.com/user-attachments/assets/13f43898-fb57-4d00-9627-f3729e1ac41a" />

<img width="921" height="348" alt="image" src="https://github.com/user-attachments/assets/894dfe1b-b7f3-488d-8ccb-ea0849559be4" />


•	**Zona refined/**

<img width="921" height="283" alt="image" src="https://github.com/user-attachments/assets/6d83f7b5-c998-40f0-b109-842080798e19" />

<img width="921" height="360" alt="image" src="https://github.com/user-attachments/assets/4240cd0b-74b0-4960-8756-8df8c3f5e73c" />

**Otros directorios**

•	jupyter/ → notebooks utilizados en EMR o Studio.

•	scripts/ → Copias locales de los scripts Python.

•	resultados/athenas/ → resultados de consultas ejecutadas en Athena.

---


## 9. COMPONENTES DE BASE DE DATOS

### 9.1 Base de Datos Relacional AWS RDS

**Nombre:** rds-covid

**Tabla principal importada desde pgAdmin:**

casos_municipios

**Campos:**

•	categoria

•	nombre_departamento

•	camas_uci_disponibles

•	poblacion

•	nombre_municipio

•	codigo_divipola


<img width="978" height="547" alt="image" src="https://github.com/user-attachments/assets/89eabb3a-72fd-4433-b4a8-212050c58191" />


### 9.2 Base de Datos en AWS Glue Data Catalog

**Nombre:** db_covid

**Tablas:**

1. covidrds_public_casos_municipios

2. datos-finalesanalisis

**Columnas:**

•	nombre_departamento

•	casos_totales

•	fallecidos_totales

•	tasa_letalidad_pct

•	casos_por_100k_hab

•	promedio_camas_uci


<img width="921" height="479" alt="image" src="https://github.com/user-attachments/assets/fb1eefde-a66e-4ad7-812b-05809b49c2a4" />

---


## 10. ANÁLISIS AVANZADO

Una vez finalizadas las transformaciones y el enriquecimiento de datos, se implementó un proceso analítico mediante un script adicional denominado analítica.py. Este script se encarga de cargar la información desde la zona trusted, procesar los datos departamentales y generar indicadores epidemiológicos relevantes para la interpretación del comportamiento del COVID-19 en Colombia.

Entre los cálculos realizados se encuentran el número total de casos por departamento, el número total de fallecidos, la cantidad de recuperados, el promedio departamental de camas UCI disponibles, la tasa de letalidad expresada en porcentaje y la tasa relativa de casos por cada cien mil habitantes. Para ello, se emplean agregaciones de Spark DataFrames como count, sum y avg, acompañadas del uso de funciones condicionales para discriminar estados de recuperación. Posteriormente, se construye una vista temporal que permite ejecutar consultas por medio de SparkSQL, facilitando la clasificación de los departamentos según diferentes criterios.

El resultado finalmente producido consiste en un conjunto de datos refinados con los diez departamentos que presentan la mayor tasa de casos por habitante. Este archivo es almacenado en la zona refined/ del data lake, en el directorio refined/analisis, nuevamente en formato parquet comprimido. A partir de allí puede ser consumido por Athena o por una API externa según los requerimientos analíticos.

---

## 11. CONSULTAS ANALÍTICAS MEDIANTE AMAZON ATHENA

Athena constituye una herramienta indispensable dentro del flujo, al permitir realizar consultas SQL sobre archivos ubicados en S3 sin la necesidad de motores de base de datos tradicionales. En este proyecto, Athena está asociada al Data Catalog generado por AWS Glue, lo que permite tener tablas definidas con metadatos coherentes, tanto para los datos provenientes de RDS como para los resultados refinados.

El sistema permite consultar directamente tablas como covidrds_public_casos_municipios o datos-finalesanalisis, y generar resultados que luego son almacenados automáticamente en la carpeta resultados/athenas del bucket proyecto3datalake. Esto facilita la explotación final de los datos para informes, visualizaciones o procedimientos externos, y demuestra el valor de un modelo distribuido de consulta sin servidores.


<img width="885" height="406" alt="image" src="https://github.com/user-attachments/assets/90667c6c-a942-43bd-8b30-dd065f59a569" />

---


## 12. EXPLICACIÓN DE SCRIPTS

### 12.1 datos_api.py

**Funcionalidad:**

•	Consumir API REST del Ministerio de Salud.

•	Descargar el JSON en modo streaming para mayor eficiencia.

•	Enviar el contenido directamente a S3 sin guardar en disco.

### 12.2 datos_url.py

**Funcionalidad:**

•	Descargar el archivo CSV publicado por Datos.gov.

•	Utilizar streaming para archivos grandes.

•	Subir el contenido comprimido (.gz) directamente a S3.

### 12.3 rds_s3.py

Este script ejecutado desde Glue:

•	Conecta con la tabla catalogada de RDS.

•	Convierte el resultado en un DynamicFrame.

•	Lo almacena en S3 como Parquet con Snappy.

### 12.4 analítica.py

Realiza la parte analítica:

•	Carga de parquet desde TRUSTED.

•	Agrupaciones y cálculos estadísticos.

•	Consulta SQL para obtener ranking departamental.


---


## 14. CONCLUSIONES

El desarrollo de este proyecto permitió comprender con profundidad la complejidad y relevancia de implementar una arquitectura distribuida para la gestión de datos en un contexto real. La utilización integrada de varios servicios de AWS puso de manifiesto la importancia de elegir adecuadamente las tecnologías que permitan automatizar procesos, manejar volúmenes significativos de información y garantizar la disponibilidad continua de los datos en todas las etapas del flujo. La experiencia adquirida en la ingesta automática desde fuentes heterogéneas confirmó que la combinación de datos abiertos y bases de datos relacionales enriquece significativamente las capacidades analíticas y permite ofrecer una visión más precisa sobre los fenómenos estudiados.

El proyecto evidenció también el papel central que desempeñan los data lakes en la gestión moderna de información, particularmente gracias a su flexibilidad para almacenar datos sin necesidad de esquemas rígidos. La estructuración en zonas RAW, trusted y refined facilita la separación entre las etapas del ciclo de vida de los datos y contribuye a la trazabilidad y calidad del producto final. Del mismo modo, el uso de Amazon EMR y Apache Spark permitió experimentar con procesamiento distribuido a gran escala, demostrando la potencia de estas herramientas para ejecutar tareas ETL y de análisis avanzado sobre conjuntos amplios de datos epidemiológicos.

Asimismo, la integración con AWS Glue y Amazon Athena reveló el papel fundamental de los catálogos de metadatos y los motores de consulta sin servidor, ya que ofrecen una forma eficiente de acceder, explorar y validar los resultados generados por el sistema. La automatización lograda en los procesos de ingesta y transformación aseguró una operación fluida, replicable y confiable, alineada con las prácticas profesionales de la ingeniería de datos. La experiencia completa fortaleció la comprensión de los desafíos reales asociados al manejo de sistemas distribuidos y al diseño de soluciones escalables basadas en la nube.

Finalmente, la construcción conjunta de esta arquitectura permitió al equipo aplicar, en un caso práctico y realista, muchos de los conceptos aprendidos teóricamente, integrando conocimientos de sistemas distribuidos, bases de datos, computación en la nube, procesamiento masivo de datos y analítica.


---


## REFERENCIAS

(https://youtu.be/ZFns7fvBCH4?si=hu5Y34JDB9yY7bsd)

(https://github.com/airscholar/EMR-for-data-engineers/tree/main)




