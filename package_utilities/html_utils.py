from html.parser import HTMLParser

class HTMLStripper(HTMLParser):
    """
    Un parser que extiende de HTMLParser para eliminar etiquetas HTML 
    y obtener solo el contenido visible de una cadena HTML.
    
    Atributos:
    fed (list of str): Lista que almacena fragmentos de texto no etiquetado.
    
    Métodos:
    handle_data(d): Agrega fragmentos de texto no etiquetado a la lista `fed`.
    get_data(): Retorna el contenido visible completo sin etiquetas HTML.
    """
    
    def __init__(self):
        """
        Inicializa el HTMLStripper.
        """
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []
        
    def handle_data(self, d):
        """
        Agrega fragmentos de texto no etiquetado a la lista `fed`.
        
        Parámetros:
        d (str): Fragmento de texto no etiquetado.
        """
        self.fed.append(d)
        
    def get_data(self):
        """
        Retorna el contenido visible completo sin etiquetas HTML.
        
        Retorna:
        str: Texto sin etiquetas HTML.
        """
        return ''.join(self.fed)

def remove_html(text):
    """
    Elimina las etiquetas HTML de una cadena de texto dada y retorna solo el contenido visible.
    
    Parámetros:
    text (str) -- La cadena de texto que contiene etiquetas HTML.
    
    Retorna:
    str: Una cadena de texto sin etiquetas HTML.
    
    Ejemplo:
    >>> remove_html("<p>Hola, mundo!</p>")
    'Hola, mundo!'
    """
    
    s = HTMLStripper()
    s.feed(text)
    return s.get_data()
