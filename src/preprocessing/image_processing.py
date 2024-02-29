import cv2
import numpy as np
from skimage.feature import local_binary_pattern

def extract_features_from_image(image_path):
    # Carica immagine
    image = cv2.imread(image_path)
    # Conversione in scala di grigi
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calcolo dell'istogramma
    hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
    hist_features = hist.flatten()
    
    # Calcolo del Local Binary Pattern (LBP)
    radius = 3  # Raggio per LBP
    n_points = 8 * radius  # Numero di punti da considerare intorno a un pixel
    lbp = local_binary_pattern(gray_image, n_points, radius, method="uniform")
    (lbp_hist, _) = np.histogram(lbp.ravel(),
                                 bins=np.arange(0, n_points + 3),
                                 range=(0, n_points + 2))
    # Normalizzazione dell'istogramma LBP
    lbp_hist = lbp_hist.astype("float")
    lbp_hist /= (lbp_hist.sum() + 1e-6)
    
    # Combinazione delle features
    features = np.hstack([hist_features, lbp_hist])
    
    return features

if __name__ == "__main__":
    image_path = "path/to/your_image_file.png"
    features = extract_features_from_image(image_path)
    print(features)
