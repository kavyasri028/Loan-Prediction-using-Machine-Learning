# 🏦 Loan Prediction using Machine Learning

This project uses machine learning techniques to predict whether a loan should be approved based on applicant details such as income, credit history, employment status, and more.

---

## 📌 Project Objective

The goal is to automate the loan approval process using historical data and classification algorithms, helping banks and financial institutions make data-driven decisions.

---

## 📁 Project Structure


Loan_Pred_Project/
├── LOAN_CODE.ipynb                # Main notebook for EDA, model training & evaluation
├── LoanApprovalPrediction.csv     # Cleaned and processed dataset
├── loan_model.pkl                 # Trained ML model (Pickle format)
├── loan_flask_app/
│   ├── app.py                     # Flask API script
│   ├── model/                     # Folder containing pkl model
│   └── templates/
│       └── index.html             # Frontend UI
├── Loan_Prediction.pptx           # Presentation on methodology and results
└── README.md                      # Project documentation


---

## 🧪 Technologies Used

- Python 🐍
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Flask (for web deployment)
- HTML/CSS (for UI)
- Git & GitHub

---

## 🔍 Machine Learning Algorithms

- Logistic Regression
- Decision Trees
- Random Forest
- XGBoost

Model performance was evaluated using:
- Accuracy
- Precision & Recall
- Confusion Matrix
- ROC AUC Curve

---

## 🚀 How to Run the Project

### 1. Clone the Repository

bash
git clone https://github.com/kavyasri028/Loan-Prediction-using-Machine-Learning.git
cd Loan-Prediction-using-Machine-Learning


### 2. Set Up the Environment

bash
pip install -r requirements.txt


If you don’t have a requirements.txt file, you can manually install:

bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost flask


### 3. Run the Flask App

bash
cd loan_flask_app
python app.py


Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🧠 Inputs to the Model

The prediction is based on:

- Gender
- Marital Status
- Dependents
- Education
- Self Employment
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Property Area

---

## ✅ Results

- Achieved *~85% accuracy* using the XGBoost model.
- Deployed via Flask to serve real-time predictions.
- Clean, interactive UI built using HTML and CSS.

---

## 📸 Screenshot

> Add screenshots here if available using the format below:


![App Screenshot](loan_flask_app/static/screenshot.png)


---

## 🙋‍♀ Author

*Kavya Sri Inkollu*  
GitHub: [@kavyasri028](https://github.com/kavyasri028)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Add project README file
