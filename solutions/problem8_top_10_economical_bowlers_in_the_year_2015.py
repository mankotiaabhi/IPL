"""Importing CSV to handle csv files"""
import csv
import matplotlib.pyplot as plt
import os
plt.switch_backend('TkAgg')


def read_data_from_file(file_path):
    """
    Read CSV file and return rows as list of dictionaries.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


def top_10_economical_bowlers_in_the_year(year):
    """
    Find top 10 bowlers with best economy rate in given season.
    """

    deliveries = read_data_from_file('./data/deliveries.csv')
    matches = read_data_from_file('./data/matches.csv')

    # Collect match IDs for selected year
    match_ids_for_year = {
        match['id']
        for match in matches
        if match['season'] == str(year)
    }

    bowler_stats = {}

    for delivery in deliveries:
        if delivery['match_id'] in match_ids_for_year:

            bowler = delivery['bowler']

            # Exclude byes and legbyes from bowler's conceded runs
            runs_conceded = (
                int(delivery['total_runs'])
                - int(delivery['bye_runs'])
                - int(delivery['legbye_runs'])
            )

            is_illegal_ball = (
                int(delivery['wide_runs']) > 0
                or int(delivery['noball_runs']) > 0
            )

            if bowler not in bowler_stats:
                bowler_stats[bowler] = {
                    'runs': 0,
                    'balls': 0
                }

            bowler_stats[bowler]['runs'] += runs_conceded

            if not is_illegal_ball:
                bowler_stats[bowler]['balls'] += 1

    economy_of_bowlers = {}

    for bowler, stats in bowler_stats.items():
        if stats['balls'] > 0:
            economy = (stats['runs'] * 6) / stats['balls']
            economy_of_bowlers[bowler] = economy

    # Sort by economy (ascending = best first)
    top_10 = dict(
        sorted(economy_of_bowlers.items(), key=lambda item: item[1])[:10]
    )

    return top_10


def plot(year):
    """
    Plot bar chart of top 10 economical bowlers.
    """

    data = top_10_economical_bowlers_in_the_year(year)

    bowlers = list(data.keys())
    economies = list(data.values())

    plt.figure(figsize=(10, 8))
    plt.bar(bowlers, economies)

    plt.title(f"Top 10 Economical Bowlers in {year}")
    plt.xlabel("Bowlers")
    plt.ylabel("Economy Rate")

    plt.xticks(rotation=45)
    plt.tight_layout()

    os.makedirs("output", exist_ok=True)
    plt.savefig('./output/problem8.png')
    plt.show()


def execute():
    year = 2015
    plot(year)


if __name__ == '__main__':
    execute()
