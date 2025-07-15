from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open('../mf_surrogates/mf_surrogate_model.pkl', 'rb') as f:
    mf_model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X = [[data['NH3_ratio'], data['H2_ratio']]]
    prediction = mf_model.predict(X)[0][0]
    return jsonify({'predicted_NOx': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
