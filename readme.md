# ✍️ Handwritten Digit Classifier with Odd/Even Checker

Welcome! This is a simple and fun web app where you can **draw any digit from 0 to 9**, and it will:
1. Predict what digit you wrote using a trained CNN model.
2. Tell you if that digit is **odd** or **even** using some basic logic.

---

## 📦 Project Structure

```
HANDWRITTEN_DIGIT_CLASSIFIER/
│
├── model/
│   └── digit_model.h5              # Pre-trained CNN model for digit recognition
│
├── static/
│   └── style.css                   # CSS for the web interface
│
├── templates/
│   └── index.html                  # Main UI for drawing digits
│
├── app.py                          # Flask web server
├── model_training.py               # Script to train the CNN model
├── predict_and_classify.py         # Predict digit and check if odd/even
├── utils.py                        # Image processing and helper functions
├── input.png                       # Temporary canvas image
├── requirements.txt                # Required Python packages
└── README.md                       # Project documentation
```

---

## 🧠 How the Model Works

The digit classifier is built using a **Convolutional Neural Network (CNN)** trained on the MNIST dataset.

### 📐 Model Architecture
- Input: 28x28 grayscale image
- Layers:
  - Two convolutional layers (ReLU + MaxPooling)
  - One fully connected dense layer (64 units)
  - Output layer (10 neurons with Softmax)

The trained model is saved as `digit_model.h5` and loaded at prediction time.

---

## 🔍 How We Check Odd or Even

Once the digit is predicted, we use a simple logic:

```python
parity = "Even" if predicted_digit % 2 == 0 else "Odd"
```

So:
- 2, 4, 6, 8 → Even
- 1, 3, 5, 7, 9 → Odd

---

## 🚀 How to Get It Running

### Step 1: Clone the Repository

```bash
git clone https://github.com/aryan1112003/HANDWRITTEN_DIGIT_CLASSIFIER.git
cd HANDWRITTEN_DIGIT_CLASSIFIER
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train the Model (optional)

If `digit_model.h5` is already present, skip this step.

```bash
python model_training.py
```

### Step 4: Run the Web App

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🎥 Demo Video

👉 [Watch on YouTube](https://youtu.be/bbZL2fxtNKU)

---

## 🖱️ How to Use the App

1. Draw a digit (0–9) on the white box.
2. Click **Predict**.
3. The app shows the predicted digit and whether it is odd or even.
4. Click **Clear** to try again.

---

## ✅ Requirements

Make sure you have the following Python packages installed:

- `flask`
- `tensorflow`
- `numpy`
- `pillow`

---

## 👨‍🎨 Created By

> Made with ❤️ by **Aryan Acharya**  
> © 2025 — All rights reserved.
