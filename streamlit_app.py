import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import datetime
import re

"""
# Welcome to your own UPI Transaction Fraud Detector!

You have the option of inspecting a single transaction by adjusting the parameters below or you can even check 
multiple transactions at once by uploading a .csv file in the specified format
"""
# Function to validate time format
def validate_time_format(input_time):
    pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$')
    if pattern.match(input_time):
        return True
    else:
        return False

tran_date = st.date_input("Select the date of your transaction", datetime.date.today())
tran_time = st.text_input("Enter transaction time (HH:MM:SS)", "")
# Validate time and display error message if format is incorrect
if not validate_time_format(tran_time):
    st.error("Please enter time in the format HH:MM:SS")
# Display the entered time if format is correct
else:
    st.write("You entered:", tran_time)
merch_id = st.text_input("Enter the merchant's id:")
cust_id = st.text_input("Enter the customer's id:")
device_id = st.text_input("Enter the device's id:")
trans_type = st.selectbox("Select an option", ["Bank Transfer", "Bill Payment", "Investment", "Other", "Purchase", "Refund", "Subscription"])
pay_type = st.selectbox("Select an option", ["CRED", "Google Pay", "HDFC", "ICICI UPI", "IDFC UPI", "Other", "Paytm", "PhonePe", "Razor Pay"])
num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)
merch_id = st.text_input("Enter the merchant's id:")
indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
