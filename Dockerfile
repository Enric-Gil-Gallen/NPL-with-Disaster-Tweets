# Usamos una imagen base con la versión específica de Python que necesitamos
FROM python:3.8.18

# Establecer directorio de trabajo
WORKDIR /usr/src/NPL-WITH-DISASTER-TWEETS

# Copiar el archivo de requisitos
COPY requirements.txt ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación
COPY . .