from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import joblib  # Utilizzato per salvare il modello

# Funzione fittizia per caricare i dati
def load_data(data_path, labels_path):
    # Questo è solo un esempio: dovresti caricare i tuoi dati reali qui
    # Potrebbe essere necessario adattare questo a seconda del formato dei tuoi dati
    data = np.random.rand(100, 10)  # 100 esempi, 10 features per esempio
    labels = np.random.randint(2, size=100)  # 100 etichette, per una classificazione binaria
    return data, labels

def train_model(data, labels):
    # Divisione dei dati in set di addestramento e test
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    
    # Definizione del modello
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Addestramento del modello
    model.fit(X_train, y_train)
    
    # Valutazione del modello
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy * 100:.2f}%')
    
    # Salva il modello addestrato
    joblib.dump(model, 'model.pkl')
    print("Modello addestrato e salvato con successo.")

if __name__ == "__main__":
    # Caricare i dati e le etichette
    data_path = "path/to/your_data"
    labels_path = "path/to/your_labels"
    data, labels = load_data(data_path, labels_path)
    
    # Addestramento del modello
    train_model(data, labels)
