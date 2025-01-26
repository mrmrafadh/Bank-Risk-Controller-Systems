import streamlit as st
import pandas as pd

def main():
    st.header("📊 Data Display")
    df=pd.read_csv("sample_data/sample_loan_data.csv")


    metrics_knn = {
    'Accuracy on Training Data': [f"{round(0.95, 2):.2f}"],
    'Accuracy': [f"{round(0.91, 2):.2f}"],  
    'Precision': [f"{round(0.93, 2):.2f}"],
    'Recall': [f"{round(0.91, 2):.2f}"],
    'F1 Score': [f"{round(0.91, 2):.2f}"],
    'ROC AUC': [f"{round(0.95, 2):.2f}"]
    }

    metrics_xgb = {
    'Accuracy on Training Data': [f"{round(0.70, 2):.2f}"],
    'Accuracy': [f"{round(0.69, 2):.2f}"],  
    'Precision': [f"{round(0.69, 2):.2f}"],
    'Recall': [f"{round(0.69, 2):.2f}"],
    'F1 Score': [f"{round(0.69, 2):.2f}"],
    'ROC AUC': [f"{round(0.76, 2):.2f}"]
    }

    metrics_rfc = {
    'Accuracy on Training Data': [f"{round(1.00, 2):.2f}"],
    'Accuracy': [f"{round(1.00, 2):.2f}"],  
    'Precision': [f"{round(1.00, 2):.2f}"],
    'Recall': [f"{round(1.00, 2):.2f}"],
    'F1 Score': [f"{round(1.00, 2):.2f}"],
    'ROC AUC': [f"{round(1.00, 2):.2f}"]
    }

    st.subheader("Entire Dataset")
    st.dataframe(df)
    st.write("The dataset contains 1,413,701 Rows and 158 Columns.")
    # List of selected features
    selected_features = [
        'EXT_SOURCE_3', 'EXT_SOURCE_2', 'DAYS_LAST_PHONE_CHANGE',
        'DAYS_ID_PUBLISH', 'DAYS_REGISTRATION', 'DAYS_EMPLOYED',
        'AMT_ANNUITY_x', 'ANNUITY_PERC', 'AGE', 'REGION_POPULATION_RELATIVE',
        'AMT_INCOME_TOTAL', 'HOUR_APPR_PROCESS_START_x', 'ORGANIZATION_TYPE', 'TARGET'
    ]

    # Write the selected features in Streamlit
    st.write("The following features have been selected for model training:")
    for feature in selected_features:
        st.write(f"- {feature}")    


    st.subheader("KNN Metrics")
    metrics_knn=pd.DataFrame(metrics_knn)
    st.dataframe(metrics_knn)
    st.image('images/knn_confusion_m.png', caption='KNN Confusion')
    st.divider()


    st.subheader("XGB Metrics")
    metrics_xgb=pd.DataFrame(metrics_xgb)
    st.dataframe(metrics_xgb)
    st.image('images/xgb_confusion_m.png', caption='XGB Confusion')
    st.divider()


    st.subheader("RandomForestClassifier Metrics")
    metrics_rfc=pd.DataFrame(metrics_rfc)
    st.dataframe(metrics_rfc)
    st.image('images/rfc_confusion_m.png', caption='RFC Confusion')