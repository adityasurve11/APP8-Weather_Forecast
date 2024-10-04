import streamlit as st
import plotly.express as px


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


dates = ["2024-04-10", "2024-05-10", "2024-06-10"]
temperature = [10, 11, 15]
figure = px.line(x=dates, y, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
