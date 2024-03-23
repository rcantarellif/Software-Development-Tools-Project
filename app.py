# Importing the necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the app
st.title('Vehicle Data Exploration')

# Reading the dataset's CSV file into a Pandas DataFrame
# df = pd.read_csv('C:\\Users\\System32\\Documents\\MyProject\\vehicles_us.csv')
df = pd.read_csv('vehicles_us.csv')

# Display a header
st.header('Histogram of Vehicle Prices')

# Create a checkbox to show/hide the histogram
if st.checkbox('Show Price Histogram'):
    # Creating a histogram using Plotly Express
    fig_hist = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
    # Displaying the histogram
    st.plotly_chart(fig_hist)

# Display another header
st.header('Scatter Plot of Odometer vs Price')

# Create a checkbox to show/hide the scatter plot
if st.checkbox('Show Odometer vs Price Scatter Plot'):
    # Drop rows with missing values for 'odometer' and 'price'
    df_dropna = df.dropna(subset=['odometer', 'price'])
    # Creating a scatter plot using Plotly Express
    fig_scatter = px.scatter(df_dropna, x='odometer', y='price', title='Odometer Reading vs Price')
    # Displaying the scatter plot
    st.plotly_chart(fig_scatter)

# Optionally, if you want to show all data as a table
st.header('Vehicle Data')
st.write(df)
