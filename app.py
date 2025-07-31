import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="LineupWire PGA Model", layout="wide")

# -------------------------------
# INLINE CSS FOR CARD STYLING
# -------------------------------
st.markdown(
    """
    <style>
    .card {
        background-color: white;
        border: 1px solid lightgray;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }
    .stat-row {
        display: flex;
        justify-content: space-between;
        padding: 4px 0;
        font-size: 15px;
    }
    .winner {
        color: green;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# TOURNAMENT DROPDOWN
# -------------------------------
st.title("🏌️ LineupWire PGA Model")
st.caption("Smarter Sports Betting for PGA Tournaments")

tournaments = [
    "Masters", "U.S. Open", "PGA Championship", "The Open Championship",
    "The Players", "Genesis Invitational", "Arnold Palmer Invitational",
    "Memorial Tournament", "BMW Championship", "FedEx St. Jude",
    "Tour Championship", "RBC Heritage", "Wells Fargo", "Charles Schwab",
    "Travelers", "John Deere Classic", "Rocket Mortgage Classic",
    "3M Open", "Wyndham Championship"
]
selected_tournament = st.selectbox("Select Tournament", tournaments)

# -------------------------------
# SAMPLE LEADERBOARD (Scroll + Fixed Header)
# -------------------------------
st.subheader(f"📊 Live Leaderboard — {selected_tournament}")

leaderboard_data = pd.DataFrame({
    "Pos": [1, 2, 2, 4, 5, 6, 7, 8, 9, 10],
    "Player": [
        "Jon Rahm", "Scottie Scheffler", "Rory McIlroy", "Xander Schauffele", "Viktor Hovland",
        "Jordan Spieth", "Collin Morikawa", "Brooks Koepka", "Tony Finau", "Max Homa"
    ],
    "Score": [-12, -10, -10, -8, -7, -7, -6, -5, -5, -5],
    "Round": [4]*10,
    "Thru": ["F"]*10
})

st.dataframe(leaderboard_data, use_container_width=True, hide_index=True, height=350)

# -------------------------------
# TOGGLE FOR BEST BETS / H2H-3BALL
# -------------------------------
view_option = st.radio("View", ["Pre-Tourney Best Bets", "H2H / 3-Ball"], horizontal=True)

# -------------------------------
# PRE-TOURNEY BEST BETS (Table Only)
# -------------------------------
if view_option == "Pre-Tourney Best Bets":
    st.subheader(f"🏆 Pre-Tourney Best Bets — {selected_tournament}")
    best_bets = pd.DataFrame({
        "Player": ["A. Rai", "M. Fitzpatrick", "K. Bradley", "S. Kim", "R. MacIntyre"],
        "Make Cut %": [76.7, 72.7, 72.5, 72.2, 71.5],
        "Top 20 %": [42.5, 37.5, 36.5, 35.6, 34.5],
        "Top 10 %": [27.1, 23.5, 22.2, 21.6, 20.2],
        "Top 5 %": [16.5, 14.2, 13.0, 12.4, 11.4],
        "Win %": [4.6, 3.8, 3.4, 3.0, 2.7],
        "Edge %": [8, 5, 4, 3, 2]
    })
    st.dataframe(best_bets, use_container_width=True, hide_index=True, height=350)

# -------------------------------
# H2H / 3-BALL CARD VIEW
# -------------------------------
elif view_option == "H2H / 3-Ball":
    mode = st.radio("Mode", ["H2H", "3-Ball"], horizontal=True)

    # Example data for demonstration
    if mode == "H2H":
        matchups = [
            {
                "players": ["Scheffler", "Rahm"],
                "stats": [
                    ("SG: Tee to Green", 1.85, 1.55),
                    ("SG: Putting", 0.12, 0.23),
                    ("Scoring Avg", 68.3, 68.9)
                ],
                "best_bet": "Scheffler -120",
                "advantage": "Scheffler"
            },
            {
                "players": ["Rory McIlroy", "Spieth"],
                "stats": [
                    ("SG: Tee to Green", 1.70, 1.05),
                    ("SG: Putting", 0.18, 0.05),
                    ("Scoring Avg", 68.8, 69.5)
                ],
                "best_bet": "Rory -115",
                "advantage": "Rory McIlroy"
            }
        ]
    else:  # 3-Ball
        matchups = [
            {
                "players": ["Homa", "Finau", "Morikawa"],
                "stats": [
                    ("SG: Tee to Green", 1.2, 1.5, 1.4),
                    ("SG: Putting", 0.3, 0.2, 0.4),
                    ("Scoring Avg", 69.1, 68.8, 69.0)
                ],
                "best_bet": "Finau +200",
                "advantage": "Finau"
            }
        ]

    # Render each matchup as a card
    for matchup in matchups:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        # Header
        st.markdown("### " + " vs ".join(matchup["players"]))

        # Stats rows with ✅ winner check
        for stat in matchup["stats"]:
            st.markdown('<div class="stat-row">', unsafe_allow_html=True)
            label = stat[0]
            values = stat[1:]
            
            # Determine winner logic (lower better for Scoring, higher better otherwise)
            if "Scoring" in label:
                best_val = min(values)
            else:
                best_val = max(values)

            display_vals = []
            for val in values:
                check = "✅" if val == best_val else ""
                display_vals.append(f"{val} {check}")
            st.markdown(f"{label}: {' | '.join(display_vals)}")

            st.markdown('</div>', unsafe_allow_html=True)

        # Footer
        st.markdown(f"🏆 **Overall Advantage:** {matchup['advantage']}")
        st.markdown(f"💰 **Best Value Bet:** {matchup['best_bet']}")
        st.markdown('</div>', unsafe_allow_html=True)
