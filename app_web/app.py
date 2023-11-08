# 0 - Libraries
from flask import Flask, request, render_template, jsonify
from joblib import load
from pathlib import Path

# 1 - Create app, load model and vectorizer
app = Flask(__name__)

# Use absolute path for robustness
model_path = Path(__file__).parent / '..' / 'models' / '1_LogisticRegression.joblib'
model = load(model_path)

vectorizer_path = Path(__file__).resolve().parent.parent / 'data' / 'modifications' / 'TfidfVectorizer' / 'vectorizer_TfidfVectorizer.joblib'
vectorizer = load(vectorizer_path)

# 2 - Functions
@app.route('/')
def home():
    # Render the home page
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    if request.method == 'POST':
        tweet_text = request.form['tweet']

        # Prepare data
        vectorized_data = vectorizer.transform([tweet_text])  # Transform the input
        vectorized_data = vectorized_data.toarray()  # Convert to array

        # Generate predictions
        prediction = model.predict(vectorized_data)
        prediction_label = int(prediction[0])  # Corrected from 'prediction.Label[0]'
        res = "Habla de catástrofes" if prediction_label == 0 else "No habla de catástrofes"

        print(res)
        # Output
        return render_template('home.html', pred=res)

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get data from API request
    data = request.get_json(force=True)
    text = data['tweet']  # Assuming the JSON has a 'text' field

    # Prepare data
    vectorized_data = vectorizer.transform([text])  # Transform the input
    vectorized_data = vectorized_data.toarray()  # Convert to array

    # Generate predictions
    prediction = model.predict(vectorized_data)
    output = int(prediction[0])  # Corrected from 'prediction.Label[0]'
    return jsonify(output)

if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0', port=5000)
