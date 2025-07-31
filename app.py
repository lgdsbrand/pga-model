import streamlit as st
import pandas as pd
import pga_model

st.set_page_config(page_title="LineupWire PGA Model", layout="wide")

# ---- TITLE & TOURNAMENT DROPDOWN ----
st.title("🏌️ LineupWire PGA Model")
st.caption("Smarter Sports Betting for PGA Tournaments")

tournaments = ["Sample Tournament", "Masters", "US Open", "PGA Championship"]
selected_tournament = st.selectbox("Select Tournament", tournaments)

# ---- TOGGLE PRE-TOURNEY / H2H ----
view_option = st.radio("View", ["Pre-Tourney", "H2H / 3-Ball"], horizontal=True)

# ---- LOAD DATA FROM MODEL ----
if view_option == "Pre-Tourney":
    st.subheader(f"🏆 Pre-Tourney Leaderboard — {selected_tournament}")
    df = pga_model.load_leaderboard(selected_tournament)
    st.dataframe(
        df.style.apply(pga_model.highlight_edges, axis=1),
        use_container_width=True,
        height=450
    )

elif view_option == "H2H / 3-Ball":
    st.subheader(f"⚔️ Matchup Viewer — {selected_tournament}")
    matchup_df = pga_model.load_matchups(selected_tournament)
    st.dataframe(
        matchup_df.style.apply(pga_model.highlight_matchup, axis=1),
        use_container_width=True,
        height=450
    )

st.caption("🔄 Auto-refreshes every 60 seconds (demo static data for now)")
