# 🏡 House Price Prediction App

A simple machine learning project that predicts house prices based on square footage, number of bedrooms, and number of bathrooms. The project uses a **Linear Regression** model built with **scikit-learn** and served via a **Flask** API.

---

## 📂 Project Structure

.
├── app.py # Flask app to serve predictions
├── train_and_save_model.py# Script to train and save the model and imputer
├── model.pkl # Trained Linear Regression model
├── imputer.pkl # Imputer for handling missing values
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Features

- Predicts house price using:
  - ✅ Square footage
  - ✅ Number of bedrooms
  - ✅ Number of bathrooms
- Preprocessing with missing value handling
- Trained using **scikit-learn Linear Regression**
- REST API interface built using Flask

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Dipayan342/CODECRAFT_ML_TASK01
cd house-price-predictor
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Train the model (if not already trained)
bash
Copy
Edit
python train_and_save_model.py
This generates:

model.pkl — the trained regression model

imputer.pkl — preprocessing object to handle missing values

4. Run the application
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

📮 API Usage
🔹 Endpoint
bash
Copy
Edit
POST /predict
🔸 Request Body (JSON)
json
Copy
Edit
{
  "square_footage": 2000,
  "bedrooms": 3,
  "bathrooms": 2
}
🔸 Response
json
Copy
Edit
{
  "predicted_price": 320000.0
}
🧠 Model Details
Algorithm: Linear Regression

Input Features:

Square footage (float)

Bedrooms (int)

Bathrooms (int)

Output: Predicted house price (float)

📦 Requirements
All dependencies are listed in requirements.txt:

text
Copy
Edit
Flask==3.0.2
numpy==1.26.4
pandas==2.2.2
scikit-learn==1.4.2
joblib==1.4.2
Install them with:

bash
Copy
Edit
pip install -r requirements.txt
👤 Author
Dipayan Guha
BCA Graduate | Aspiring Software Developer & Data Analyst
Feel free to connect!

📄 License
This project is licensed under the MIT License.
You can use, modify, and distribute it freely.
