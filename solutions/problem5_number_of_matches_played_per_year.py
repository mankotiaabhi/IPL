import csv
import matplotlib.pyplot as plt
import os




def number_of_matches_played_per_year(file_path):
    with open(file_path,'r',encoding='utf-8') as file:
        res = {}
        data = csv.DictReader(file)
        for matches in data:
            year = matches["season"]
            if year not in res:
                res[year] = 0
            res[year] += 1

    return res



def plot(file_path):
    data = number_of_matches_played_per_year(file_path)

    total_no_matches = list(data.values())
    years = list(data.keys())

    plt.figure(figsize=(10,8))
    plt.bar(years, total_no_matches, color="green")

    plt.title("Number of Matches Played By Year")
    plt.xlabel("Years")
    plt.ylabel("Number of Matches Played")

    plt.xticks(rotation=45)
    plt.subplots_adjust(bottom=0.25)

    plt.savefig('./output/problem5.png')
    plt.show()


def execute() :
    file_path = './data/matches.csv'
    plot(file_path)



if __name__ == "__main__":
    execute()