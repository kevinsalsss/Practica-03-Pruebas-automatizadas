Práctica 03 – Pruebas Automatizadas en Python

Autor: Kevin Salas
Materia: Gestion de calidad de Software**
Fecha: 19/11/2025

📌 Descripción General

Este proyecto desarrolla un analizador de ventas basado en datos del Servicio de Rentas Internas (SRI).
El sistema incluye:

Procesamiento de datos desde un archivo CSV.

Pruebas unitarias automatizadas.

Medición de cobertura con la herramienta coverage.

Entorno virtual aislado.

Documentación profesional del proyecto.

El objetivo principal es aplicar buenas prácticas de desarrollo utilizando herramientas comunes en el ciclo de vida de software moderno.

📂 Estructura del Proyecto

Practica-03-Pruebas-automatizadas/
│
├── app.py
├── datos/
│   └── sri_ventas_2024.csv
├── src/
│   └── procesador.py
├── tests/
│   └── test_procesador.py
├── venv/
├── htmlcov/ 
├── .gitignore
└── README.md

Crear el entorno virtual:
python -m venv venv

Activar el entorno virtual:
En Windows:
venv\Scripts\activate


📦 Instalación de Dependencias

Instalar la herramienta de cobertura dentro del entorno virtual:

pip install coverage

🧪 Ejecución de Pruebas Unitarias

Todas las pruebas se encuentran dentro de la carpeta tests/.
Ejecutar:
python -m unittest discover -s tests

📊 Medición de (Coverage)

Ejecutar coverage sobre los tests:
coverage run -m unittest discover -s tests

Generar un reporte en consola:
coverage report -m
Generar un reporte HTML (visual):
coverage html


Esto crea la carpeta:
htmlcov/
El cual se Puede abrir htmlcov/index.html en tu navegador.

🧠 Descripción de la Lógica Principal
La clase Analizador, ubicada en src/procesador.py, permite:
Cargar y procesar un archivo CSV delimitado por |.
Calcular ventas totales por provincia.
Consultar ventas por provincia específica.
Manejar excepciones para provincias inexistentes.
Ignorar provincias no determinadas (“ND”).
Asegurar que los datos sean válidos antes del procesamiento.

Las pruebas unitarias validan:
Estructura de datos correcta.
Cantidad de provincias.
Ventas mayores a un umbral.
Manejo de errores.
Comportamiento esperado de los métodos públicos.

🚀 Ejecutar la Aplicación

Para ejecutar el programa principal:
python app.py


La aplicación utiliza la clase Analizador para procesar y mostrar resultados del archivo sri_ventas_2024.csv.

📝 Archivo .gitignore
El proyecto ignora correctamente:
Entorno virtual venv/
Carpeta de coverage htmlcov/
Archivo .coverage
Cachés de Python __pycache__/
Configuraciones locales .vscode/
Esto evita subir archivos innecesarios al repositorio.

🧑‍💻 Autor
Kevin Salas