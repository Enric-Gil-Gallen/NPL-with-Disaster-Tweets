from .text_utils import remove_url, remove_emoji, remove_punctuation, remove_stopwords
from .html_utils import remove_html

def clean_text_field(pandas_dataset):
    """
    Limpia una columna 'text' del dataset de pandas proporcionado, eliminando URLs, HTML, emojis y puntuación.
    
    Parámetros:
    - pandas_dataset (pandas.DataFrame): DataFrame de pandas que contiene una columna 'text' a limpiar.
    
    Retorna:
    - pandas.DataFrame: DataFrame de pandas con la columna 'text' limpiada.
    
    Excepciones:
    - ValueError: Se lanza si el DataFrame no tiene una columna 'text'.
    """
    
    try:
        df = pandas_dataset.copy()

        # Asegurarse de que el DataFrame tiene una columna 'text'
        if 'text' not in df.columns:
            raise ValueError("El DataFrame proporcionado no tiene una columna 'text'.")

        df['text'] = pandas_dataset['text'].apply(remove_url)
        df['text'] = pandas_dataset['text'].apply(remove_html)
        df['text'] = pandas_dataset['text'].apply(remove_emoji)
        df['text'] = pandas_dataset['text'].apply(remove_punctuation)
        df['text'] = pandas_dataset['text'].apply(remove_stopwords)

        return df

    except Exception as e:
        print(f"Error: {e}")
        raise
