from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load('loan_model.pkl')

# Mapping dictionaries
gender_map = {'Male': 1, 'Female': 0}
married_map = {'Yes': 1, 'No': 0}
education_map = {'Graduate': 1, 'Not Graduate': 0}
self_employed_map = {'Yes': 1, 'No': 0}
credit_history_map = {'Yes': 1, 'No': 0}
property_area_map = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        gender = gender_map.get(request.form.get('Gender'))
        married = married_map.get(request.form.get('Married'))
        dependents_raw = request.form.get('Dependents')
        education = education_map.get(request.form.get('Education'))
        self_employed = self_employed_map.get(request.form.get('Self_Employed'))
        applicant_income = request.form.get('ApplicantIncome')
        coapplicant_income = request.form.get('CoapplicantIncome')
        loan_amount = request.form.get('LoanAmount')
        loan_term = request.form.get('Loan_Amount_Term')
        credit_history = credit_history_map.get(request.form.get('Credit_History'))
        property_area = property_area_map.get(request.form.get('Property_Area'))

        # Check if any required numeric fields are missing
        required_fields = [applicant_income, coapplicant_income, loan_amount, loan_term]
        if any(field is None or field.strip() == "" for field in required_fields):
            return render_template('index.html', prediction="Please fill in all the numeric fields.")

        # Clean and convert numeric values
        dependents = int(dependents_raw.replace('3+', '3'))
        applicant_income = float(applicant_income)
        coapplicant_income = float(coapplicant_income)
        loan_amount = float(loan_amount)
        loan_term = float(loan_term)

        # Input array
        input_data = np.array([[gender, married, dependents, education,
                                self_employed, applicant_income, coapplicant_income,
                                loan_amount, loan_term, credit_history, property_area]])

        # Predict
        prediction = model.predict(input_data)[0]
        result = "Approved ✅" if prediction == 1 else "Rejected ❌"
        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {e}")

import webbrowser
import threading

if __name__ == "__main__":
    # Open browser in a new thread
    def open_browser():
        webbrowser.open_new("http://127.0.0.1:5000")

    threading.Timer(1.5, open_browser).start()  # wait 1.5 seconds then open browser
    app.run(debug=True)
    




