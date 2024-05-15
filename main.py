import streamlit as st
import plotly.express as px

st.title("Weather Forecast App: Get the Weather for the Next Few Days")
place = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# function for getting data
def get_data(days):
    # create plotly figure first & date/temperature list
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    # this makes y-axis dynamically change pending on when days change
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)