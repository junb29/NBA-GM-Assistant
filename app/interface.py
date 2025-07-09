import pandas as pd
import os

SEASONS = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

def build_team_features(season):
    input_path = f"data/player_stats_{season}_cleaned.csv"
    output_path = f"data/team_features_{season}.csv"

    df = pd.read_csv(input_path)

    team_features = df.groupby("TEAM_ABBREVIATION").agg({
        'PTS': 'sum',
        'REB': 'mean',
        'AST': 'mean',
        'STL': 'mean',
        'BLK': 'mean',
        'TOV': 'mean',
        'FG_PCT': 'mean',
        'FG3M': 'sum',
        'FG3_PCT': 'mean',
        'FT_PCT': 'mean',
        'PLUS_MINUS': 'mean',
        'AGE': 'mean',
        'MIN': 'sum',
        'GP': 'sum'
    }).reset_index()

    team_features.to_csv(output_path, index=False)
    print(f"Saved team features for {season} to {output_path}")

def build_all_team_features():
    for season in SEASONS:
        build_team_features(season)

if __name__ == "__main__":
    build_all_team_features()
