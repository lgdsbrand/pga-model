import streamlit as st
import pandas as pd

st.set_page_config(page_title="LineupWire PGA Model", layout="wide")

# -------------------------------
# Header
# -------------------------------
st.title("⛳ LineupWire PGA Model")
st.write("Smarter golf betting starts here.")

# -------------------------------
# Tournament Dropdown
# -------------------------------
tournaments = ["The Masters", "PGA Championship", "US Open", "Open Championship"]
selected_tournament = st.selectbox("Select Tournament", tournaments)

st.write(f"Showing model for: **{selected_tournament}**")

# -------------------------------
# Leaderboard Shell (Placeholder)
# -------------------------------
leaderboard_data = pd.DataFrame({
    "Position": [1, 2, 2, 4, 5],
    "Player": ["Jon Rahm", "Scottie Scheffler", "Rory McIlroy", "Xander Schauffele", "Viktor Hovland"],
    "Score": [-12, -10, -10, -8, -7],
    "Round": [4, 4, 4, 4, 4]
})

st.subheader("🏆 Live Leaderboard (Demo)")
st.dataframe(leaderboard_data, use_container_width=True, hide_index=True)

# -------------------------------
# H2H Matchup Table (Placeholder)
# -------------------------------
st.subheader("🤝 H2H & 3-Ball Matchups")

matchups = pd.DataFrame({
    "Matchup": ["Rahm vs Scheffler", "Rory vs Xander"],
    "SG Tee to Green": ["+1.8 / +1.5", "+1.2 / +1.4"],
    "SG Putting": ["+0.3 / +0.6", "+0.5 / +0.2"],
    "Score Avg": ["68.5 / 69.0", "69.2 / 69.1"],
    "Model Winner": ["Rahm 57%", "Xander 52%"]
})

st.dataframe(matchups, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("This is the PGA model demo. Future versions will include live stats, value highlights, and matchup edges.")
