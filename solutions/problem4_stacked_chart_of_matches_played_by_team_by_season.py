import csv
import matplotlib.pyplot as plt
import os

def data_from_file(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        data = list(csv.DictReader(file))
    return data


def number_of_matches_played_by_team_by_year(file_path):

    matches = data_from_file(file_path)

    total_no_of_matches_by_team_by_year = {}

    for match in matches:
        team1 = match['team1']
        team2 = match['team2']
        season = match['season']

        if season not in total_no_of_matches_by_team_by_year:
            total_no_of_matches_by_team_by_year[season] = {}

        if team1 not in total_no_of_matches_by_team_by_year[season]:
            total_no_of_matches_by_team_by_year[season][team1] = 0

        if team2 not in total_no_of_matches_by_team_by_year[season]:
            total_no_of_matches_by_team_by_year[season][team2] = 0

        total_no_of_matches_by_team_by_year[season][team1] += 1
        total_no_of_matches_by_team_by_year[season][team2] += 1

    return total_no_of_matches_by_team_by_year


def plot(file_path):

    data = number_of_matches_played_by_team_by_year(file_path)

    all_teams = set()
    for season_data in data.values():
        all_teams.update(season_data.keys())
    all_teams = sorted(all_teams)

    years = sorted(data.keys())

    teams_matches_per_year = {
        team: [data[year].get(team, 0) for year in years]
        for team in all_teams
    }

    bottom = [0]*len(years)

    plt.figure(figsize=(12,8))

    for team, matches in teams_matches_per_year.items():
        plt.bar(range(len(years)), matches, bottom=bottom, label=team)
        bottom = [b + m for b, m in zip(bottom,matches)]

    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.title("Number of Matches Played by Teams Per Year")
    plt.xticks(range(len(years)), years, rotation=45)
    plt.legend(loc="upper left", bbox_to_anchor=(1.05,1), title="Teams")
    plt.tight_layout()

    os.makedirs("output", exist_ok=True)
    plt.savefig('./output/problem4.png')
    plt.show()


def execute():
    file_path = './data/matches.csv'
    plot(file_path)


if __name__ == "__main__":
    execute()
