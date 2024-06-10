import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, subheader
st.title("Weather Forecast App: Get the Weather for the Next Few Days")
place = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

# Only runs if Place has an entry to avoid showing a default error before user types anything in
if place:
    # function for getting data
    try:
        filtered_data = get_data(place, days)

        # Generate plot graphics depending on user selection
        if option == "Temperature":
            # Create temperature plot, div temps by 10 to show correct Celsius decimal point
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":
            # Create image plot of sky weather if selected
            # weather is a list hence the [0] index addition
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # match conditions to image dictionary, called translation. Creates list "images" of file paths
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place does not exist! Please check for typos")