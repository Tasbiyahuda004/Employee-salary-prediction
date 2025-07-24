EMPLOYEE SALARY PREDICTION SYSTEM

This project aims to build an intelligent system that accurately predicts employee salaries based on various features such as experience, education level, job title, company, and location.
Using machine learning algorithms, the model learns from real-world datasets to estimate salaries and uncover patterns behind compensation.
The system helps job seekers understand their market value and supports HR teams in making data-driven decisions.

📌OVERVIEW

Employee Salary Predictor is a machine learning-based web application that intelligently predicts the expected salary of an employee based on multiple input features such as job title, experience, company, location, and more. The project is designed to assist HR professionals, recruiters, job seekers, and businesses in estimating appropriate compensation benchmarks for different roles. It uses a clean and user-friendly Streamlit interface to take user input, processes it through a trained regression model, and outputs a predicted salary with performance metrics and data visualizations. This tool is a practical example of how machine learning and web apps can be combined to create impactful real-world solutions.

📁PROJECT STRUCTURE(folder structure)
Employee-Salary-Predictor/
│
├── app.py                 # Streamlit web application entry point
├── model.py               # Machine learning model training and pipeline logic
├── employee_data.csv      # Dataset used for training and prediction
├── requirements.txt       # List of required Python packages
├── README.md              # Project documentation
├── .gitignore             # Files and folders to ignore in Git
├── __pycache__/           # Python cache files (can be ignored)
└── assets/                # (Optional) Folder for charts, screenshots, or supporting files

📌FEATURES

🔹Predicts salary based on job-specific details.
🔹Input fields for name, job title, experience, company, and more.
🔹Real-time predictions with user-friendly UI.
🔹Displays performance metrics: R² Score, MAE, MSE
🔹Includes charts for better visualization.
🔹Built with Streamlit for easy web interface.

📌SYSTEM REQUIREMENTS

🔹OS: Windows / macOS / Linux
🔹Python: Version 3.8 or higher
🔹RAM: Minimum 4 GB (8 GB recommended)
🔹Internet: Required for installation and app hosting

📌KEY LIBRARIES USED

🔹pandas – Data handling
🔹numpy – Numerical operations
🔹scikit-learn – Machine learning
🔹joblib – Model serialization
🔹streamlit – Web app interface
🔹matplotlib, seaborn – Visualization

📌ML MODEL & PIPELINE

🔹Regression model used: RandomForestRegressor
🔹Steps include encoding, scaling, and splitting dataset
🔹Model evaluated using R² score, MAE, and MSE
🔹Final model saved as model.joblib for predictions

📌VISUALIZATION & EXPLAINABILITY

🔹Shows bar charts and prediction comparisons
🔹Visual output helps understand model performance
🔹Optional: Add feature importance graphs for interpretability

📌WEB APP FUNCTIONALITY

🔹Inputs: Name, Company, Job Title, Experience, Location, etc.
🔹Button to predict salary in real-time
🔹Output: Predicted salary, charts, and metrics
🔹Simple layout with sidebar and main prediction area

📌HOW TO RUN LOCALLLY

# Step 1: Clone this repo
git clone https://github.com/YourUsername/Employee-Salary-Predictor.git
cd Employee-Salary-Predictor

# Step 2: Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the app
streamlit run app.py

LICENSE

This project is licensed under the MIT License, is created for educational and internship purposes,demonstrating advanced machine learning capabilities in real-world scenario.







