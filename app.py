import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Forecast Dashboard", layout="wide")

# -------------------------------
# 1. Define Forecast Data
# -------------------------------
questions = [
    "US Withdrawal from WTO (2025)",
    "USMCA Renegotiation (2026)",
    "EU Carbon Border Adjustment (2027)",
    "India–EU FTA (2026)",
    "US–China Trade Value Increase (2025)",
    "Transatlantic Green Alliance (2027)",
    "Americas Semiconductor Revenue >35% (2025)",
    "TSMC Revenue Share <78% (2025–2026)",
    "China REE Export Restrictions (2027)",
    "US Firms on China's Unreliable Entity List (2026)",
    "Mercosur Common Currency (2033)",
    "BRICS Expansion (≥5 new members by 2027)",
    "BRICS Common Currency (2030)",
    "GCC–China FTA Completion (2026)",
    "China Leads Economic Relationships Index (2026)",
    "BRICS Economic Capability > US (2028)",
    "China’s Future Resource Score within 5 pts of US (2030)",
    "Starlink Authorized >12,000 Satellites (2026)",
    "Non-US/China AI Model Top 3 in Arena (2026)",
    "≥15 CBDCs Operational by 2028"
]

df = pd.DataFrame({
    "ID": [f"F{i}" for i in range(1, 21)],
    "Question": questions,
    "Forecast_Prob": [0.12, 0.60, 0.70, 0.60, 0.26, 0.40, 0.13, 0.42, 0.65, 0.30,
                      0.07, 0.35, 0.20, 0.40, 0.90, 0.10, 0.25, 0.60, 0.15, 0.35],
    "Resolved": [False] * 20,
    "Outcome": [np.nan] * 20
})

# -------------------------------
# 2. Compute Brier Score (none resolved)
# -------------------------------
df["Brier_Score"] = np.nan
avg_brier = np.nan  # No resolved forecasts yet

# -------------------------------
# 3. Dashboard Layout
# -------------------------------
st.title("📊 Forecast Tracker — Bridgewater × Global Citizen Challenge")

col1, col2 = st.columns(2)
with col1:
    st.metric("Average Brier Score", "N/A")
with col2:
    st.metric("Resolved Forecasts", f"{df['Resolved'].sum()} / {len(df)}")

st.markdown("---")

# -------------------------------
# 4. Calibration Placeholder
# -------------------------------
st.subheader("🎯 Calibration Chart")
st.info("No forecasts have resolved yet — the calibration chart will appear automatically when outcomes are added.")

st.markdown("---")

# -------------------------------
# 5. Forecast Table (Main View)
# -------------------------------
st.subheader("🧾 Current Forecast Portfolio")

styled = df.style.format({
    "Forecast_Prob": "{:.2f}"
}).background_gradient(subset=["Forecast_Prob"], cmap="Blues")

st.dataframe(styled, use_container_width=True, height=600)

# Optional future extension placeholder
#st.caption("Tip: Once questions resolve, add outcomes (0 or 1) to compute Brier scores and show calibration.")
