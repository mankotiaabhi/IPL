import csv
import matplotlib.pyplot as plt
import os

def top_10_batsman_of_rcb(file_path):
    with open (file_path,'r','utf-8') as file:
        deliveries = csv.DictReader(file)
        res = {}

        for delivery in deliveries:
            batting_team = delivery['batting_team']
            if batting_team == 'Royal  Challengers Banglore':
                batsman = delivery['batsman']
                batsman_runs = int(delivery['batsman_runs'])
                if batsman not in res:
                    res[batsman] = 0
                res[batsman] += batsman_runs
        
        res = dict(sorted(res.items(),key=lambda item: item[1],
                          reverse=True)[:10])
        return res



def plot(file_path):
    top_10_batsman_data = top_10_batsman_of_rcb(file_path)
    batsman_names = list(top_10_batsman_data.keys())
    batsman_runs = list(top_10_batsman_data.values())


    os.makedirs("output", exist_ok=True)
    plt.figure(figsize=(12,8))
    plt.bar(batsman_names, batsman_runs)

    plt.title("Top 10 batsman for RCB")
    plt.xlabel("Batsman")
    plt.ylabel("Runs Scored by Batsman")

    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig("./output/problem2.png")
    plt.show()



def execute():

    file_path = "./data/deliveries.csv"
    plot(file_path)




if __name__ == "__main__":
    execute()
