"""
This program calculates how many matches each team played in every IPL season
and then shows the result as a stacked bar chart.
"""

import csv
import matplotlib.pyplot as plt
import os


def data_from_file(file_path):
    """
    Open the matches file and return all rows as a list.
    Each row represents one match.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def number_of_matches_played_by_team_by_year(file_path):
    """
    For each season, count how many matches every team played.
    Since each match has two teams (team1 and team2),
    we increase the count for both.
    """
    matches = data_from_file(file_path)
    matches_per_year = {}

    for match in matches:
        season = match['season']
        team1 = match['team1']
        team2 = match['team2']

        # If this season is not added yet, create it
        if season not in matches_per_year:
            matches_per_year[season] = {}

        # Make sure both teams exist in that season
        if team1 not in matches_per_year[season]:
            matches_per_year[season][team1] = 0

        if team2 not in matches_per_year[season]:
            matches_per_year[season][team2] = 0

        # Add one match for both teams
        matches_per_year[season][team1] += 1
        matches_per_year[season][team2] += 1

    return matches_per_year


def plot(file_path):
    """
    Create a stacked bar chart showing matches played
    by teams in each season.
    """

    data = number_of_matches_played_by_team_by_year(file_path)

    # Collect all team names
    all_teams = set()
    for season_data in data.values():
        all_teams.update(season_data.keys())

    all_teams = sorted(all_teams)
    seasons = sorted(data.keys())

    # Prepare data in plotting format
    team_data = {
        team: [data[season].get(team, 0) for season in seasons]
        for team in all_teams
    }

    bottom = [0] * len(seasons)

    plt.figure(figsize=(12, 8))

    # Draw stacked bars team by team
    for team, values in team_data.items():
        plt.bar(range(len(seasons)), values, bottom=bottom, label=team)
        bottom = [b + v for b, v in zip(bottom, values)]

    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.title("Matches Played by Each Team Per Season")
    plt.xticks(range(len(seasons)), seasons, rotation=45)

    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1))
    plt.tight_layout()

    # Make sure output folder exists
    os.makedirs("output", exist_ok=True)

    plt.savefig("./output/problem4.png")
    plt.show()


def execute():
    """
    Start the program from here.
    """
    file_path = "./data/matches.csv"
    plot(file_path)


if __name__ == "__main__":
    execute()
