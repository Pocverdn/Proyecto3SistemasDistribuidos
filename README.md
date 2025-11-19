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
