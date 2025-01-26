import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import warnings
# Ignore all warnings
warnings.filterwarnings('ignore')

# Load the dataset
class eda_object():
    def __init__(self):
        self.load_data()
    
    def load_data(self):
        self.df = pd.read_csv('data/loan_data_cleaned.csv')



    def plot1(self):
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x='CODE_GENDER', palette='viridis')
        plt.title('Distribution of Gender', fontsize=16)
        plt.xlabel('Gender', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)  # Ensure this call is placed here

    def plot2(self):
        # Set plot style
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.df, x='NAME_CONTRACT_TYPE_x', palette='viridis')
        plt.title('Distribution Contract Type', fontsize=16)
        plt.xlabel('Contract Type', fontsize=12)  # Corrected the x-axis label
        plt.ylabel('Count', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)  # Ensure this call is placed here


    def plot3(self):
        # Set plot style
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 5))
        sns.countplot(data=self.df, x='NAME_INCOME_TYPE', palette='viridis')
        plt.title('Distribution of Income Type', fontsize=16)
        plt.xlabel('Income Type', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        st.pyplot(plt)


    def plot4(self):
        # Set plot style
        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 5))
        sns.countplot(data=self.df, x='NAME_EDUCATION_TYPE', palette='viridis')
        plt.title('Distribution of Education Type', fontsize=16)
        plt.xlabel('Education Type', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        st.pyplot(plt)


    def plot5(self):

        sns.set_theme(style="whitegrid")
        plt.figure(figsize=(12, 5))
        sns.countplot(data=self.df, x='OCCUPATION_TYPE', palette='viridis')
        plt.title('Distribution of Occupation Type', fontsize=16)
        plt.xlabel('Occupation Type', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=90)
        plt.tight_layout()
        st.pyplot(plt)


    def plot6(self):

        # Count the occurrences of each value in the TARGET column
        target_counts = self.df['TARGET'].value_counts()

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(target_counts,
                labels=['No Default (0)', 'Default (1)'],
                autopct='%1.1f%%',
                startangle=90,
                colors=['skyblue', 'orange'],
                explode=(0, 0.1))  # Emphasize the 'Default' slice
        plt.title('Distribution of Target Variable')
        plt.tight_layout()
        st.pyplot(plt)


    def plot7(self):
        temp_df = self.df[['AMT_INCOME_TOTAL','AMT_CREDIT_x','AMT_ANNUITY_x']]
        mean_values = temp_df.mean()
        median_values = temp_df.median()
        # Prepare the data for plotting
        temp_df = {
            'Mean': temp_df.mean(),
            'Median': temp_df.median()
        }
        stats_df = pd.DataFrame(temp_df)
        # Plot the bar plot
        stats_df.plot(kind='bar', figsize=(8, 4))
        plt.title("Mean, Median, and Mode of AMT_INCOME_TOTAL,AMT_CREDIT_x & AMT_ANNUITY_x")
        plt.xlabel("Columns")
        plt.ylabel("Values")
        st.pyplot(plt)


    def plot8(self):
        temp_df = self.df[['AMT_INCOME_TOTAL','AMT_CREDIT_x','AMT_ANNUITY_x', 'TARGET']]
        # Calculate mean and median for each TARGET
        mean_df = temp_df.groupby('TARGET').mean().reset_index().melt(id_vars='TARGET', var_name='measure', value_name='value')
        median_df = temp_df.groupby('TARGET').median().reset_index().melt(id_vars='TARGET', var_name='measure', value_name='value')

        # Add a 'statistic' column to distinguish between mean and median
        mean_df['statistic'] = 'mean'
        median_df['statistic'] = 'median'

        # Combine mean and median into one DataFrame
        combined_df = pd.concat([mean_df, median_df])

        # Create the bar plot with grouped means and medians
        fig = px.bar(
            combined_df,
            x='TARGET',
            y='value',
            color='statistic',
            facet_col='measure',
            barmode='group',
            title='AMT_INCOME_TOTAL, AMT_CREDIT_x & AMT_ANNUITY_x Mean and Median Values by Target Group'
        )

        # Update the layout for improved readability
        fig.update_layout(
            xaxis_title='Target',
            yaxis_title='Values',
            legend_title='Statistic'
        )

        # Show the plot
        st.plotly_chart(fig)

    def plot9(self):
        temp_df = self.df[['EXT_SOURCE_2', 'EXT_SOURCE_3', 'TARGET']]

        # Calculate mean and median for each TARGET
        mean_df = temp_df.groupby('TARGET').mean().reset_index().melt(id_vars='TARGET', var_name='measure', value_name='value')
        median_df = temp_df.groupby('TARGET').median().reset_index().melt(id_vars='TARGET', var_name='measure', value_name='value')

        # Add a 'statistic' column to distinguish between mean and median
        mean_df['statistic'] = 'mean'
        median_df['statistic'] = 'median'

        # Combine mean and median into one DataFrame
        combined_df = pd.concat([mean_df, median_df])

        # Create the bar plot with grouped means and medians
        fig = px.bar(
            combined_df,
            x='TARGET',
            y='value',
            color='statistic',
            facet_col='measure',
            barmode='group',
            title='EXT_SOURCE_2 & EXT_SOURCE_3 Mean and Median Values by Target Group'
        )

        # Update the layout for improved readability
        fig.update_layout(
            xaxis_title='Target',
            yaxis_title='Values',
            legend_title='Statistic'
        )

        # Show the plot
        st.plotly_chart(fig)

    def plot10(self):
        # Group data by target and calculate mean and median
        temp_df = self.df[['DAYS_EMPLOYED', 'TARGET']]
        mean_df = temp_df.groupby('TARGET').mean().reset_index()
        median_df = temp_df.groupby('TARGET').median().reset_index()

        # Add a 'statistic' column to label mean and median
        mean_df = mean_df.melt(id_vars='TARGET', var_name='measure', value_name='value')
        mean_df['statistic'] = 'mean'

        median_df = median_df.melt(id_vars='TARGET', var_name='measure', value_name='value')
        median_df['statistic'] = 'median'

        # Combine both dataframes
        combined_df = pd.concat([mean_df, median_df])

        # Create the plot with distinct colors for mean and median
        fig = px.bar(
            combined_df,
            x='TARGET',
            y='value',
            color='statistic',  # Use `statistic` for color distinction
            barmode='group',
            title='DAYS_EMPLOYED Mean and Median Values by Target Group'
        )

        # Update axis and legend titles
        fig.update_layout(
            xaxis_title='Target',
            yaxis_title='Values',
            legend_title='Statistic'
        )

        # Show the plot
        st.plotly_chart(fig)

    
    def plot11(self):
        # Define the columns to plot
        d_cols = ['NAME_CONTRACT_TYPE_x', 'CODE_GENDER', 'FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'NAME_TYPE_SUITE_x', 'NAME_INCOME_TYPE','NAME_EDUCATION_TYPE']

        # Define a function to create bar plots
        def plot_bar_charts(data, title_prefix, num_cols):
            plt.figure(figsize=(16, 8))  # Adjusted height for better readability
            for col, idx in zip(d_cols, range(num_cols)):
                plt.subplot(2, (num_cols + 1) // 2, idx + 1)  # Spread plots across 2 rows
                sns.countplot(data=data, x=col, order=data[col].value_counts().index, palette="pastel")
                plt.title(f"{col} - {title_prefix}")
                plt.xlabel("")
                plt.ylabel("Count")
                plt.xticks(rotation=90)
            plt.tight_layout()
            st.pyplot(plt)

        # Plot for defaulters (TARGET = 1)
        default = self.df[self.df["TARGET"] == 1][d_cols]
        plot_bar_charts(default, "Defaulter", len(d_cols))

        # Plot for non-defaulters (TARGET = 0)
        non_default = self.df[self.df["TARGET"] == 0][d_cols]
        plot_bar_charts(non_default, "Repayer", len(d_cols))



