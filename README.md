# 🧠 Customer Segmentation for Personalized Banking Services

This project provides an end-to-end solution to segment banking customers based on their behavior and spending patterns using machine learning, and visualizes these insights using **Power BI** and **Streamlit**. It helps banks like **Goldman Sachs** offer tailored financial services.


---

## 📌 Key Features

- Extracts and processes customer transaction data
- Performs segmentation using **K-Means clustering**
- Visualizes insights in **Power BI**
- Built with:
  - Python 🐍
  - Pandas, NumPy, scikit-learn
  - Streamlit (for web deployment)
  - MySQL (for data storage)
  - Power BI (for visualization)

---
## 📸 Customer Segmentation System 
![App Screenshot](https://github.com/ramashishmaurya/Project-Customer-Segmentation-for-Personalized-Banking-Services/blob/main/Streamlit_page-0002.png)

## Interactive Dashboard Overview
   This interactive dashboard provides a comprehensive view of Customer Segmentation for Personalized Banking Services. Built using Power BI, it allows users to explore customer demographics, spending patterns, preferred payment methods, and income distributions across various segments.
   
## Key Features:
 Gender & Occupation Filters: Dynamically filter customer data based on gender or profession to uncover personalized insights.
 Spending Categories: Visualize how customers allocate their expenses across categories like Bills, Food, Healthcare, Travel, and more.
 
 Customer Distribution by City:
 Understand geographic concentration with a city-wise breakdown of customer count.
 Mode of Payment by Company:
 Analyze which companies (e.g., Paytm, Swiggy, Uber) customers prefer for credit or debit transactions.
 Income Distribution by Occupation: Get insights into average income across different job roles to tailor banking products accordingly.
 
---
## 📸 Dashboard 
![App Screenshot](https://github.com/ramashishmaurya/Project-Customer-Segmentation-for-Personalized-Banking-Services/blob/main/powerbi_page-0001.jpg)

-----



## 🛠️ Tech Stack

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Python      | Backend and ML processing      |
| scikit-learn| Machine learning clustering    |
| Pandas/Numpy| Data wrangling and analysis    |
| MySQL       | Structured data storage        |
| Power BI    | Business visualizations        |
| Streamlit   | User interface & deployment    |

---

## 📦 Requirements

Python version: `3.12.8`  
Required libraries (`requirements.txt`):



---

## <a href ='https://project-customer-segmentation-for-pj24.onrender.com' > This is my project link </a> 

---


## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/ramashishmaurya/Project-Customer-Segmentation-for-Personalized-Banking-Services.git
cd Project-Customer-Segmentation-for-Personalized-Banking-Services

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

