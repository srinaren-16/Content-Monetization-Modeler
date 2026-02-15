import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Load Model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="YouTube Ad Revenue Predictor", layout="centered")

st.title("📊 YouTube Ad Revenue Prediction App")
st.write("Predict estimated ad revenue based on video performance metrics.")
st.markdown("---")

# Inputs
views = st.number_input("Views", min_value=1, value=1000)
likes = st.number_input("Likes", min_value=0, value=100)
comments = st.number_input("Comments", min_value=0, value=10)
watch_time_minutes = st.number_input("Total Watch Time (Minutes)", min_value=0.0, value=500.0)
video_length_minutes = st.number_input("Video Length (Minutes)", min_value=0.1, value=10.0)
subscribers = st.number_input("Channel Subscribers", min_value=0, value=10000)

st.markdown("---")

category = st.selectbox("Category", ["Entertainment", "Gaming", "Lifestyle", "Music", "Tech"])
device = st.selectbox("Device", ["Mobile", "TV", "Tablet"])
country = st.selectbox("Country", ["CA", "DE", "IN", "UK", "US"])

st.markdown("---")

# Function to Create DataFrame
def create_input_dataframe(watch_time_value):

    engagement_rate = (likes + comments) / views
    watch_time_per_view = watch_time_value / views
    retention_rate = watch_time_per_view / video_length_minutes

    return pd.DataFrame({
        "views": [views],
        "likes": [likes],
        "comments": [comments],
        "watch_time_minutes": [watch_time_value],
        "video_length_minutes": [video_length_minutes],
        "subscribers": [subscribers],
        "engagement_rate": [engagement_rate],
        "watch_time_per_view": [watch_time_per_view],
        "retention_rate": [retention_rate],
        "category": [category],
        "device": [device],
        "country": [country]
    }), engagement_rate, watch_time_per_view, retention_rate


# Prediction
if st.button("Predict Ad Revenue"):

    # Main prediction
    input_df, engagement_rate, watch_time_per_view, retention_rate = create_input_dataframe(watch_time_minutes)

    predicted_revenue = model.predict(input_df)[0]
    st.success(f"💰 Estimated Ad Revenue: ${predicted_revenue:.2f}")

    st.markdown("---")

    # Metrics
    st.subheader("📈 Calculated Engagement Metrics")
    st.write(f"Engagement Rate: {engagement_rate:.4f}")
    st.write(f"Watch Time Per View: {watch_time_per_view:.4f}")
    st.write(f"Retention Rate: {retention_rate:.4f}")

    # Bar Chart
    st.subheader("📊 Performance Breakdown")

    fig1, ax1 = plt.subplots()
    ax1.bar(
        ["Engagement", "Retention", "Watch Time/View"],
        [engagement_rate, retention_rate, watch_time_per_view]
    )
    ax1.set_ylabel("Value")
    ax1.set_title("Video Performance Metrics")
    st.pyplot(fig1)

    st.markdown("---")

    # Watch Time vs Revenue Curve
    st.subheader("📈 Watch Time vs Revenue")

    watch_time_range = np.linspace(0, watch_time_minutes * 2, 20)
    revenue_predictions = []

    for wt in watch_time_range:
        temp_df, _, _, _ = create_input_dataframe(wt)
        revenue_predictions.append(model.predict(temp_df)[0])

    fig2, ax2 = plt.subplots()
    ax2.plot(watch_time_range, revenue_predictions)

    ax2.set_xlabel("Watch Time (Minutes)")
    ax2.set_ylabel("Predicted Revenue ($)")
    ax2.set_title("Impact of Watch Time on Revenue")
    ax2.grid(True)

    st.pyplot(fig2)
