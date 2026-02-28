import streamlit as st
import altair as alt
from utils.io import load_weather
from charts.charts import (
    base_theme,
    chart_hook_temp_over_time,
    chart_context_seasonality,
    chart_static_temp_weather,
    chart_surprise_extremes,
    chart_explain_precip_vs_temp,
)

st.set_page_config(page_title="Story", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

df = load_weather()

st.title("A Data Story: Seattle Weather Patterns")
st.markdown("**Central question:** *What patterns (seasonality and extremes) show up in daily weather over time?*")

st.header("1) Daily temperature over time")
st.write("We start with a simple time series to build intuition about variability and overall range.")
st.altair_chart(chart_hook_temp_over_time(df), use_container_width=True)
st.caption("Takeaway: Temperature fluctuates heavily day-to-day. There is evidence of strong seasonality and occasional extremes.")

st.header("2) Seasonality by month")
st.write("Next, we summarize the temperature info in a way that makes month-to-month structure easy to compare.")
st.altair_chart(chart_context_seasonality(df), use_container_width=True)
st.caption("Takeaway: As expected, summer months shift the distribution upward; winter months have lower medians and tighter ranges.")

st.header("3) Surprise: Extremely hot days")
st.write("Here we highlight rare events of extreme heat, not just the average, defined by temperatures in the 99-th percentile.")
st.altair_chart(chart_surprise_extremes(df), use_container_width=True)
st.caption("Takeaway: A small fraction of days drive the highest peaks—outliers that a smoothed trend can hide.")

st.header("4) Precipitation vs temperature")
st.write("We wish to test a plausible explanation: are the warmest days also the driest (or not)?")
st.altair_chart(chart_explain_precip_vs_temp(df), use_container_width=True)
st.caption("Takeaway: The relationship is noisy — precipitation alone does not explain extreme heat, motivating more fine-grained exploration.")

st.header("4) Temperature Distribution by Weather Type")
st.write("We created a faceted histogram that shows the distribution of daily maximum temperatures separately for each weather type, allowing us to compare how temperature ranges differ across weather conditions.")
st.altair_chart(chart_static_temp_weather(df), use_container_width=True)
st.caption("Takeaway: From the distributions we can see that snow and drizzle occur almost entirely at lower temperatures, fog and rain cluster in the mid-range, and sun clusters at higher temperatures, showing that daily maximum temperature is strongly associated with the type of weather condition. ")