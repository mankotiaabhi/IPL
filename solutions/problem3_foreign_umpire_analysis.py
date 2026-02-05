"""Importing CSV to handle csv files"""
import csv
import matplotlib.pyplot as plt
import os

def calculate_number_of_foreign_umpire(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        result = {}
        umpires = csv.DictReader(file)
        for umpire in umpires:
            country = umpire['country']
            if country != 'India':
                if country not in result:
                    result[country] = 0
                result[country] += 1
        return result




def plot(file_path):

    umpires_data = calculate_number_of_foreign_umpire(file_path)

    country_names = list(umpires_data.keys())
    number_of_umpires = list(umpires_data.values())

    plt.figure(figsize=(10,6))

    plt.bar(country_names,number_of_umpires)

    plt.title('Foreign Umpires in IPL By Country')
    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")

    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig('./output/problem3.png')
    plt.show()



def execute() :
    """
    Executes the program to read data, process it, and plot the results.
    """
    file_path = './data/umpire_country.csv'
    plot(file_path)


if __name__ == "__main__" :
    execute()
