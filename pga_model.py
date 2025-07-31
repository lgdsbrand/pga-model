import pandas as pd

# ---- SAMPLE LEADERBOARD ----
def load_leaderboard(tournament):
    # Sample demo data (replace with real model output later)
    data = {
        "Player": ["A. Rai", "M. Fitzpatrick", "K. Bradley", "S. Kim", "R. MacIntyre"],
        "Make Cut %": [76.7, 72.7, 72.5, 72.2, 71.5],
        "Top 20 %": [42.5, 37.5, 36.5, 35.6, 34.5],
        "Top 10 %": [27.1, 23.5, 22.2, 21.6, 20.2],
        "Top 5 %": [16.5, 14.2, 13.0, 12.4, 11.4],
        "Win %": [4.6, 3.8, 3.4, 3.0, 2.7],
        "Edge %": [8, 5, 4, 3, 2]  # Simulated model edges
    }
    return pd.DataFrame(data)

# ---- HIGHLIGHT FOR EDGE % ----
def highlight_edges(row):
    color = ""
    if row["Edge %"] >= 7:
        color = "background-color: lightgreen; font-weight: bold"
    elif row["Edge %"] <= 3:
        color = "background-color: pink"
    return [color if col == "Edge %"
            else "" for col in row.index]

# ---- SAMPLE H2H MATCHUPS ----
def load_matchups(tournament):
    data = {
        "Player 1": ["Scheffler", "Rory McIlroy"],
        "Player 2": ["Rahm", "Spieth"],
        "SG: Total": ["+2.14 / +1.78", "+1.88 / +1.10"],
        "SG: Tee to Green": ["+1.85 / +1.55", "+1.70 / +1.05"],
        "SG: Putting": ["+0.12 / +0.23", "+0.18 / +0.05"],
        "Scoring Avg": ["68.3 / 68.9", "68.8 / 69.5"],
        "Model Lean": ["72% → Scheffler", "65% → Rory"],
        "Best Bet": ["Scheffler -120", "Rory -115"]
    }
    return pd.DataFrame(data)

# ---- HIGHLIGHT MATCHUPS ----
def highlight_matchup(row):
    color = ""
    if "→" in row["Model Lean"]:
        color = "background-color: lightgreen; font-weight: bold"
    return [color if col == "Model Lean"
            else "" for col in row.index]
