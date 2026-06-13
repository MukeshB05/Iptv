from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

# 1. Create a new Flask application
app = Flask(__name__)

# 2. Load your trained TensorFlow model
#    Replace 'path/to/your/model' with the actual path to your model file.
#    This could be a .h5 file, a SavedModel directory, etc.
try:
    model = tf.keras.models.load_model('path/to/your/model')
except (IOError, ImportError) as e:
    print(f"Error loading model: {e}")
    model = None

# 3. Define a function to preprocess input data
def preprocess_input(data):
    # This is an example. You'll need to adapt this to your model's specific input requirements.
    # For instance, if your model expects a 28x28 grayscale image, you might need to
    # resize and reshape the input data.
    #
    # Assuming the input `data` is a list of numbers that can be converted to a NumPy array:
    return np.array(data).reshape(1, -1) # Example reshape, adjust as needed

# 4. Create an API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        # Get the JSON data from the request
        data = request.get_json(force=True)

        # Extract the input features from the JSON data
        # The key 'features' is just an example, it should match what you send in your request
        input_data = data['features']

        # Preprocess the input data so it's in the correct format for the model
        processed_data = preprocess_input(input_data)

        # Use the model to make a prediction
        prediction = model.predict(processed_data)

        # Convert the prediction to a list so it can be sent as JSON
        output = {'prediction': prediction.tolist()}

        return jsonify(output)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 5. Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
