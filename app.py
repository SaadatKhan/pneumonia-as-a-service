from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load your model
model = load_model('my_model.h5')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return img_array_expanded_dims / 255.

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('upload.html', error='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', error='No selected file')
        if file and allowed_file(file.filename):
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            
            prepared_image = prepare_image(file_path)
            prediction = model.predict(prepared_image)
            result = prediction[0][0]
            
            probability = result
            diagnosis = 'Pneumonia' if probability > 0.5 else 'Normal'
            os.remove(file_path)
            return render_template('result.html', probability=probability, diagnosis=diagnosis)
    return render_template('upload.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=str(error)), 500

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)
