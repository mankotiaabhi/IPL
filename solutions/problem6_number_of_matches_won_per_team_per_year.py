"""
This script finds how many matches each IPL team played
in every season and displays the result as a stacked bar chart.
"""

import csv
import matplotlib.pyplot as plt
import os


def read_matches(file_path):
    """
    Read the matches CSV file and return all rows.
    Each row represents one match.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def count_matches_by_year(file_path):
    """
    Count how many matches each team played in each season.
    Since every match has two teams, both teams get +1.
    """

    matches = read_matches(file_path)
    matches_data = {}

    for match in matches:
        season = match["season"]
        team1 = match["team1"]
        team2 = match["team2"]

        # Create season entry if it doesn't exist
        if season not in matches_data:
            matches_data[season] = {}

        # Increase match count for both teams
        matches_data[season][team1] = matches_data[season].get(team1, 0) + 1
        matches_data[season][team2] = matches_data[season].get(team2, 0) + 1

    return matches_data


def plot_matches(file_path):
    """
    Plot a stacked bar chart showing
    matches played by teams per season.
    """

    data = count_matches_by_year(file_path)

    seasons = sorted(data.keys())

    # Get all unique team names
    teams = sorted({team for season in data.values() for team in season})

    # Prepare data for plotting
    team_wise_counts = {
        team: [data[year].get(team, 0) for year in seasons]
        for team in teams
    }

    bottom_values = [0] * len(seasons)

    plt.figure(figsize=(12, 8))

    for team, values in team_wise_counts.items():
        plt.bar(seasons, values, bottom=bottom_values, label=team)
        bottom_values = [b + v for b, v in zip(bottom_values, values)]

    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.title("Matches Played by Each Team Per Season")
    plt.xticks(rotation=45)
    plt.legend(loc="upper left", bbox_to_anchor=(1.05, 1))

    plt.tight_layout()

    os.makedirs("output", exist_ok=True)
    plt.savefig("./output/problem6.png")
    plt.show()


def main():
    file_path = "./data/matches.csv"
    plot_matches(file_path)


if __name__ == "__main__":
    main()
