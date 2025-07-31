import streamlit as st
import pandas as pd

st.set_page_config(page_title="LineupWire PGA Model", layout="wide")

# -------------------------------
# Header
# -------------------------------
st.title("⛳ LineupWire PGA Model")
st.caption("Smarter Golf Betting Starts Here")

# -------------------------------
# Tournament Dropdown (Top Left)
# -------------------------------
col1, col2 = st.columns([1, 4])
with col1:
    tournaments = ["The Masters", "PGA Championship", "US Open", "Open Championship"]
    selected_tournament = st.selectbox("Select Tournament", tournaments)
with col2:
    st.write(f"### {selected_tournament}")

st.markdown("---")

# -------------------------------
# Leaderboard (Scrollable)
# -------------------------------
st.subheader("🏆 Live Leaderboard")

leaderboard_data = pd.DataFrame({
    "Pos": [1, 2, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Player": [
        "Jon Rahm", "Scottie Scheffler", "Rory McIlroy", "Xander Schauffele", "Viktor Hovland",
        "Jordan Spieth", "Collin Morikawa", "Brooks Koepka", "Tony Finau", "Max Homa",
        "Patrick Cantlay", "Justin Thomas"
    ],
    "Score": [-12, -10, -10, -8, -7, -7, -6, -5, -5, -5, -4, -4],
    "Round": [4,4,4,4,4,4,4,4,4,4,4,4],
    "Thru": ["F","F","F","F","F","F","F","F","F","F","F","F"]
})

# Show only top 10 at a time with scrolling
st.dataframe(
    leaderboard_data.head(10),
    use_container_width=True,
    hide_index=True
)

st.caption("Scroll to see more players →")

st.markdown("---")

# -------------------------------
# Toggle Between Pre-Tourney & H2H
# -------------------------------
view_option = st.radio(
    "Select View:",
    ["Pre-Tourney Picks", "H2H & 3-Ball Matchups"],
    horizontal=True
)

if view_option == "Pre-Tourney Picks":
    st.subheader("📊 Pre-Tourney Value Picks")
    
    pre_tourney = pd.DataFrame({
        "Player": ["Jon Rahm", "Scottie Scheffler", "Rory McIlroy", "Xander Schauffele", "Viktor Hovland"],
        "Win Odds": ["+700", "+800", "+1200", "+1600", "+2000"],
        "Top 5 Odds": ["+200", "+220", "+300", "+400", "+450"],
        "Top 10 Odds": ["-110", "+100", "+150", "+200", "+250"],
        "Make Cut": ["Yes", "Yes", "Yes", "Yes", "Yes"]
    })
    
    st.dataframe(pre_tourney, use_container_width=True, hide_index=True)

else:
    st.subheader("🤝 H2H & 3-Ball Matchups")

    matchups = pd.DataFrame({
        "Matchup": ["Rahm vs Scheffler", "Rory vs Xander", "Hovland vs Spieth"],
        "SG Tee to Green": ["+1.8 / +1.5", "+1.2 / +1.4", "+1.1 / +0.9"],
        "SG Putting": ["+0.3 / +0.6", "+0.5 / +0.2", "+0.1 / +0.4"],
        "Score Avg": ["68.5 / 69.0", "69.2 / 69.1", "69.5 / 69.8"],
        "Model Winner": ["Rahm 57%", "Xander 52%", "Hovland 54%"]
    })

    st.dataframe(matchups, use_container_width=True, hide_index=True)

st.markdown("---")
st.caption("Future version: Live odds, stat highlights, and best bet indicators")
