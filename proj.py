
from nba_api.stats.endpoints import playergamelog
import pandas as pd

def get_last_games(player_id, num_games=5):
    logs = playergamelog.PlayerGameLog(player_id=player_id, season='2023')
    df = logs.get_data_frames()[0]
    return df.head(num_games)  # Return most recent games

# Steph Curry's player ID is 201939
curry_games = get_last_games(201939)

# Display basic stats
print(curry_games[['GAME_DATE', 'MATCHUP', 'PTS', 'AST', 'REB']])

# Calculate averages
avg_pts = curry_games['PTS'].mean()
avg_ast = curry_games['AST'].mean()
avg_reb = curry_games['REB'].mean()

print("\n--- 5 Game Averages ---")
print(f"Points: {avg_pts:.1f}")
print(f"Assists: {avg_ast:.1f}")
print(f"Rebounds: {avg_reb:.1f}")
