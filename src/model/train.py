import pandas as pd
from sklearn.ensemble import IsolationForest
from src.preprocessing import to_dataframe

def train_model(data_csv: str = "data/events.csv", model_out: str = "model.pkl"):
    df = pd.read_csv(data_csv)
    features = df[["ip", "result", "user_agent"]]  # transform them appropriately
    # example: encode categorical, engineer time features…
    clf = IsolationForest(contamination=0.01)
    clf.fit(features)
    import joblib; joblib.dump(clf, model_out)
    print("Model saved to", model_out)
