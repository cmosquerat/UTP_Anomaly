
# UTPAnomaly

`UTPAnomaly` es una herramienta avanzada para la clasificación de imágenes y videos, diseñada para detectar y categorizar anomalías utilizando el modelo CLIP de OpenAI. Esta herramienta es especialmente útil para aplicaciones que requieren detección de anomalías en contextos variados, como seguridad, monitoreo de tráfico, entre otros.

## Instalación

Las dependencias requeridas para `UTPAnomaly` pueden instalarse mediante el siguiente comando:

```bash
pip install -r requirements.txt
```

Este comando asegura la instalación de todas las bibliotecas y dependencias necesarias para el correcto funcionamiento de `UTPAnomaly`.

## Uso de la Clase `UTPAnomaly`

La clase `UTPAnomaly` se encuentra en el archivo `utpanomaly.py`. Para su importación y uso, se debe proceder de la siguiente manera:

```python
from utpanomaly import UTPAnomaly

# Inicialización de la clase
label_dict = {
    "Anomaly": ["etiqueta1", "etiqueta2"],
    "Not Anomaly": ["etiqueta3", "etiqueta4"]
}
classifier = UTPAnomaly(label_dict=label_dict)

# Clasificación de una imagen
frame = [cargar_frame_aquí]
anomaly_score = classifier.get_classification(frame)
print(f"Puntuación de Anomalía: {anomaly_score}")
```

Este fragmento de código muestra cómo importar la clase `UTPAnomaly` y utilizarla para clasificar un frame de imagen.

## Documentación y Ejemplos

Se proporciona un notebook de Jupyter, `UTPAnomaly.ipynb`, que incluye ejemplos detallados y explicaciones sobre cómo utilizar `UTPAnomaly` para la clasificación de imágenes y videos. Este recurso es recomendado para obtener una comprensión más profunda de las funcionalidades y capacidades de la herramienta.

## Aplicación de Demostración

En el directorio `app`, se encuentra una aplicación de ejemplo que ilustra el uso de `UTPAnomaly` en un contexto de aplicación en tiempo real. La aplicación, nombrada `app.py`, puede ser ejecutada utilizando Streamlit con el siguiente comando:

```bash
streamlit run app/app.py
```

Esta aplicación permite la carga y clasificación de imágenes o videos, facilitando la visualización de los resultados de la detección de anomalías en tiempo real.

Aquí está la sección adicional para el archivo README de `UTPAnomaly`, que incluye los requisitos mínimos y los protocolos de ingreso de datos:

---

## Requerimientos Mínimos y Protocolos de Ingreso de Datos

### Protocolos de Ingreso de Datos

`UTPAnomaly` está diseñado para ser compatible con una amplia variedad de formatos de imagen y video, ya que utiliza OpenCV (`cv2`) para la captura y el procesamiento de frames. Esto significa que cualquier formato de archivo que pueda ser leído por OpenCV puede ser utilizado con `UTPAnomaly`. 

Por ejemplo, para capturar un frame de un video o una transmisión, puede utilizarse el siguiente fragmento de código:

```python
import cv2

# Reemplazar con la ruta del archivo de video o la URL de la transmisión
video_source = 'ruta/a/tu/video.o.transmision'  

cap = cv2.VideoCapture(video_source)
ret, frame = cap.read()

if ret:
    # Procesar el frame con UTPAnomaly
    # ...
else:
    print("Error al capturar el frame.")

cap.release()
```

Este ejemplo muestra cómo utilizar `cv2.VideoCapture` para cargar un video o transmisión y cómo leer un frame del mismo.

### Formatos de Imagen

- JPEG (`.jpg`, `.jpeg`)
- PNG (`.png`)
- BMP (`.bmp`)
- TIFF (`.tiff`, `.tif`)
- WebP (`.webp`)
- PPM, PGM, PBM (`.ppm`, `.pgm`, `.pbm`)
- OpenEXR (`.exr`)

### Formatos de Video

- AVI (`.avi`)
- MP4 (`.mp4`)
- MOV (`.mov`)
- MKV (`.mkv`)
- FLV (`.flv`)
- WMV (`.wmv`)
- MPEG (`.mpeg`, `.mpg`, `.mpe`, `.mpv`, `.m1v`, `.m2v`, `.mp4v`, `.m4v`, `.m4p`, `.mp2v`, `.mp2`, `.m2p`, `.vob`)

### Formatos de Transmisión

- RTSP
- RTMP
- HTTP (para transmisiones basadas en HTTP)



### Requerimientos Mínimos de Hardware y Software

Para un rendimiento óptimo con `UTPAnomaly`, se recomiendan los siguientes requisitos mínimos de hardware y software:

- **Hardware**: 
  - Para cada frame que se desee procesar de manera simultánea, se recomienda al menos un core de CPU.
  - Se sugiere un mínimo de 2 GB de RAM por frame.
  - Por ejemplo, para conectar y procesar datos de 8 cámaras simultáneamente, se recomendaría un equipo con al menos 8 cores de CPU y 16 GB de RAM.

- **Software**: 
  - Se recomienda utilizar un sistema operativo basado en Linux debido a su estabilidad y rendimiento en tareas de procesamiento de imágenes y video.
  - Se aconseja el uso de un entorno virtual de Python (`venv`) para la instalación de dependencias y la ejecución de `UTPAnomaly`. Para crear y activar un `venv`, puede seguirse el siguiente procedimiento:

    ```bash
    python3 -m venv mi_entorno
    source mi_entorno/bin/activate  # En Windows, use mi_entorno\Scripts\activate
    ```

Estos requisitos y protocolos garantizan que `UTPAnomaly` funcione de manera eficiente y confiable en una variedad de entornos y escenarios de uso.

