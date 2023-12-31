from sklearn.metrics import f1_score, confusion_matrix, precision_score, recall_score, auc, roc_curve, precision_recall_curve, average_precision_score, accuracy_score, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_precision(y_pred, Y_val):
    """
    Calcula y devuelve la precisión.

    Parámetros:
    - y_pred: Predicciones del modelo.
    - Y_val: Etiquetas verdaderas.

    Retorna:
    - precision: Precisión del modelo.
    """
    return precision_score(Y_val, y_pred) 

def calculate_recall(y_pred, Y_val):
    """
    Calcula y devuelve el recall.

    Parámetros:
    - y_pred: Predicciones del modelo.
    - Y_val: Etiquetas verdaderas.

    Retorna:
    - recall: Recall del modelo.
    """
    return recall_score(Y_val, y_pred)

def calculate_accuracy(y_pred, Y_val):
    """
    Calcula y devuelve el accuracy.

    Parámetros:
    - y_pred: Predicciones del modelo.
    - Y_val: Etiquetas verdaderas.

    Retorna:
    - accuracy: Accuracy del modelo.
    """
    return accuracy_score(Y_val, y_pred)

def calculate_f1(y_pred, Y_val):
    """
    Calcula y devuelve el F1 score.

    Parámetros:
    - y_pred: Predicciones del modelo.
    - Y_val: Etiquetas verdaderas.

    Retorna:
    - f1: F1 score del modelo.
    """
    return f1_score(Y_val, y_pred)

def calculate_auc(y_prob, Y_val):
    """
    Calcula y devuelve el AUC.

    Parámetros:
    - y_prob: Probabilidades de la clase positiva.
    - Y_val: Etiquetas verdaderas.

    Retorna:
    - auc: Área bajo la curva ROC.
    """
    return roc_auc_score(Y_val, y_prob)

def matriz_confusion(y_pred, Y_val):
    """
    Traza la matriz de confusión.

    Parámetros:
    - y_pred: Predicciones del modelo.
    - Y_val: Etiquetas verdaderas.
    """
    # 1. Obtener la matriz de confusión
    cm = confusion_matrix(Y_val, y_pred)
    
    # 2. Graficar la matriz de confusión usando seaborn
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='3g', cmap='Blues', ax=ax)
    ax.set_xlabel('Etiquetas Predichas')
    ax.set_ylabel('Etiquetas Verdaderas')
    ax.set_title('Matriz de Confusión')
    # plt.show()
    return fig

def curva_roc(y_prob, Y_val):
    """
    Traza la curva ROC.

    Parámetros:
    - y_prob: Probabilidades de la clase positiva.
    - Y_val: Etiquetas verdaderas.
    """
    # 1. Calcular la tasa de verdaderos positivos (tvp) y la tasa de falsos positivos (tfp)
    tfp, tvp, _ = roc_curve(Y_val, y_prob)
    
    # 2. Calcular el área bajo la curva (AUC)
    roc_auc = auc(tfp, tvp)
    
    # 3. Graficar la Curva ROC
    fig, ax = plt.subplots()
    ax.plot(tfp, tvp, color='darkorange', label='Curva ROC (área = %0.2f)' % roc_auc)
    ax.plot([0, 1], [0, 1], color='navy', linestyle='--')
    ax.set_xlabel('Tasa de Falsos Positivos')
    ax.set_ylabel('Tasa de Verdaderos Positivos')
    ax.set_title('Curva ROC')
    #plt.show() 

    return fig

def curva_precision_recall(y_prob, Y_val):
    """
    Traza la curva de precisión-recall.

    Parámetros:
    - y_prob: Probabilidades de la clase positiva.
    - Y_val: Etiquetas verdaderas.
    """
    # 1. Calcular precisión y recall para diferentes umbrales
    precision, recall, _ = precision_recall_curve(Y_val, y_prob)

    # 2. Calcular el promedio de precisión
    precision_promedio = average_precision_score(Y_val, y_prob)

    # 3. Graficar la curva de precisión-recall
    fig, ax = plt.subplots()
    ax.plot(recall, precision, label='Curva Precisión-Recall: AP={0:0.2f}'.format(precision_promedio))
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precisión')
    ax.set_title('Curva de Precisión-Recall')
    # plt.show()
    return fig

def evolution_keras_train(dataframe):
    fig, ax = plt.subplots()
    dataframe.plot(ax=ax) 
    ax.grid(True)
    ax.set_ylim(0, 1.2)
    ax.set_xlabel("epochs")

    return fig

