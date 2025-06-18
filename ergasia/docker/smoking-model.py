from flask import Flask, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

app = Flask(__name__)

@app.route('/run-model', methods=['GET'])
def run_model():
    df = pd.read_csv("smoking.csv")

    # Convert categorical columns to numeric
    df = pd.get_dummies(df, drop_first=True)

    if "smoking" not in df:
        return jsonify({"error": "Missing 'smoking' column"}), 500

    X = df.drop(columns=["smoking"])
    y = df["smoking"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)

    return jsonify({
        "accuracy": acc,
        "report": report
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)