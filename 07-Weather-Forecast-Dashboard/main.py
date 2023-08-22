import streamlit as st
import plotly.express as px
from backend import get_data

# Add Title, Text Input, Slider, Selectbox, Subheader UI components
st.title("Weather Forecast for the Next Days")
place = st.text_input('Place: ')
days = st.slider('Forecast Days',
                 min_value=1,
                 max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")

# Get the Temperature/Sky Data
d, t = get_data(place, days, option)

# Create a Temperature Plot
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
