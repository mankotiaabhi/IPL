"""Importing CSV to handle csv files"""
import csv
import matplotlib.pyplot as plt
import os
plt.switch_backend('TkAgg')


def read_data_from_file(file_path):
    """
    Read a CSV file and return all rows as a list of dictionaries.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def extra_runs_conceded_per_team_in_the_year(year):
    """
    Find how many extra runs each team conceded in a given season.
    """

    deliveries = read_data_from_file('./data/deliveries.csv')
    matches = read_data_from_file('./data/matches.csv')

    # First collect all match IDs that belong to the given season
    match_ids_for_year = {
        match['id']
        for match in matches
        if match['season'] == str(year)
    }

    extra_runs_conceded_by_teams_in_the_year = {}

    # Now go through deliveries and sum extra runs for those matches
    for delivery in deliveries:
        if delivery['match_id'] in match_ids_for_year:

            bowling_team = delivery['bowling_team']
            extra_runs = int(delivery['extra_runs'])

            extra_runs_conceded_by_teams_in_the_year[bowling_team] = \
                extra_runs_conceded_by_teams_in_the_year.get(bowling_team, 0) + extra_runs

    return extra_runs_conceded_by_teams_in_the_year


def plot(year):
    """
    Plot a bar chart showing extra runs conceded by each team
    in the selected season.
    """

    data = extra_runs_conceded_per_team_in_the_year(year)

    teams = list(data.keys())
    extra_runs = list(data.values())

    plt.figure(figsize=(10, 8))
    plt.bar(teams, extra_runs)

    plt.title(f"Extra Runs Conceded By Teams in {year}")
    plt.xlabel("Teams")
    plt.ylabel("Extra Runs")

    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs("output", exist_ok=True)
    plt.savefig('./output/problem7.png')
    plt.show()


def execute():
    """
    Start execution from here.
    """
    year = 2016
    plot(year)


if __name__ == '__main__':
    execute()
