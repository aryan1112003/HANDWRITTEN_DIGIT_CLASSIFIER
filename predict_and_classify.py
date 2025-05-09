import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

# Load trained model
model = load_model("model/digit_model.h5")

def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')

    img = ImageOps.invert(img)
    img = img.resize((28, 28))

    # Normalize pixel values and reshape
    img = np.array(img).astype(np.float32) / 255.0
    img = img.reshape(1, 28, 28, 1)

    return img

def predict_digit(image_path):
    processed_img = preprocess_image(image_path)

    prediction = np.argmax(model.predict(processed_img), axis=1)[0]
    parity = "Even" if prediction % 2 == 0 else "Odd"

    return prediction, parity
