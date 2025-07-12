import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
model = pickle.load(open("model/kmeans_model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

st.title("🏦 Customer Segmentation App")

# Input fields
age = st.slider("Age", 18, 70)
income = st.number_input("Monthly Income", min_value=1000, max_value=200000)
total_spent = st.number_input("Total Spent", min_value=0.0)
avg_spent = st.number_input("Average Spend", min_value=0.0)
txn_count = st.number_input("Transaction Count (The number of times a customer made a purchase )", min_value=0)
recency = st.number_input("Recency (Days since last transaction)", min_value=0)

# Predict segment

if st.button("Predict Segment"):
    input_df = pd.DataFrame([[age, income, total_spent, avg_spent, txn_count, recency]],
                            columns=['age', 'income', 'total_spent', 'avg_spent', 'txn_count', 'recency'])
    input_scaled = scaler.transform(input_df)
    segment = model.predict(input_scaled)[0]
    
    # Segment labels and descriptions
    segment_dict = {
        0: {
            "label": "💼 Segment 0: High Income, Low Activity",
            "details": "These customers earn well but don’t use banking services frequently. They might need investment advice, savings schemes, or exclusive offers to re-engage them."
        },
        1: {
            "label": "🧑‍🎓 Segment 1: Young, Medium Spend",
            "details": "Younger customers who spend moderately, often on categories like food, shopping, or subscriptions. Ideal for digital banking promotions or cashback debit cards."
        },
        2: {
            "label": "👵 Segment 2: Senior, Utility Users",
            "details": "Typically older individuals using banking mostly for utility bills or essentials. Promote retirement plans, fixed deposits, or insurance products."
        },
        3: {
            "label": "💰 Segment 3: Heavy Spenders",
            "details": "Frequent, high-value customers who engage actively. Perfect audience for premium credit cards, high-interest savings accounts, or loyalty programs."
        }
    }

    # Display prediction result
    st.success(segment_dict[segment]["label"])
    st.info(segment_dict[segment]["details"])
