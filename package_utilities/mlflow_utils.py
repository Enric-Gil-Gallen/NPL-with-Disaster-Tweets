import os
import mlflow


# Métodos para cargar datos mas fácilmente
import os
import mlflow

def log_model(model, name):
    """
    Registrar un modelo específico en MLflow.

    Parámetros:
    - model: Modelo a registrar.
    - name: Nombre con el que se registrará el modelo.

    Retorna:
    - None
    """
    mlflow.sklearn.log_model(model, name)

def log_params(params):
    """
    Registrar múltiples parámetros en MLflow.

    Parámetros:
    - params: Diccionario de parámetros a registrar.

    Retorna:
    - None
    """
    mlflow.log_params(params)

def log_metrics(metrics, prefix):
    """
    Registrar múltiples métricas en MLflow con un prefijo específico.

    Parámetros:
    - metrics: Diccionario de métricas a registrar.
    - prefix: Prefijo para las métricas (e.g. 'train', 'val').

    Retorna:
    - None
    """
    for key, value in metrics.items():
        mlflow.log_metric(f"{prefix} - {key}", value)

def log_plot(figure, name, temp_dir="temp_mlflow"):
    """
    Registrar una figura/gráfico en MLflow.

    Parámetros:
    - figure: Figura o gráfico a registrar.
    - name: Nombre con el que se registrará la figura.
    - temp_dir (opcional): Directorio temporal para guardar la figura antes de registrarla. Por defecto, "temp_mlflow".

    Retorna:
    - None
    """
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    temp_path = os.path.join(temp_dir, name)
    figure.savefig(temp_path, format="png")
    mlflow.log_artifact(temp_path, name)
    os.remove(temp_path)
