# Markdown
# ✍️ Handwritten Digit Classifier with Odd/Even Checker

This web app lets you **draw any digit (0–9)** in your browser. It will:
- Predict the digit using a trained CNN model.
- Tell you whether it is **odd or even**.


## 📦 Project Structure


HANDWRITTEN\_DIGIT\_CLASSIFIER/
│
├── model/
│   └── digit\_model.h5            # Trained digit recognition model
│
├── static/
│   └── style.css                 # Optional styling
│
├── templates/
│   └── index.html                # Web interface
│
├── app.py                        # Flask app runner
├── model\_training.py             # Script to train the CNN
├── predict\_and\_classify.py       # Prediction + odd/even checker
├── utils.py                      # Helper functions
├── input.png                     # Temp image from canvas
├── requirements.txt              # Required Python packages
└── README.md                     # You're reading it!

````

---

## 🧠 Model Overview

A CNN trained on the **MNIST dataset**:
- Input: 28x28 grayscale image.
- Layers: 2 Conv2D + MaxPooling, followed by Dense layers.
- Output: 10 classes (digits 0–9) using softmax.

---

## 🔍 Odd or Even Logic

```python
parity = "Even" if predicted_digit % 2 == 0 else "Odd"
````

---

## 🚀 Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/aryan1112003/HANDWRITTEN_DIGIT_CLASSIFIER.git
cd HANDWRITTEN_DIGIT_CLASSIFIER
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. (Optional) Train the Model

```bash
python model_training.py
```

### 4. Launch the App

```bash
python app.py
```

Then go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖱️ How to Use

1. Draw a digit (0–9) on the whiteboard.
2. Click **Predict**.
3. The model will display the digit and whether it's odd or even.
4. Use **Clear** to try again.

---

## ✅ Requirements

* `flask`
* `tensorflow`
* `numpy`
* `pillow`

Install using:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Author

**Aryan Acharya**
Made with ❤️ — © 2025

