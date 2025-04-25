#API SETUP & DATAFRAME FORMAT.

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

# Mocking sportsbook lines
points_line = 25.5
assists_line = 6.5
rebounds_line = 5.5

last_game = curry_games.iloc[0]

actual_pts = last_game['PTS']
actual_ast = last_game['AST']
actual_reb = last_game['REB']

print("\n--- Actual Results ---")
print(f"Points: {actual_pts}")
print(f"Assists: {actual_ast}")
print(f"Rebounds: {actual_reb}")

# compare with the lean
print("\n--- Betting Lean Comparison ---")
def compare_leans(avg_stat, actual_stat, line, stat_name):
    print(f"{stat_name}: Avg: {avg_stat:.1f}, Actual: {actual_stat}, Line: {line}")
    if (actual_stat > line and avg_stat > line) or (actual_stat < line and avg_stat < line):
        print(f"{stat_name}: Correct Lean ✅")
    else:
        print(f"{stat_name}: Missed Lean ❌")

compare_leans(avg_pts, actual_pts, points_line, "Points")
compare_leans(avg_ast, actual_ast, assists_line, "Assists")
compare_leans(avg_reb, actual_reb, rebounds_line, "Rebounds")
