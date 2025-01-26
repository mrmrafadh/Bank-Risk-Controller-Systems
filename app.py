import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import pickle
import eda
import data
import model_prediction

# Sidebar Menu
sidebar_choice = st.sidebar.selectbox(
    "Choose a Menu",
    ("Data", "EDA - Visual", "Prediction")
)

# Sidebar 1: Data
if sidebar_choice == "Data":
    data.main()

# Sidebar 2: EDA - Visual
elif sidebar_choice == "EDA - Visual":
    eda = eda.eda_object()

    st.title("EDA & Statistical Visualization")
    st.subheader("EDA")
    eda.plot1()
    st.write('The majority of loan applicants are female.')
    st.divider()
    eda.plot2()
    st.write('The predominant type of loan issued is a Cash Loan.')
    st.divider()
    eda.plot3()
    st.write('The majority of loan applicants are working people.')
    st.divider()
    eda.plot4()
    st.write('The majority of loan applicants are Secondary / Secondary Special.')
    st.divider()
    eda.plot5()
    st.write('A significant number of loan applicants have unspecified occupations, indicating that the occupation feature will not be useful in predicting the target.')
    st.divider()
    eda.plot6()
    st.write('The majority of loan applicants are not defaulters.')
    st.divider()
    st.subheader("Statistical Visualization")
    eda.plot7()
    st.write('This plot is designed to examine the variations and trends in income, credit, and annuity figures.')
    st.divider()
    eda.plot8()
    st.write('This plot is designed to analyze the differences in income, credit, and annuity between defaulters and non-defaulters, to determine if there are any significant variations.')
    st.divider()
    eda.plot9()
    st.write('These features demonstrate significant differences between defaulters and non-defaulters. We can consider these features will play a key roll in classification')
    st.divider()
    eda.plot10()
    st.write('These features demonstrate significant differences between defaulters and non-defaulters. We can consider these features will play a key roll in classification')
    st.divider()
    eda.plot11()
    st.write('These plots are designed to analyze the differences between defaulters and non-defaulters.')


# Sidebar 3: Prediction
elif sidebar_choice == "Prediction":
    st.subheader("Prediction")
    model = model_prediction.PredictionModel()
    model.ui()