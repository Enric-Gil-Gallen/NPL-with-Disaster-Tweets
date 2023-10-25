# Imports
import re
import string
import nltk
from nltk.corpus import stopwords

# Constantes 
__URL = "https?://\S+|www\.\S+''"

# Metodos

def remove_url(text):
    """
    Elimina todas las URLs de una cadena de texto dada.
    
    Parámetros:
    text (str) -- La cadena de texto de la que se quieren eliminar las URLs.
    
    Retorna:
    str: Una cadena de texto sin URLs.
    
    Ejemplo:
    >>> remove_url("Visita https://www.ejemplo.com para más información.")
    'Visita  para más información.'
    """
    
    url = re.compile(__URL)
    return url.sub(r'', text)

def remove_emoji(text):
    """
    Elimina todos los emojis de una cadena de texto dada.
    
    Parámetros:
    text (str) -- La cadena de texto de la que se quieren eliminar los emojis.
    
    Retorna:
    str: Una cadena de texto sin emojis.
    
    Ejemplo:
    >>> remove_emoji("Hola 😃")
    'Hola '
    """
    
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_punctuation(text):
    """
    Elimina todos los signos de puntuación de una cadena de texto dada.
    
    Parámetros:
    text (str) -- La cadena de texto de la que se quieren eliminar los signos de puntuación.
    
    Retorna:
    str: Una cadena de texto sin signos de puntuación.
    
    Ejemplo:
    >>> remove_punctuation("¡Hola, mundo!")
    'Hola mundo'
    """
    
    return text.translate(str.maketrans('', '', string.punctuation))

import nltk
from nltk.corpus import stopwords

def remove_stopwords(text):
    """
    Elimina las stopwords en inglés del texto proporcionado.

    Args:
    - text (str): El texto del cual se desean eliminar las stopwords.

    Returns:
    - str: El texto sin las stopwords.

    Raises:
    - Exception: Si las stopwords de nltk no están descargadas y no se pueden descargar.
    """
    # Verifica si las stopwords están descargadas
    if not nltk.data.find('corpora/stopwords'):
        try:
            nltk.download('stopwords')
        except:
            raise Exception("No se pudo descargar las stopwords de nltk. Verifica tu conexión a internet y reintenta.")
    
    stopwords_set = set(stopwords.words('english'))
    
    text = text.lower()  # Convertir el texto a minúsculas
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords_set]
    return ' '.join(filtered_words)
