import streamlit as st
from utils.io import load_weather
from charts.charts import chart_dashboard, chart_interactive_wind_vs_temp

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")

st.altair_chart(chart_dashboard(df), use_container_width=True)

st.title("Wind vs Max Temperature (Filter by Weather Type)")
st.write("Below we have created an interactive scatterplot that shows the relationship between maximum temperature and wind speed, allowing users to filter to one weather type while fading others to compare how temperature–wind patterns differ across weather conditions.")

st.altair_chart(chart_interactive_wind_vs_temp(df), use_container_width=True)
st.write("Overall, there is no strong linear relationship between wind and temperature for any weather type, but weather types clearly separate along the temperature axis, with wind variability differing slightly by weather condition.")

st.markdown("**Guided prompts:**")
st.write("- Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift?")
st.write("- Brush a specific year—do extremes cluster in particular periods?")
st.write("- Compare histogram shape across weather types—what changes most: center, spread, or tails?")
