import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def analytics_ui():
    st.title("📊 Analytics Dashboard")

    try:
        dsa = pd.read_csv("data/dsa_progress.csv")

        topic_count = dsa["Topic"].value_counts()

        fig, ax = plt.subplots()
        topic_count.plot(kind="bar", ax=ax)
        ax.set_title("DSA Topic Distribution")

        st.pyplot(fig)
    except:
        st.warning("Analytics data not available")
