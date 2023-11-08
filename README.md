# Natural Disaster Tweet Classification Project

## Objective

This project aims to develop an artificial intelligence model capable of discerning whether a tweet is related to natural disasters. It utilizes both Machine Learning and Deep Learning techniques and the methodology of MLOps.

`Data Source`: https://www.kaggle.com/vstepanenko/disaster-tweets
    
## Project Structure

- `data`: The primary directory that houses the database and all applied data transformations, serving as the core of our information resources.
- `mlflow`: This directory serves as the centralized repository for experiment tracking and model lifecycle management through MLflow.
- `models`: This is where the trained models are stored, allowing for easy access and efficient local version management.
- `notebooks`: Contains the core of the model development, with detailed notebooks documenting each step of the creation and refinement process.
- `package_utils`: A custom package designed to maximize code reusability, adaptable to the changing needs of the project.
- `DockerFile`: To containerize the development environment and ensure consistency across platforms.

## Development Phases

### Exploratory Data Analysis (EDA)

- `0-Exploration_dataset.ipynb`: In-depth analysis of the data to understand its nature and explore exogenous variables that may enrich our insights, culminating in a comprehensive report.
- `1-Preparacion_dataset.ipynb`: Meticulous data transformations to optimize the quality of information feeding into our models, with intermediate records for later use.

### Machine Learning

- `0-Eleccion_modelo.ipynb`: Preliminary evaluation to determine the most promising algorithm for our model.
- `1-Testeo_modelo.ipynb`: Rigorous testing of different algorithms and a wide range of hyperparameters, with meticulously recorded results in MLflow to facilitate repetition and refinement.

### Deep Learning
- `0-Pruebas_seleccion_hiperparametros.ipynb`: Hyperparameter tuning, testing different architectures.
- `1-Testeo_modelo.ipynb`: Experimentation with various advanced neural network architectures, documenting each step in MLflow.

### Model Interpretability
- `0-interpretability_modelos.ipynb`: Analyze and understand the inner workings of the models.

### API
- `api.py`: A fully operational API that enables efficient POST request handling and result retrieval.
- Additionally, a Dockerfile is included to simplify its deployment and usage.

## Future Implementation Roadmap

- `Web App`: Creation of an interactive web application to democratize the use of the model and enable real-time access.


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Proyecto de Clasificación de Tweets sobre Desastres Naturales

## Objetivo

Este proyecto tiene como meta el desarrollo de un modelo de inteligencia artificial capaz de discernir si un tweet está relacionado con desastres naturales. Utilizando técnicas tanto de Machine Learning como Deep Learning y la metodología de MLOps.

`Funete de datos`: https://www.kaggle.com/vstepanenko/disaster-tweets
    
## Estructura del Proyecto

- `data`: Directorio principal que alberga la base de datos y todas las transformaciones de datos aplicadas, sirviendo como el núcleo de nuestros recursos de información.
- `mlflow`: Este directorio actúa como el repositorio centralizado para el seguimiento de experimentos y la gestión del ciclo de vida de los modelos mediante MLflow.
- `models`: Aquí se almacenan los modelos entrenados, permitiendo un acceso fácil y una gestión eficiente de las versiones locales.
- `notebooks`: Contiene el núcleo del desarrollo del modelo, con notebooks detallados que documentan cada paso del proceso de creación y afinamiento del modelo.
- `package_utils`: Un paquete personalizado diseñado para maximizar la reutilización de código, adaptable a las necesidades cambiantes del proyecto.
- `DockerFile`: Para contenerizar el entorno de desarrollo y asegurar la consistencia a través de las plataformas.

## Fases de Desarrollo

### Análisis Exploratorio de Datos (EDA)

- `0-Exploration_dataset.ipynb`: Profundo análisis de los datos para entender su naturaleza y explorar variables exógenas que puedan enriquecer nuestros insights, culminando con un informe exhaustivo.
- `1-Preparacion_dataset.ipynb`: Transformaciones de datos meticulosas para optimizar la calidad de la información que alimenta nuestros modelos, con registros intermedios para su uso posterior.

### Machine Learning

- `0-Eleccion_modelo.ipynb`: Evaluación preliminar para determinar el algoritmo más prometedor para nuestro modelo.
- `1-Testeo_modelo.ipynb`: Pruebas rigurosas de diferentes algoritmos y una amplia gama de hiperparámetros, con resultados meticulosamente registrados en MLflow para facilitar la repetición y el refinamiento.

### Deep Learning

- `0-Pruebas_seleccion_hiperparametros.ipynb`: Hypertuning, prueba de distintas arquitecturas.
- `1-Testeo_modelo.ipynb`: Experimentación con diversas arquitecturas de redes neuronales avanzadas, documentando cada paso en MLflow.

### Interpretabilidad del modelo

- `0-interpretability_modelos.ipynb`: Analizar y comprender el funcionamiento interno de los modelos.

### API
- `api.py: API totalmente funcional que permite realizar solicitudes POST y obtener resultados de manera eficiente.
- Además, se incluye un Dockerfile diseñado para facilitar su uso y despliegue sin complicaciones.
  
## Roadmap de Implementaciones Futuras

- `Web App`: Creación de una aplicación web interactiva para democratizar el uso del modelo y permitir su acceso en tiempo real.
