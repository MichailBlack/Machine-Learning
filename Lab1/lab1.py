import numpy as np
import matplotlib.pyplot as plt
import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            del row[reader.fieldnames[0]]
            data.append(row)
    return data

def visualize_data(data, title, color):
    x = [float(row["x"]) for row in data]
    y = [float(row["y"]) for row in data]
    plt.title(title)
    plt.scatter(x, y, c=color)
    plt.show()

train_data = read_csv("lab_1_train.csv")
visualize_data(train_data, "Train Data", "b")
