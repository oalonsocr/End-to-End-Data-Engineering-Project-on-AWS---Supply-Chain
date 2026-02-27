# Supply Chain Lakehouse en AWS

📌 Descripción del Proyecto

Este proyecto implementa una arquitectura Lakehouse moderna en AWS para el procesamiento y análisis de datos de Supply Chain, aplicando el patrón Medallion (landing, processed, Gold).

Se diseñó una solución serverless, escalable y orquestada, que permite transformar datos operacionales de manufactura en información analítica lista para la toma de decisiones estratégicas mediante dashboards en Power BI.

---

🎯 Objetivo

Diseñar e implementar un pipeline de datos end-to-end que:

    - Ingesta datos operacionales de Supply Chain
    - Aplica procesos de limpieza y transformación
    - Construye una tabla fact optimizada para análisis
    - Orquesta automáticamente el flujo de procesamiento
    - Implementa monitoreo y notificaciones
    - Permite análisis en tiempo real desde Power BI

---

🏗 Arquitectura Implementada

La solución sigue un enfoque Lakehouse desacoplado y basado en servicios serverless.

Servicios utilizados:

    - Amazon S3 – Almacenamiento por capas (Raw, Silver, Gold)
    - AWS Glue – Transformaciones con PySpark
    - Amazon Athena – Motor de consultas SQL serverless
    - AWS Step Functions – Orquestación del pipeline
    - Amazon SNS – Notificaciones y monitoreo
    - AWS Identity and Access Management – Control de accesos y seguridad
    - Power BI – Visualización y análisis

---

🥉 Arquitectura Medallion

- Capa Bronce (Landing)

       - Almacena datos originales sin transformación
       - Formato CSV
       - Datos inmutables

- Capa Silver (Processed)

       - Limpieza de datos
       - Manejo de nulos
       - Estandarización de tipos
       - Aplicación de reglas de negocio
       - Procesamiento realizado con PySpark en AWS Glue.

- Capa Gold (Gold)

       - Construcción de tabla analítica fact_supply_chain
       - Datos agregados y optimizados
       - Almacenamiento en formato Parquet
       - Preparada para consumo analítico

---

📊 Modelo Analítico – fact_supply_chain

La tabla Gold contiene métricas clave de manufactura y rentabilidad:

     - product_type
     - units_sold
     - revenue_generated
     - manufacturing_costs
     - manufacturing_efficiency
     - lead_time_status

Permite analizar:

     - Rentabilidad por tipo de producto
     - Eficiencia de manufactura
     - Distribución de tiempos de entrega
     - Relación entre volumen y revenue

---

🔄 Orquestación y Monitoreo

El pipeline es orquestado mediante:

👉 AWS Step Functions

Características implementadas:

     - Ejecución secuencial Silver → Gold
     - Retry con backoff exponencial
     - Manejo de errores con Catch
     - Flujo de éxito y fallo

Las notificaciones se envían mediante:

👉 Amazon SNS

     - Correo en caso de éxito
     - Correo en caso de error

🔐 Seguridad

   - Se implementó control de acceso mediante:

👉 AWS Identity and Access Management

     - Aplicando el principio de mínimo privilegio:
     - Rol de ejecución para Glue
     - Rol de orquestación para Step Functions
     - Usuario IAM dedicado para conexión Power BI–Athena
     - Permisos restringidos sobre S3 y Data Catalog

---

📈 Visualización

La capa Gold es consultada mediante:

👉 Amazon Athena

Power BI se conecta a Athena vía ODBC, permitiendo dashboards con:

     - KPI de ingresos totales
     - Costos de manufactura
     - Margen operativo
     - Eficiencia promedio
     - Distribución de lead time
     - Análisis por tipo de producto

🚀 Características Técnicas Destacadas

     ✔ Arquitectura Lakehouse
     ✔ Modelo Medallion
     ✔ Procesamiento distribuido con PySpark
     ✔ Formato optimizado Parquet
     ✔ Orquestación serverless
     ✔ Manejo de errores productivo
     ✔ Monitoreo automatizado
     ✔ Seguridad basada en IAM
     ✔ Integración con herramienta BI externa

---

🧠 Aprendizajes Clave

     - Diseño de arquitectura desacoplada y escalable
     - Implementación de pipelines productivos con manejo de errores
     - Aplicación de principios de seguridad en la nube
     - Modelado de datos orientado a analítica
     - Integración de servicios AWS con herramientas de BI


---

📌 Posibles Mejoras Futuras

    - Implementar particionamiento dinámico en Gold
    - Carga incremental
    - Infraestructura como código (Terraform)
    - CI/CD para despliegue automatizado
    - Data Quality checks automatizados
    

---

👨‍💻 Autor

     - Omar Alonso Cuadros Román
       Data Engineer
