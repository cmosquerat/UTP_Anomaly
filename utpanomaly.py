from PIL import Image
import torch
import clip
import cv2
import numpy as np

class UTPAnomaly:
    def __init__(self, model_name="ViT-B/32", label_dict={"Anomaly": [], "Not Anomaly": []}):
        """
        Constructor de la clase UTPAnomaly.

        Args:
        model_name (str): Nombre del modelo de CLIP a cargar. Por defecto es "ViT-B/32".
        label_dict (dict): Diccionario con las categorías "Anomaly" y "Not Anomaly", cada una con su lista de etiquetas.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(model_name, device=self.device)
        self.label_dict = label_dict
        self.all_labels = [label for labels in label_dict.values() for label in labels]
        self.label_indices = {label: idx for idx, label in enumerate(self.all_labels)}

    def get_classification(self, frame):
        """
        Clasifica un frame (imagen) en base a las categorías "Anomaly" y "Not Anomaly".

        Args:
        frame: Una imagen en formato que OpenCV pueda procesar.

        Returns:
        float: Puntuación ponderada indicando la probabilidad de que la imagen sea una anomalía.
        """
        image = self.preprocess(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))).unsqueeze(0).to(self.device)
        text = clip.tokenize(self.all_labels).to(self.device)

        with torch.no_grad():
            logits_per_image, _ = self.model(image, text)
            probabilities = logits_per_image.softmax(dim=-1).cpu().numpy()[0]

        # Calcular la puntuación de anomalía y no anomalía
        anomaly_score = max([probabilities[self.label_indices[label]] for label in self.label_dict["Anomaly"]])
        

        return anomaly_score

# Ejemplo de uso:
# label_dict = {
#     "Anomaly": ["etiqueta1", "etiqueta2"],
#     "Not Anomaly": ["etiqueta3", "etiqueta4"]
# }
# classifier = UTPAnomaly(label_dict=label_dict)
# frame = [aquí iría el frame cargado]
# resultado_anomaly = classifier.get_classification(frame)
