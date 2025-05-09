**🚀 How to Get It Running**:

---

```markdown
# ✍️ Handwritten Digit Classifier with Odd/Even Checker

Welcome! This is a simple and fun web app where you can **draw any digit from 0 to 9**, and it will:
1. Predict what digit you wrote using a trained CNN model.
2. Tell you if that digit is **odd** or **even** using some basic logic.

---

## 📦 What's Inside

Here's how everything is organized in the project:

```

HANDWRITTEN\_DIGIT\_CLASSIFIER/
│
├── model/
│   └── digit\_model.h5              # Pre-trained digit recognition model
│
├── static/
│   └── style.css                   # (Optional) CSS for styling
│
├── templates/
│   └── index.html                  # Web interface where you draw digits
│
├── app.py                          # Flask app to run everything
├── model\_training.py               # Trains the digit classifier
├── predict\_and\_classify.py         # Predicts digit and checks if it's odd/even
├── utils.py                        # Extra helper functions for images
├── input.png                       # Temporary image saved from canvas
├── requirements.txt                # List of Python packages needed
└── README.md                       # You're reading it!

````

---

## 🧠 How the Model Works

The digit classifier is built using a **Convolutional Neural Network (CNN)** trained on the MNIST dataset (handwritten digits).

### 📐 Model Architecture
- Takes a 28x28 grayscale image as input.
- Two convolutional layers with ReLU and max pooling.
- Fully connected layer with 64 units.
- Output layer has 10 neurons (0 to 9), with Softmax to pick the most likely digit.

The model is saved as `digit_model.h5` and gets loaded whenever a prediction is needed.

---

## 🔍 How We Check Odd or Even

Once the model predicts a digit, we apply a super simple logic:

```python
parity = "Even" if predicted_digit % 2 == 0 else "Odd"
````

So:

* 2, 4, 8 → Even
* 1, 3, 9 → Odd
  ...and so on!

---

## 🚀 How to Get It Running

### Step 1: Clone the Repository

```bash
git clone [https://github.com/your-username/HANDWRITTEN_DIGIT_CLASSIFIER.git](https://github.com/aryan1112003/HANDWRITTEN_DIGIT_CLASSIFIER)
cd HANDWRITTEN_DIGIT_CLASSIFIER
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train the model (optional)

If `digit_model.h5` already exists, you can skip this.

```bash
python model_training.py
```

### Step 4: Run the web app

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🎥 Demo Video

Watch a full demo of this project here:
👉 [YouTube Video](https://youtu.be/bbZL2fxtNKU)

---

## 🖱️ How to Use the App

1. Draw a digit (0 to 9) on the white box using your mouse or touchpad.
2. Click the **Predict** button.
3. You’ll see the predicted digit and whether it’s odd or even.
4. Click **Clear** to start over and try again!

---

## 👨‍🎨 Created By

> Made with ❤️ by **Aryan Acharya**
> © 2025 — All rights reserved.

---

## ✅ Requirements

This project uses the following Python packages (listed in `requirements.txt`):

* `flask`
* `tensorflow`
* `numpy`
* `pillow`

Make sure these are installed before running the app!
