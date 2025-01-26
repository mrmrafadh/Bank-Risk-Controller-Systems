import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import pickle
import datetime as dt

class PredictionModel:
    def __init__(self):
        self.load_models()

    def load_models(self):
        # Load the pre-trained model and encoders
        with open('pickle_final/random_forest_model_final.pkl', 'rb') as f:
            self.model = joblib.load(f)

        with open('pickle_final/label_encoder_finaL.pkl', 'rb') as f:
            self.le = pickle.load(f)

    def predict(self, user_inputs):
        new_data = pd.DataFrame([user_inputs])

        # Label encode columns using pre-fitted LabelEncoders
        new_data['ORGANIZATION_TYPE'] = self.le['ORGANIZATION_TYPE'].transform(new_data['ORGANIZATION_TYPE'])

        # Scale the numeric features
        numeric_columns = new_data.columns
        scaler = StandardScaler()
        new_data[numeric_columns] = scaler.fit_transform(new_data[numeric_columns])

        # Make the prediction
        prediction = self.model.predict(new_data)

        return prediction

    

    def ui(self):
        organization = ['Business Entity Type 3', 'School', 'Government', 'Religion', 'Other', 'XNA', 'Electricity', 'Medicine',
                'Business Entity Type 2', 'Self-employed', 'Transport: type 2', 'Construction', 'Housing', 'Kindergarten', 'Trade: type 7',
                'Industry: type 11', 'Military', 'Services', 'Security Ministries', 'Transport: type 4', 'Industry: type 1', 'Emergency',
                'Security', 'Trade: type 2', 'University', 'Police', 'Business Entity Type 1', 'Postal', 'Transport: type 3', 'Industry: type 4', 'Agriculture',
                'Restaurant', 'Culture', 'Hotel', 'Industry: type 7', 'Industry: type 3', 'Bank', 'Trade: type 3', 'Industry: type 9',
                'Trade: type 6', 'Industry: type 2', 'Transport: type 1', 'Industry: type 12', 'Insurance', 'Mobile', 'Trade: type 1',
                'Industry: type 5', 'Industry: type 10', 'Legal Services', 'Advertising', 'Trade: type 5', 'Cleaning', 'Industry: type 13',
                'Trade: type 4', 'Telecom', 'Industry: type 8', 'Realtor', 'Industry: type 6']
        
        def calculate_days_to_date(input_date):
            # Assuming input_date is in the format 'YYYY-MM-DD'
            input_date = dt.datetime.strptime(input_date, '%Y-%m-%d')
            current_date = dt.datetime.now()
            delta = input_date - current_date
            return delta.days

        # Create input fields for user input
        user_inputs = {}
        data_for_prediction = {}
        EXT_SOURCE_3 = st.sidebar.text_input("External Source 3 :")
        EXT_SOURCE_2 = st.sidebar.text_input("External Source 2 :")
        DAYS_LAST_PHONE_CHANGE = st.sidebar.date_input("LAST PHONE CHANGE Date :",
                                                            value=dt.date.today(),
                                                            min_value=dt.date.today() - dt.timedelta(days=365*90),
                                                            max_value=dt.date.today())
        DAYS_ID_PUBLISH = st.sidebar.date_input("ID Publish Date :",
                                                            value=dt.date.today(),
                                                            min_value=dt.date.today() - dt.timedelta(days=365*90),
                                                            max_value=dt.date.today())
        DAYS_REGISTRATION = st.sidebar.date_input("Registration Date :",
                                                            value=dt.date.today(),
                                                            min_value=dt.date.today() - dt.timedelta(days=365*90),
                                                            max_value=dt.date.today())
        DAYS_EMPLOYED = st.sidebar.date_input("Employment Date :",
                                                            value=dt.date.today(),
                                                            min_value=dt.date.today() - dt.timedelta(days=365*90),
                                                            max_value=dt.date.today())
        AMT_ANNUITY_x = st.sidebar.text_input("Annuity Amount :")
        AGE = st.sidebar.number_input("Age", min_value=18, max_value=70, step=1)
        REGION_POPULATION_RELATIVE = st.sidebar.text_input("REGION POPULATION RELATIVE :")
        AMT_INCOME_TOTAL = st.sidebar.text_input("Income Amount :")
        HOUR_APPR_PROCESS_START_x = st.sidebar.number_input("Region Rating", min_value=1, max_value=24, step=1)
        ORGANIZATION_TYPE = st.sidebar.selectbox("Select Organization Type", organization)


        def validate_inputs(user_inputs):
            errors = []
            if EXT_SOURCE_3 == "" or EXT_SOURCE_2 == "" or DAYS_LAST_PHONE_CHANGE == "" or AMT_ANNUITY_x == "" or AGE == "" or REGION_POPULATION_RELATIVE == "" or AMT_INCOME_TOTAL == "" or HOUR_APPR_PROCESS_START_x == "":
                st.sidebar.error(f"Please enter valid input.")
            else:
                try:
                    user_inputs['EXT_SOURCE_3'] = float(user_inputs['EXT_SOURCE_3'])
                except (ValueError, KeyError, TypeError):
                    errors.append("EXT_SOURCE_3")

                try:
                    user_inputs['EXT_SOURCE_2'] = float(user_inputs['EXT_SOURCE_2'])
                except (ValueError, KeyError, TypeError):
                    errors.append("EXT_SOURCE_2")

                try:
                    user_inputs['DAYS_LAST_PHONE_CHANGE'] = float(calculate_days_to_date(str(user_inputs['DAYS_LAST_PHONE_CHANGE'])))
                except (ValueError, KeyError, TypeError):
                    errors.append("DAYS_LAST_PHONE_CHANGE")

                try:
                    user_inputs['DAYS_ID_PUBLISH'] = int(calculate_days_to_date(str(user_inputs['DAYS_ID_PUBLISH'])))
                except (ValueError, KeyError, TypeError):
                    errors.append("DAYS_ID_PUBLISH")

                try:
                    user_inputs['DAYS_REGISTRATION'] = float(calculate_days_to_date(str(user_inputs['DAYS_REGISTRATION'])))
                except (ValueError, KeyError, TypeError):
                    errors.append("DAYS_REGISTRATION")

                try:
                    user_inputs['DAYS_EMPLOYED'] = int(calculate_days_to_date(str(user_inputs['DAYS_EMPLOYED'])))
                except (ValueError, KeyError, TypeError):
                    errors.append("DAYS_EMPLOYED")

                try:
                    user_inputs['AMT_ANNUITY_x'] = float(user_inputs['AMT_ANNUITY_x'])
                except (ValueError, KeyError, TypeError):
                    errors.append("AMT_ANNUITY_x")

                try:
                    user_inputs['AGE'] = int(user_inputs['AGE'])
                except (ValueError, KeyError, TypeError):
                    errors.append("AGE")

                try:
                    user_inputs['REGION_POPULATION_RELATIVE'] = float(user_inputs['REGION_POPULATION_RELATIVE'])
                except (ValueError, KeyError, TypeError):
                    errors.append("REGION_POPULATION_RELATIVE")

                try:
                    user_inputs['AMT_INCOME_TOTAL'] = float(user_inputs['AMT_INCOME_TOTAL'])
                except (ValueError, KeyError, TypeError):
                    errors.append("AMT_INCOME_TOTAL")

                try:
                    user_inputs['HOUR_APPR_PROCESS_START_x'] = int(user_inputs['HOUR_APPR_PROCESS_START_x'])
                except (ValueError, KeyError, TypeError):
                    errors.append("HOUR_APPR_PROCESS_START_x")

                try:
                    user_inputs['ORGANIZATION_TYPE'] = str(user_inputs['ORGANIZATION_TYPE'])
                except (ValueError, KeyError, TypeError):
                    errors.append("ORGANIZATION_TYPE")

                data_for_prediction = {
                    'EXT_SOURCE_3': user_inputs['EXT_SOURCE_3'],
                    'EXT_SOURCE_2': user_inputs['EXT_SOURCE_2'],
                    'DAYS_LAST_PHONE_CHANGE': user_inputs['DAYS_LAST_PHONE_CHANGE'],
                    'DAYS_ID_PUBLISH': user_inputs['DAYS_ID_PUBLISH'],
                    'DAYS_REGISTRATION': user_inputs['DAYS_REGISTRATION'],
                    'DAYS_EMPLOYED': user_inputs['DAYS_EMPLOYED'],
                    'AMT_ANNUITY_x': user_inputs['AMT_ANNUITY_x'],
                    'ANNUITY_PERC': user_inputs['AMT_ANNUITY_x']/user_inputs['AMT_INCOME_TOTAL'],
                    'AGE': user_inputs['AGE'],
                    'REGION_POPULATION_RELATIVE': user_inputs['REGION_POPULATION_RELATIVE'],
                    'AMT_INCOME_TOTAL': user_inputs['AMT_INCOME_TOTAL'],
                    'HOUR_APPR_PROCESS_START_x': user_inputs['HOUR_APPR_PROCESS_START_x'],
                    'ORGANIZATION_TYPE': user_inputs['ORGANIZATION_TYPE']
                }

                return errors, data_for_prediction

        if st.sidebar.button("Check"):
            user_inputs = {
                'EXT_SOURCE_3': EXT_SOURCE_3,
                'EXT_SOURCE_2': EXT_SOURCE_2,
                'DAYS_LAST_PHONE_CHANGE': DAYS_LAST_PHONE_CHANGE,
                'DAYS_ID_PUBLISH': DAYS_ID_PUBLISH,
                'DAYS_REGISTRATION': DAYS_REGISTRATION,
                'DAYS_EMPLOYED': DAYS_EMPLOYED,
                'AMT_ANNUITY_x': AMT_ANNUITY_x,
                'AGE': AGE,
                'REGION_POPULATION_RELATIVE': REGION_POPULATION_RELATIVE,
                'AMT_INCOME_TOTAL': AMT_INCOME_TOTAL,
                'HOUR_APPR_PROCESS_START_x': HOUR_APPR_PROCESS_START_x,
                'ORGANIZATION_TYPE': ORGANIZATION_TYPE,
            }
            
            errors, data_for_prediction = validate_inputs(user_inputs)
            if errors:
                st.sidebar.error(f"Please correct the following fields: {', '.join(errors)}")
            else:
                pred_model = PredictionModel()
                prediction = pred_model.predict(data_for_prediction)
                st.write(f"### The user's loan risk status is: {'Defaulted' if prediction[0] == 1 else 'Not Defaulted'}")
