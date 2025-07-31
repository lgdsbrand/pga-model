import pandas as pd

# ---- SAMPLE LEADERBOARD ----
def load_leaderboard(tournament):
    data = {
        "Player": ["A. Rai", "M. Fitzpatrick", "K. Bradley", "S. Kim", "R. MacIntyre"],
        "Make Cut %": [76.7, 72.7, 72.5, 72.2, 71.5],
        "Top 20 %": [42.5, 37.5, 36.5, 35.6, 34.5],
        "Top 10 %": [27.1, 23.5, 22.2, 21.6, 20.2],
        "Top 5 %": [16.5, 14.2, 13.0, 12.4, 11.4],
        "Win %": [4.6, 3.8, 3.4, 3.0, 2.7],
        "Edge %": [8, 5, 4, 3, 2]
    }
    return pd.DataFrame(data)

# ---- HIGHLIGHT FOR EDGE % AND BEST STAT ----
def highlight_edges(row):
    styles = []
    max_stat_cols = ["Make Cut %","Top 20 %","Top 10 %","Top 5 %","Win %"]
    for col in row.index:
        if col == "Edge %":
            if row[col] >= 7:
                styles.append("background-color: lightgreen; font-weight: bold")
            elif row[col] <= 3:
                styles.append("background-color: pink")
            else:
                styles.append("")
        elif col in max_stat_cols:
            # Highlight better stats in green (for leaderboards, higher is better)
            if row[col] == max([row[c] for c in max_stat_cols]):
                styles.append("color: green; font-weight: bold")
            else:
                styles.append("")
        else:
            styles.append("")
    return styles

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
    styles = []
    for col in row.index:
        if col == "Model Lean":
            styles.append("background-color: lightgreen; font-weight: bold")
        elif "/" in str(row[col]) and any(ch.isdigit() for ch in str(row[col])):
            # Pick lower scoring avg as green, higher SG as green
            values = row[col].split("/")
            try:
                left_val = float(values[0].replace("+","").strip())
                right_val = float(values[1].replace("+","").strip())
                if "SG" in col:
                    # Higher SG is better
                    styles.append("color: green; font-weight: bold" if left_val>right_val else "")
                elif "Scoring" in col:
                    # Lower score is better
                    styles.append("color: green; font-weight: bold" if left_val<right_val else "")
                else:
                    styles.append("")
            except:
                styles.append("")
        else:
            styles.append("")
    return styles
