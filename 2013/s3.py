import sys

favoriteTeam = int(input())
gamesPlayed= int(input())
teamScores = [0,0,0,0]

for _ in range(gamesPlayed):
    game = list(map(int, input().split()))
    if game[2] > game[3]:
        teamScores[game[0]-1] += 3
    elif game[2] == game[3]:
        teamScores[game[0]-1] += 1
        teamScores[game[1]-1] += 1
    else:
        teamScores[game[1]-1] += 3

print(teamScores)