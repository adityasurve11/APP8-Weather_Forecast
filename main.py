import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast For Upcoming Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted.")
min_value = 1
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
if days == min_value:
    print(st.subheader(f"{option} for the next {days} day in {place}"))
else:
    print(st.subheader(f"{option} for the next {days} days in {place}"))

data = get_data()

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
