# 0 - Librerías
from fastapi import FastAPI
import uvicorn  # No es necesario importar uvicorn aquí si se va a correr con `uvicorn.run()` desde la línea de comandos.
from pydantic import BaseModel
from joblib import load
from pathlib import Path

# 1 - Creación de la app, el modelo y vectorizer
app = FastAPI()

model_path = Path(__file__).parent / '..' / 'models' / '1_LogisticRegression.joblib'
model = load(model_path)

vectorizer_path = Path(__file__).resolve().parent.parent / 'data' / 'modifications' / 'TfidfVectorizer' / 'vectorizer_TfidfVectorizer.joblib'
vectorizer = load(vectorizer_path)

# 2 - Validación de datos
class Tweet_BaseModel(BaseModel):
    tweet: str

# 3 - Funciones
@app.get('/')
def index():
    return {'tweet': 'Introduce /docs para poder ejecutar'}

@app.post('/predict')
def predict(tweet: Tweet_BaseModel):
    # Preparar datos
    vectorized_data = vectorizer.transform([tweet.tweet])  # Se debe pasar una lista al transform y acceder al atributo de la instancia.
    vectorized_data = vectorized_data.toarray()  # La variable 'info' no está definida, debería ser 'vectorized_data'.

    # Generar predicciones
    predictions = model.predict(vectorized_data)  # No se debe indexar 'predictions' como si fuera un diccionario.
    return {'prediction': predictions.tolist()}  # Convertir las predicciones a lista para que sean serializables por JSON.

# Esta parte se utiliza para ejecutar el servidor directamente desde el script.
# Es una práctica común para pruebas, pero para producción, se debería ejecutar uvicorn desde la línea de comandos.
if __name__ == '__main__':
    #uvicorn.run(app, host='127.0.0.1', port=8000)
    config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, loop="asyncio", reload=True)
    server = uvicorn.Server(config)
    server.run()
