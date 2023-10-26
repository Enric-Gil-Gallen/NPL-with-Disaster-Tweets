from .text_utils import remove_url, remove_emoji, remove_punctuation, remove_stopwords
from .html_utils import remove_html
from .grafics_utils import calculate_precision, calculate_recall, calculate_accuracy, calculate_f1, calculate_auc,  matriz_confusion, curva_roc, curva_precision_recall

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

        df['text'] = df['text'].apply(remove_url)
        df['text'] = df['text'].apply(remove_html)
        df['text'] = df['text'].apply(remove_emoji)
        df['text'] = df['text'].apply(remove_punctuation)
        df['text'] = df['text'].apply(remove_stopwords)

        return df

    except Exception as e:
        print(f"Error: {e}")
        raise

def evaluate_model(y_pred, y_val):
    precision = calculate_precision(y_pred, y_val)
    recall = calculate_recall(y_pred, y_val)
    accuracy = calculate_accuracy(y_pred, y_val)
    f1 = calculate_f1(y_pred, y_val)
    auc = calculate_auc(y_pred, y_val)

    print("Precisión:", precision)
    print("Recall:", recall)
    print("Accuracy:", accuracy)
    print("F1 score:", f1)
    print("AUC:", auc)

    matriz = matriz_confusion(y_pred, y_val)
    roc = curva_roc(y_pred, y_val)
    precision_recall = curva_precision_recall(y_pred, y_val)

    return precision, recall, accuracy, f1, auc, matriz, roc, precision_recall